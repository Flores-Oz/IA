// Browser QA with the already installed Edge and native Node APIs; no downloads.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {spawn} from 'node:child_process';

const root = process.cwd();
const edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const delay = ms => new Promise(resolve=>setTimeout(resolve,ms));
const browser = spawn(edge, ['--headless=new','--disable-gpu','--no-sandbox','--no-first-run','--no-default-browser-check',
  '--disable-background-networking','--disable-component-update','--disable-sync','--disable-extensions',
  '--remote-debugging-port=9223','--remote-debugging-address=127.0.0.1',
  `--user-data-dir=${path.join(root,'app_data','browser_qa')}`, 'about:blank'], {windowsHide:true,stdio:'ignore'});
let ws;
const pending = new Map();
let serial = 0;
const errors = [];
const requests = [];
async function send(method,params={}) {
  const id=++serial;
  const result = new Promise((resolve,reject)=>{
    const timer=setTimeout(()=>{pending.delete(id);reject(new Error(`CDP timeout: ${method}`));},12000);
    pending.set(id,{resolve,reject,timer});
  });
  ws.send(JSON.stringify({id,method,params}));
  return result;
}
async function evaluate(expression) {
  const result=await send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});
  if(result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result.value;
}
async function until(expression) {
  for(let n=0;n<60;n++) { if(await evaluate(expression))return; await delay(100); }
  throw new Error(`Page condition failed: ${expression}`);
}
try {
  let tabs;
  for(let n=0;n<60;n++) {
    try { tabs=await (await fetch('http://127.0.0.1:9223/json/list')).json(); if(tabs.some(t=>t.type==='page'))break; } catch(_) {}
    await delay(150);
  }
  const target=tabs?.find(t=>t.type==='page');
  assert.ok(target,'The installed Edge did not open its local debugging endpoint.');
  ws=new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve,reject)=>{ws.addEventListener('open',resolve,{once:true});ws.addEventListener('error',reject,{once:true});});
  ws.addEventListener('message',event=>{
    const message=JSON.parse(event.data);
    if(message.id && pending.has(message.id)) {
      const item=pending.get(message.id);pending.delete(message.id);clearTimeout(item.timer);
      if(message.error)item.reject(new Error(JSON.stringify(message.error)));else item.resolve(message.result);
    }
    if(message.method==='Runtime.exceptionThrown')errors.push(message.params.exceptionDetails.text);
    if(message.method==='Network.requestWillBeSent')requests.push(message.params.request.url);
  });
  await send('Runtime.enable');await send('Page.enable');await send('Network.enable');
  await send('Emulation.setDeviceMetricsOverride',{width:1400,height:1000,deviceScaleFactor:1,mobile:false});
  await send('Page.navigate',{url:'http://127.0.0.1:8501'});
  await until('document.querySelectorAll(".question-card").length===4');
  assert.equal(await evaluate('document.querySelectorAll(".topic-button").length'),13);
  assert.equal(await evaluate('document.querySelectorAll(".feedback").length'),0);
  await evaluate(`(()=>{const q=COURSE.lessons[0].questions[0];const f=document.querySelector('[data-question="'+q.id+'"]');f.querySelector('[value="'+q.answer+'"]').click();f.querySelector('[type="submit"]').click();})()`);
  assert.equal(await evaluate('document.querySelector(".feedback-title").textContent'),'Correcto.');
  await evaluate('document.querySelector("[data-retry]").click()');
  assert.equal(await evaluate('document.querySelectorAll(".feedback").length'),0);
  await evaluate(`(()=>{const q=COURSE.lessons[0].questions[0];const f=document.querySelector('[data-question="'+q.id+'"]');f.querySelector('[value="'+((q.answer+1)%4)+'"]').click();f.querySelector('[type="submit"]').click();})()`);
  assert.equal(await evaluate('document.querySelector(".feedback-title").textContent'),'Revisa esta idea.');
  await evaluate(`(()=>{const t=document.querySelector('textarea');t.value='Mi explicación de las entradas y las capas';t.dispatchEvent(new Event('input',{bubbles:true}));t.closest('form').querySelector('button').click();})()`);
  assert.equal(await evaluate('document.querySelectorAll(".rubric").length'),1);
  await send('Page.reload');
  await until('document.querySelectorAll(".feedback").length===2');
  for(let i=0;i<13;i++) {
    await evaluate(`document.querySelector('#topics [data-topic="'+COURSE.lessons[${i}].id+'"]').click()`);
    assert.equal(await evaluate('document.querySelectorAll(".question-card").length'),4);
    assert.ok(await evaluate(`document.querySelector('h1').textContent===COURSE.lessons[${i}].title`));
  }
  await evaluate(`document.querySelector('#topics [data-topic="normalizacion"]').click()`);
  await evaluate(`document.querySelector('a[href="#questions"]').click()`);
  await send('Page.reload');
  await until(`document.querySelector('h1')?.textContent==='Normalizar: cambiar la escala, no el significado'`);
  await evaluate('window.scrollTo(0,0)');
  const desktop=await send('Page.captureScreenshot',{format:'png'});
  fs.writeFileSync(path.join(root,'app_data','page-desktop.png'),Buffer.from(desktop.data,'base64'));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  assert.equal(await evaluate('document.documentElement.scrollWidth>window.innerWidth'),false,'Horizontal overflow on mobile');
  const mobile=await send('Page.captureScreenshot',{format:'png'});
  fs.writeFileSync(path.join(root,'app_data','page-mobile.png'),Buffer.from(mobile.data,'base64'));
  assert.deepEqual(errors,[],'Browser JavaScript exceptions');
  const external=requests.filter(url=>!url.startsWith('http://127.0.0.1:8501/')&&!url.startsWith('data:'));
  assert.deepEqual(external,[],'Unexpected external page resources');
  console.log('Browser OK: 13 topics; hidden solutions; correct/incorrect feedback; retries; open answers; saved answers; mobile layout; local resources.');
} finally {
  if(ws?.readyState===WebSocket.OPEN) { try {await send('Browser.close');}catch(_){} ws.close(); }
  if(browser.exitCode===null)browser.kill();
  for(const item of pending.values())clearTimeout(item.timer);
}
