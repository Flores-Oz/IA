@echo off
cd /d "%~dp0"
python -m unittest discover -s tests -v
node tests\test_page.js
pause
