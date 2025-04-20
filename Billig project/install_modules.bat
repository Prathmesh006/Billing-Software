@echo off
echo ===================================
echo Installing all required Python modules...
echo ===================================

:: ---------- Standard Libraries (no installation needed) ----------
echo The following standard libraries are already included with Python:
echo - tkinter
echo - os
echo - time
echo - datetime
echo - shutil
echo - sys
echo - subprocess
echo - re
echo - logging
echo - tempfile
echo - winreg

:: ---------- External Libraries (installed via pip) ----------
echo.
echo Installing external libraries via pip...

pip install pillow
pip install pywin32

echo.
echo ==========================
echo   All modules ready!
echo ==========================

exit
