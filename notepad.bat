@echo off
for /L %%i in (4,1,33) do (
    setlocal enabledelayedexpansion
    set "folder=day00%%i"
    set "folder=!folder:~-5!"
    mkdir "!folder!"
    endlocal
)
