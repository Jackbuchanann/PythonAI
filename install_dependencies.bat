# Local path to Python installer
$pythonInstallerUrl = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"
$pythonInstallerPath = "$PSScriptRoot\python_installer.exe"

# Download and run the Python installer
Invoke-WebRequest -Uri $pythonInstallerUrl -OutFile $pythonInstallerPath
Start-Process -Wait -FilePath $pythonInstallerPath -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"

# Verify Python installation
$pythonPath = (Get-Command python).Source
Write-Output "Python installed at: $pythonPath"

# Install required Python packages using pip
python -m pip install -r "$PSScriptRoot\requirements.txt"

# Cleanup
Remove-Item $pythonInstallerPath
