'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const {evaluate, escape, inline} = require('../public/app.js');
const context = {window:{}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../public/course.js'),'utf8'),context);
const lessons = context.window.COURSE.lessons;
let objective = 0, open = 0;
for (const lesson of lessons) {
  for (const q of lesson.questions) {
    if (q.kind==='choice') {
      assert.equal(evaluate(q,String(q.answer)).correct,true);
      assert.equal(evaluate(q,String((q.answer+1)%q.options.length)).correct,false);
      assert.equal(evaluate(q,'').correct,false);
      assert.equal(evaluate(q,String(q.answer)).expected,q.options[q.answer]);
      objective++;
    } else {
      assert.equal(evaluate(q,'Una respuesta cualquiera').correct,null);
      assert.equal(evaluate(q,'Una respuesta cualquiera').expected,q.answer);
      open++;
    }
  }
}
assert.equal(objective,39);
assert.equal(open,13);
assert.equal(escape('<img src="https://external.invalid/">').includes('<img'),false);
assert.equal(inline('**idea** y `Dense`'),'<strong>idea</strong> y <code>Dense</code>');
console.log(`Comprobadas ${lessons.length} lecciones, ${objective} respuestas objetivas y ${open} respuestas abiertas sin nota automática.`);
