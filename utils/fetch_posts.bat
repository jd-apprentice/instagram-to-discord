@echo off

set "username=%~1"

if "%username%"=="" (
    echo "username is empty"
    exit /b 1
)

if not exist "%username%" (
    timeout /t 10
    instaloader "%username%" --no-captions

    for %%F in ("%username%\*.json.xz") do (
        echo %%~nxF | findstr /r "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" >nul || (
            del "%%F"
        )
    )

    for /r "%username%" %%F in (*.txt *.jpg *.mp4) do (
        del "%%F"
    )

    del "%username%\id"
    exit /b 1
)

timeout /t 10
instaloader "%username%" --fast-update --no-captions

for %%F in ("%username%\*.json.xz") do (
    echo %%~nxF | findstr /r "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" >nul || (
        del "%%F"
    )
)

for /r "%username%" %%F in (*.txt *.jpg *.mp4) do (
    del "%%F"
)

del "%username%\id"
