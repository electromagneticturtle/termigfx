@echo off
cmd /k "cd %~dp0\venv\Scripts & activate & cd %~dp0 & %~dp0venv\Scripts\python.exe test.py runserver & cd %~dp0\venv\Scripts & deactivate & exit"
pause