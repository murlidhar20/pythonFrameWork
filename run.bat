
@echo off 
REM pytest -v -s --alluredir="C:\Users\HP\PycharmProjects\pythonFrameWork\AllureReport" testCase/test_login.py --browser chrome
pytest -v -s -m "sanity" --alluredir="C:\Users\HP\PycharmProjects\pythonFrameWork\AllureReport" testCase/test_login.py --browser chrome
pause

