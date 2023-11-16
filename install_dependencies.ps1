# Download and install Python 3.13
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.13.0/python-3.13.0.exe"
$pythonInstallerPath = "$PSScriptRoot\python_installer.exe"

Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath
Start-Process -Wait -FilePath $pythonInstallerPath -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"

# Install required Python packages using pip
python -m pip install -r "$PSScriptRoot\requirements.txt"

# Cleanup
Remove-Item $pythonInstallerPath
