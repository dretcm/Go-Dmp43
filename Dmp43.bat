@echo off
echo BEGIN PROGRAM ...

set /p restart=refresh the environment(y/n)?


if %restart%==y (goto pytube) else goto start


:start
python main.py
exit

:pytube
echo refreshing pytube...
pip uninstall -y pytube
pip install pytube
goto start

