const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const { JSDOM } = require('jsdom');
const html = fs.readFileSync('index.html', 'utf8');
const script = fs.readFileSync('city.js', 'utf8');
async function app(hash = '#/home', stored) {
  const dom = new JSDOM(html, { url: 'http://localhost/' + hash, runScripts: 'outside-only', pretendToBeVisual: true });
  const w = dom.window;
  w.confirm = () => true;
  if (stored) w.localStorage.setItem('21city.v1', stored);
  w.eval(script);
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  // Allow RAFs and defer script boot; all interactions use actual DOM handlers.
  await new Promise(r => setTimeout(r, 30));
  const $ = s => w.document.querySelector(s);
  const click = s => $(s).click();
  const input = (s, value) => { $(s).value = value; $(s).dispatchEvent(new w.Event('input', { bubbles: true })); };
  const state = () => JSON.parse(w.localStorage.getItem('21city.v1'));
  return { dom, w, $, click, input, state };
}
test('boots with projects, quests and community totals', async t => {
  const a = await app(); t.after(() => a.dom.window.close());
  assert.equal(a.w.document.querySelectorAll('#homeProjects .pcard').length, 3);
  assert.equal(a.w.document.querySelectorAll('#homeQuests .qcard').length, 4);
  assert.match(a.$('#communityStats').textContent, /5/);
});
test('catalog searches, filters, sorts and shows empty state', async t => {
  const a = await app('#/projects'); t.after(() => a.dom.window.close());
  a.input('#catalogSearch', 'велопарковку');
  // Seed locale follows browser; set RU explicitly.
  a.click('[data-set-lang="ru"]');
  assert.equal(a.w.document.querySelectorAll('#projList .pcard').length, 1);
  a.input('#catalogSearch', 'zzzz-no-match');
  assert.ok(a.$('#projList .empty'));
  a.input('#catalogSearch', ''); a.click('[data-plist="quests"]');
  assert.equal(a.w.document.querySelectorAll('#projList .qrow').length, 4);
  a.click('[data-plist="projects"]');
  a.$('#catalogSort').value = 'funding'; a.$('#catalogSort').dispatchEvent(new a.w.Event('change'));
  assert.equal(a.w.document.querySelectorAll('#projList .pcard').length, 5);
});
test('named donations remain owned by the current user and survive reload', async t => {
  const a = await app(); t.after(() => a.dom.window.close());
  const before = a.state().projects[0].donations.length;
  a.click('#homeProjects [data-donate="1"]'); a.input('#dName', 'Test neighbour'); a.click('#dGo');
  const donation = a.state().projects[0].donations.at(-1);
  assert.equal(donation.you, true); assert.equal(donation.amount, 25);
  const b = await app('#/wallet', JSON.stringify(a.state())); t.after(() => b.dom.window.close());
  assert.equal(b.state().projects[0].donations.length, before + 1);
});
test('rejects invalid offers; valid offer updates minimum budget target', async t => {
  const a = await app(); t.after(() => a.dom.window.close());
  a.click('#homeProjects [data-offer="1"]'); a.click('[data-newoffer="1"]');
  a.input('#oName', 'Local workshop');
  const count = a.state().projects[0].offers.length;
  a.click('#oGo'); assert.equal(a.state().projects[0].offers.length, count);
  a.input('#oPrice', '99'); a.input('#oDays', '3'); a.click('#oGo');
  assert.equal(a.state().projects[0].offers.length, count + 1);
  assert.equal(Math.min(...a.state().projects[0].offers.map(o => o.price)), 99);
});
test('profile editing persists and renders plain text', async t => {
  const a = await app('#/profile'); t.after(() => a.dom.window.close());
  a.input('#profileNameInput', '<b>Neighbour</b>');
  a.$('#profileForm').dispatchEvent(new a.w.Event('submit', { cancelable: true }));
  assert.equal(a.state().user.name, '<b>Neighbour</b>');
  assert.equal(a.$('#profileName').textContent, '<b>Neighbour</b>');
  assert.equal(a.$('#profileName b'), null);
});
test('project deep links and section navigation are restored', async t => {
  const a = await app('#/project/1'); t.after(() => a.dom.window.close());
  assert.equal(a.$('#detail').hidden, false);
  a.w.document.dispatchEvent(new a.w.KeyboardEvent('keydown', { key: 'Escape' }));
  a.click('.tab[data-view="profile"]');
  assert.equal(a.w.location.hash, '#/profile');
  assert.equal(a.$('.tab[aria-current="page"]').dataset.view, 'profile');
});
test('publishes a project and persists an accepted quest', async t => {
  const a = await app(); t.after(() => a.dom.window.close());
  a.click('[data-accept-quest="61"]');
  assert.equal(a.state().quests.find(q => q.id === 61).accepted, true);
  a.click('[data-open-new]'); a.input('#nTitleIn', 'Repair our bench'); a.input('#nDesc', 'A loose plank');
  a.click('#nGo');
  assert.equal(a.state().projects[0].title, 'Repair our bench');
  a.click('#seedLater');
  assert.equal(a.$('#detail').hidden, false);
});
test('corrupt JSON falls back safely; reset requires confirmation', async t => {
  const a = await app('#/profile', '{bad'); t.after(() => a.dom.window.close());
  assert.equal(a.state().projects.length, 5);
  a.input('#profileNameInput', 'Keep me'); a.$('#profileForm').dispatchEvent(new a.w.Event('submit', { cancelable: true }));
  a.w.confirm = () => false; a.click('#btnReset'); assert.equal(a.state().user.name, 'Keep me');
  a.w.confirm = () => true; a.click('#btnReset'); assert.equal(a.state().user.name, '');
});
test('switches between the six languages and keeps the dictionary in sync', async t => {
  const a = await app(); t.after(() => a.dom.window.close());
  const codes = ['ru', 'en', 'es', 'zh', 'ja', 'ko'];
  for (const code of codes) {
    a.click(`[data-set-lang="${code}"]`);
    const root = a.w.document.documentElement;
    assert.equal(root.getAttribute('data-lang'), code);
    assert.equal(root.getAttribute('lang'), code);
    assert.equal(a.$('#langCode').textContent, code.toUpperCase());
    assert.equal(a.state().lang, code);
    // the tab labels come from the dictionary, not from the markup
    assert.ok(a.$('[data-i18n="tabHome"]').textContent.length > 0);
  }
  // seeded data is translated too
  a.click('[data-set-lang="ja"]');
  assert.match(a.$('#homeQuests .qcard h3').textContent, /[ぁ-んァ-ン一-龥]/);
  assert.equal(a.$('[data-i18n="tabProjects"]').textContent, 'プロジェクト');
  a.click('[data-set-lang="zh"]');
  assert.equal(a.$('[data-i18n="tabProjects"]').textContent, '项目');
  a.click('[data-set-lang="ko"]');
  assert.equal(a.$('[data-i18n="tabProjects"]').textContent, '프로젝트');
});
test('landing page switches between the six languages', async t => {
  const landing = fs.readFileSync('landing.html', 'utf8');
  const script2 = fs.readFileSync('app.js', 'utf8');
  const dom = new JSDOM(landing, { url: 'http://localhost/landing.html', runScripts: 'outside-only' });
  const w = dom.window;
  w.eval(script2);
  for (const code of ['ru', 'en', 'es', 'zh', 'ja', 'ko']) {
    w.document.querySelector(`[data-set-lang="${code}"]`).click();
    assert.equal(w.document.documentElement.getAttribute('data-lang'), code);
    assert.equal(w.document.getElementById('langCode').textContent, code.toUpperCase());
  }
  assert.match(w.document.title, /숫자가 PR/);
  w.window.close();
});
test('the how-it-works sheet carries the six Ethereum principles in every language', async t => {
  const a = await app(); t.after(() => a.dom.window.close());
  a.click('[data-how="1"]');
  assert.equal(a.w.document.querySelectorAll('#mHow .prin li').length, 6);
  const neutral = {
    ru: 'Достоверная нейтральность', en: 'Credible neutrality', es: 'Neutralidad creíble',
    zh: '可信的中立', ja: '信頼できる中立性', ko: '신뢰할 수 있는 중립성'
  };
  for (const [code, title] of Object.entries(neutral)) {
    a.click(`[data-set-lang="${code}"]`);
    // principles come from the dictionary, so all six languages are real, not fallbacks
    assert.equal(a.$('#mHow [data-i18n="prin1t"]').textContent, title);
    for (let i = 1; i <= 6; i++) {
      assert.ok(a.$(`#mHow [data-i18n="prin${i}d"]`).textContent.length > 12, `prin${i}d · ${code}`);
    }
  }
  // honesty: the draft states it has no blockchain right next to the principles
  a.click('[data-set-lang="en"]');
  assert.match(a.$('#mHow [data-i18n="prinNote"]').textContent, /no blockchain/i);
  a.click('[data-set-lang="ru"]');
  assert.match(a.$('#mHow [data-i18n="prinNote"]').textContent, /без блокчейна/i);
});
test('landing explains the Ethereum philosophy in six languages and links it in the nav', async t => {
  const landing = fs.readFileSync('landing.html', 'utf8');
  assert.match(landing, /<section class="section" id="philosophy">/);
  assert.match(landing, /<a href="#philosophy">/);
  const script2 = fs.readFileSync('app.js', 'utf8');
  const dom = new JSDOM(landing, { url: 'http://localhost/landing.html', runScripts: 'outside-only' });
  const w = dom.window; w.eval(script2);
  const section = w.document.getElementById('philosophy');
  assert.equal(section.querySelectorAll('article.card').length, 6);
  const expect = {
    ru: 'Шесть принципов, взятых у Ethereum.',
    en: 'Six principles borrowed from Ethereum.',
    es: 'Seis principios tomados de Ethereum.',
    zh: '从 Ethereum 借来的六条原则。',
    ja: 'Ethereum から借りた 6 つの原則。',
    ko: 'Ethereum에서 가져온 여섯 가지 원칙.'
  };
  for (const [code, heading] of Object.entries(expect)) {
    w.document.querySelector(`[data-set-lang="${code}"]`).click();
    assert.equal(w.document.documentElement.getAttribute('data-lang'), code);
    // jsdom does not apply CSS, so the hidden languages stay in textContent:
    // read the span that the language rule would leave visible.
    assert.equal(section.querySelector(`h2 span[lang="${code}"]`).textContent, heading);
    for (const card of section.querySelectorAll('article.card')) {
      assert.equal(card.querySelectorAll('h3 span[lang]').length, 6);
      assert.ok(card.querySelector(`p span[lang="${code}"]`).textContent.length > 12, code);
    }
  }
  // the honesty note sits with the principles and says the draft has no chain
  const note = [...section.querySelectorAll('.card p')].pop();
  assert.match(note.querySelector('span[lang="ru"]').textContent, /нет блокчейна/);
  assert.match(note.querySelector('span[lang="en"]').textContent, /no blockchain/i);
  w.window.close();
});
