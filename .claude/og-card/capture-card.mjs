// Usage (from this folder, avrg-v1 serving :8124):  node capture-card.mjs "HS 06" ...
// Grab gallery cards from the local site at 4x via raw CDP (headless Chrome, throwaway profile).
import { spawn } from "node:child_process";
import { writeFileSync } from "node:fs";
const refs = process.argv.slice(2);
const chrome = spawn("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  ["--headless=new", "--remote-debugging-port=9337", "--user-data-dir=/tmp/og-card-chrome",
   "--window-size=1440,1000", "--hide-scrollbars", "about:blank"], { stdio: "ignore" });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let ws;
for (let i = 0; i < 40 && !ws; i++) { await sleep(250);
  try { const t = await (await fetch("http://127.0.0.1:9337/json")).json();
    const p = t.find(x => x.type === "page"); if (p) ws = new WebSocket(p.webSocketDebuggerUrl); } catch {} }
await new Promise(r => ws.onopen = r);
let id = 0; const pend = {};
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend[m.id]) { pend[m.id](m); delete pend[m.id]; } };
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
await send("Emulation.setDeviceMetricsOverride", { width: 1440, height: 1000, deviceScaleFactor: 4, mobile: false });
await send("Page.navigate", { url: "http://localhost:8124/index.html?v=og2#hand-shaped" });
await sleep(6000);
for (const ref of refs) {
  const r = await send("Runtime.evaluate", { returnByValue: true, awaitPromise: true, expression: `(async()=>{
    const ft=[...document.querySelectorAll('.d7f .ft')].find(f=>f.closest(".d7f").getBoundingClientRect().width>0&&f.dataset.ref===${JSON.stringify(ref)});
    if(!ft) return null; const c=ft.closest('.d7f'); c.scrollIntoView({block:'center',behavior:'instant'}); await new Promise(r=>setTimeout(r,800)); const fb=c.querySelector('.fflipc'); const faces=()=>[...c.querySelectorAll('img:not(.fface)')].map(i=>i.getAttribute('src')); const before=faces(); if(fb && !before.some(s=>/-top\./.test(s))) fb.click(); await new Promise(r=>setTimeout(r,2500)); window.__flip=[before, faces()]; c.querySelectorAll('.fflipc').forEach(e=>e.style.display='none');
    await new Promise(r=>setTimeout(r,1500)); const b=c.getBoundingClientRect();
    return {x:b.x+scrollX,y:b.y+scrollY,w:b.width,h:b.height,flip:window.__flip}})()` });
  const b = r.result.result.value; if (!b) { console.log("missing", ref); continue; }
  const pad = 24;
  const s = await send("Page.captureScreenshot", { format: "png", captureBeyondViewport: true,
    clip: { x: b.x - pad, y: b.y - pad, width: b.w + pad * 2, height: b.h + pad * 2, scale: 1 } });
  const f = "card-" + ref.replace(/\s+/g, "") + ".png";
  writeFileSync(f, Buffer.from(s.result.data, "base64")); console.log("wrote", f, b);
}
ws.close(); chrome.kill();
