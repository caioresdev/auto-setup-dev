import os
import subprocess
import requests

def download_and_install(url, file_type):
    file_name = url.split('/')[-1]
    print(f"Baixando {file_name}...")
    with open(file_name, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)
    
    print(f"Instalando {file_name}...")
    if file_type == 'exe':
        subprocess.run([file_name], shell=True)
    elif file_type == 'msi':
        subprocess.run(['msiexec', '/i', file_name, '/quiet', '/qn', '/norestart'])

# Instalar Chocolatey se ainda não estiver instalado
if not os.path.exists("C:\\ProgramData\\chocolatey"):
    print("Instalando Chocolatey...")
    subprocess.run(['powershell', '-Command', '(New-Object System.Net.WebClient).DownloadFile("https://chocolatey.org/install.ps1", "choco-install.ps1")'])
    subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy Bypass -Scope Process -Force; ./choco-install.ps1'])

# Links e tipos de instalação dos aplicativos
apps = [
    ("https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe", "exe"),
    ("https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user", "exe"),
    ("https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website", "exe"),
    ("https://www.figma.com/download/desktop/win", "exe"),
    ("https://downloads.mongodb.com/compass/mongodb-compass-1.42.5-win32-x64.exe", "exe"),
    ("https://laptop-updates.brave.com/download/BRV010?bitness=64", "exe"),
    ("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64", "exe"),
    ("https://releases.arc.net/windows/ArcInstaller.exe", "exe"),
    ("https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe", "exe"),
    ("https://download.scdn.co/SpotifySetup.exe", "exe"),
    ("https://get.microsoft.com/installer/download/9NKSQGP7F2NH?cid=website_cta_psi", "exe"),
    ("https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B6E7F39E2-5D20-D2C2-E673-89E25241BCEE%7D%26lang%3Dpt-BR%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe", "exe"),
    ("https://github.com/microsoft/PowerToys/releases/download/v0.80.1/PowerToysUserSetup-0.80.1-x64.exe", "exe"),
    ("https://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-workbench-community-8.0.36-winx64.msi", "msi"),
    ("https://nodejs.org/dist/v20.13.0/node-v20.13.0-x64.msi", "msi"),
    ("https://chocolatey.org/install.ps1", "powershell")  # Apenas para fins de teste
]

# Baixar e instalar os aplicativos
for app_url, app_type in apps:
    download_and_install(app_url, app_type)
