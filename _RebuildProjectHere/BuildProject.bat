@echo off
setlocal

REM Get default path to the .uproject file
REM Folder containing this batch file
set "SCRIPT_DIR=%~dp0"
REM Go up one folder
set "PARENT_DIR=%SCRIPT_DIR%.."
REM For loop to find .uproject file in the parent directory
for %%f in ("%PARENT_DIR%\*.uproject") do set "PROJECT_PATH=%%f"

REM Default UE path
set "UE_PATH=C:\Program Files\Epic Games\UE_5.6"
set "UE_Build_Path=\Engine\Build\BatchFiles\Build.bat"

REM Load saved paths if a save file exists
if exist build_config.txt (
	for /f "tokens=1* delims==" %%a in (build_config.txt) do (
			if "%%a"=="PROJECT_PATH" set "PROJECT_PATH=%%b"
			if "%%a"=="UE_PATH" set "UE_PATH=%%b"
		)
	)
)

REM Validate project path to make sure it exists
if not exist "%PROJECT_PATH%" (
	call :InputProject_Path
)

REM Validate path to UE build file to make sure it exists
if not exist "%UE_PATH%%UE_Build_Path%" (
	call :InputUE_Path
)

REM Save new paths if they were updated
if defined paths_updated (
    echo PROJECT_PATH=%PROJECT_PATH%>build_config.txt
    echo UE_PATH=%UE_PATH%>>build_config.txt
)

REM Print out the used paths and run the Unreal build batch file
echo Using Project Path: %PROJECT_PATH%
echo Using Engine Path: %UE_PATH%
echo.
call "%UE_PATH%%UE_Build_Path%" UI_TimeEditor Win64 Development "%PROJECT_PATH%"

REM When complete, allow the user to close the command prompt rather than auto closing
pause

exit /b


REM Subroutine for having user input valid .uproject path
:InputProject_Path
echo Project path "%PROJECT_PATH%" invalid or not found.
echo Please enter path to UI_Time.uproject file (Ex: C:\GitHub\GantRouge\UI_Time.uproject)
echo Use right click to paste 
echo.
set /p PROJECT_PATH="Enter path to UI_Time.uproject: "

REM Validate input path
if exist "%PROJECT_PATH%" (
	echo.
	echo Valid Project path, checking Unreal Engine path validity.
	echo.
	echo.
    set paths_updated=1
    goto :eof
) else (
    echo "%PROJECT_PATH%" is not a valid path, please try again.
	echo.
    goto InputProject_Path
)

REM Subroutine for having user input valid UE path
:InputUE_Path
echo Unreal Engine path "%UE_PATH%" invalid or not found.
echo Please enter path to UE version folder (Ex: C:\Epic Games\UE_5.6)
echo Use right click to paste
echo.
set /p UE_PATH="Enter path to Unreal Engine installation: "

REM Validate input path
if exist "%UE_PATH%%UE_Build_Path%" (
	echo.
	echo Valid Unreal Engine path, starting build.
	echo.
	echo.
    set paths_updated=1
    goto :eof
) else (
    echo "%UE_PATH%" is not a valid path, please try again.
	echo.
    goto InputUE_Path
)