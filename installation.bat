@echo off
echo BEGIN THE INSTALLATION ...

set /p start=do you want install packagues(y/n)?

if %start%==y (goto install) else goto finish


:install
pip install pytube
pip install pyqt5
goto finish

:finish
exit