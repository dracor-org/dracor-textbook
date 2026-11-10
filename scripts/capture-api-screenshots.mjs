// Capture the screenshots of the DraCor API documentation (Scalar) used in
// chapter 5 (docs/chapters/05-api-working-with-dracor-programmatically.md).
//
// Requirements: Node.js, Google Chrome and Playwright (`npm install playwright`,
// e.g. in a temporary directory outside the repository).
//
// Usage:
//   node scripts/capture-api-screenshots.mjs [outdir] [baseUrl]
//
//   outdir   where to write the PNG files (default: docs/images/api)
//   baseUrl  DraCor instance (default: https://dracor.org; the current images
//            were taken from https://dev.dracor.org before the v3 release)
//
// The script relies on the Classic layout (the default) and on details of the
// live data, e.g. that the Alsatian Drama Corpus (`als`) is the first corpus
// returned by /corpora. Check the images after each run.
import { chromium } from 'playwright';

const out = process.argv[2] || 'docs/images/api';
const base = process.argv[3] || 'https://dracor.org';
const DOC = `${base}/doc/api`;

const b = await chromium.launch({ channel: 'chrome' });
const ctx = await b.newContext({ viewport: { width: 1400, height: 1000 }, deviceScaleFactor: 2 });
const p = await ctx.newPage();

async function load() {
  await p.goto('about:blank');
  await p.goto(DOC, { waitUntil: 'networkidle' });
  await p.waitForTimeout(2000);
}
async function expand(label) {
  const l = p.locator(`text=${label}`).first();
  await l.click({ force: true });
  await p.waitForTimeout(1000);
  await l.evaluate(e => e.scrollIntoView({ block: 'start' }));
  await p.mouse.wheel(0, -90);
  await p.waitForTimeout(600);
}
async function openClient(path) {
  const re = new RegExp(`Test Request \\(get ${path.replace(/[{}/]/g, m => '\\' + m)}\\)`);
  await p.getByRole('button', { name: re }).first().click();
  await p.waitForTimeout(1800);
}
async function send(waitFor) {
  await p.getByRole('button', { name: /^Send/ }).first().click();
  await p.getByText(waitFor).first().waitFor({ timeout: 60000 });
  await p.waitForTimeout(800);
}
async function codeSnippet() {
  await p.evaluate(() => {
    const el = [...document.querySelectorAll('button')].find(b => b.innerText.startsWith('Code Snippet'));
    el?.click();
  });
  await p.waitForTimeout(800);
}
// Only elements actually visible on top (not hidden underneath the client modal)
const onTop = `(e) => {
  const r = e.getBoundingClientRect();
  if (r.width === 0 || r.height === 0) return false;
  const t = document.elementFromPoint(r.x + Math.min(r.width / 2, 20), r.y + r.height / 2);
  return !!t && (e.contains(t) || t.contains(e));
}`;
// Whole row (key + value) of a parameter in the client's tables
async function cellBox(key) {
  return p.evaluate(([key, onTop]) => {
    const top = eval(onTop);
    const leaf = [...document.querySelectorAll('body *')].find(e =>
      e.children.length === 0 && e.textContent.trim() === key && top(e));
    // vertical extent: the tallest ancestor still only one row high
    let cell = leaf;
    while (cell.parentElement && cell.parentElement.getBoundingClientRect().height < 60) cell = cell.parentElement;
    let wide = leaf;
    while (wide.parentElement && wide.getBoundingClientRect().width < 500) wide = wide.parentElement;
    const v = cell.getBoundingClientRect(), h = wide.getBoundingClientRect();
    return { x: h.x, y: v.y, width: h.width, height: v.height };
  }, [key, onTop]);
}
// Tight box around the visible text of the smallest element matching `re`
async function textBox(re) {
  return p.evaluate(([src, onTop]) => {
    const re = new RegExp(src);
    const top = eval(onTop);
    const cands = [...document.querySelectorAll('body *')].filter(e => re.test(e.textContent) && top(e));
    cands.sort((a, b) => a.textContent.length - b.textContent.length);
    const range = document.createRange();
    range.selectNodeContents(cands[0]);
    const r = range.getBoundingClientRect();
    return { x: r.x, y: r.y, width: r.width, height: r.height };
  }, [re.source, onTop]);
}
// Click the topmost on-screen element with exactly this text
async function clickText(t) {
  const c = await p.evaluate(([t, onTop]) => {
    const top = eval(onTop);
    const e = [...document.querySelectorAll('body *')].filter(e =>
      e.children.length === 0 && e.textContent.trim() === t && top(e)).at(-1);
    const r = e.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  }, [t, onTop]);
  await p.mouse.click(c.x, c.y);
}
async function annotate(items) {
  await p.evaluate((items) => {
    for (const { n, box, badge } of items) {
      const o = document.createElement('div');
      Object.assign(o.style, {
        position: 'fixed', left: `${box.x - 3}px`, top: `${box.y - 3}px`,
        width: `${box.width + 6}px`, height: `${box.height + 6}px`,
        border: '3px solid #d62828', borderRadius: '6px', zIndex: 2147483647, pointerEvents: 'none',
      });
      document.body.appendChild(o);
      if (!n) continue;
      const c = document.createElement('div');
      c.textContent = n;
      const left = badge === 'right' ? box.x + box.width + 10 : box.x - 34;
      Object.assign(c.style, {
        position: 'fixed', left: `${left}px`, top: `${box.y + box.height / 2 - 13}px`,
        width: '26px', height: '26px', lineHeight: '26px', borderRadius: '50%',
        background: '#d62828', color: '#fff', font: 'bold 15px sans-serif', textAlign: 'center',
        zIndex: 2147483647, pointerEvents: 'none',
      });
      document.body.appendChild(c);
    }
  }, items);
}
const shot = (name, clip) => p.screenshot({ path: `${out}/${name}`, ...(clip ? { clip } : {}) });

// 1. Overview: introduction with example pairs, server, client libraries
await load();
await p.evaluate(() => window.scrollTo(0, 0));
await shot('scalar-overview.png', { x: 0, y: 0, width: 1400, height: 1000 });

// 2.–3. Public endpoints; then collapse "Public" so all tag groups with descriptions are visible
await load();
const pub = p.locator('text=Read-only endpoints for corpora').first();
await pub.evaluate(e => e.scrollIntoView({ block: 'start' }));
await p.mouse.wheel(0, -120);
await p.waitForTimeout(400);
await shot('scalar-endpoint-public.png');
await p.locator('button:has-text("Public")').first().click({ force: true });
await p.waitForTimeout(800);
await pub.evaluate(e => e.scrollIntoView({ block: 'start' })).catch(() => {});
await p.waitForTimeout(400);
await shot('scalar-endpoint-groups.png', { x: 0, y: 0, width: 1400, height: 820 });

// 4. /corpora expanded
await load();
await expand('List available corpora');
await shot('scalar-corpora-endpoint.png');

// 5. /corpora with the structured response description (fields, types, required)
await p.setViewportSize({ width: 1400, height: 1300 });
await p.getByRole('button', { name: /200\s+Returns list of available corpora/ }).first().click();
await p.waitForTimeout(800);
await p.locator('text=List available corpora').first().evaluate(e => e.scrollIntoView({ block: 'start' }));
await p.mouse.wheel(0, -90);
await p.waitForTimeout(500);
await shot('scalar-corpora-endpoint-schema.png');
await p.setViewportSize({ width: 1400, height: 1000 });

// 6. /corpora test request after sending, numbered
await load();
await expand('List available corpora');
await openClient('/corpora');
await send(/\d+ OK/);
await codeSnippet();
await annotate([
  { n: '1', box: await cellBox('include') },
  { n: '2', box: await textBox(/^\s*curl\s.*corpora\?include=metrics/), badge: 'right' },
  { n: '3', box: await textBox(/^\s*200 OK\s*$/), badge: 'right' },
  { n: '4', box: await textBox(/^\s*"name": "als",?\s*$/), badge: 'right' },
]);
await shot('scalar-corpora-test-request-numbered.png');

// 7. /corpora/{corpusname} expanded
await load();
await expand('List corpus content');
await shot('scalar-corpora-corpusname-endpoint.png');

// 8. Play endpoint: test request with the playname dropdown open
await load();
await expand('Get metadata and network metrics for a single play');
await openClient('/corpora/{corpusname}/plays/{playname}');
await clickText('lessing-emilia-galotti');
await p.waitForTimeout(800);
await shot('scalar-play-endpoint-examples.png');

// 9. Play endpoint: rus + hamlet → 404
await clickText('hamlet');
await p.waitForTimeout(500);
await clickText('ger');
await p.waitForTimeout(500);
await clickText('rus');
await p.waitForTimeout(500);
await send(/404 Not Found/);
await codeSnippet();
await shot('scalar-play-endpoint-404.png');

await b.close();
