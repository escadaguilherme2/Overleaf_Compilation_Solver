@echo off

set "MIKTEX_PORTABLE_DIR=%~dp0MiKTeX\texmfs\install\miktex\bin\x64"

set "PATH=%MIKTEX_PORTABLE_DIR%;%PATH%"

set "TEXMAKER_EXEC=%~dp0Texmaker\texmaker.exe"

start "" "%TEXMAKER_EXEC%"