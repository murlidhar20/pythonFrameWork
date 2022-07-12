
@echo off 
REM pytest -v -s --alluredir="C:\Users\HP\PycharmProjects\pythonFrameWork\AllureReport" testCase/smoke_test.py --browser chrome
pytest -v -s -m "sanity" --alluredir="C:\Users\HP\PycharmProjects\pythonFrameWork\AllureReport" testCase/smoke_test.py --browser chrome
REM pytest -v -s -m "sanity"  testCase/smoke_test.py --browser firefox
REM pytest -v -s -m "sanity"  testCase/smoke_test.py --browser chrome
pause

