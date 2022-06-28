
@echo off 
REM pytest -v -s --alluredir="C:\Users\HP\PycharmProjects\pythonFrameWork\AllureReport" testCase/smoke_test.py --browser chrome
pytest -v -s -m "sanity" --alluredir="C:\Users\HP\PycharmProjects\pythonFrameWork\AllureReport" testCase/smoke_test.py --browser chrome
pause

