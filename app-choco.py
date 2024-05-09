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
if not subprocess.run(['choco', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
    print("Instalando Chocolatey...")
    subprocess.run(['powershell', '-Command', '(New-Object System.Net.WebClient).DownloadFile("https://chocolatey.org/install.ps1", "choco-install.ps1")'])
    subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy Bypass -Scope Process -Force; ./choco-install.ps1'])

# Pacotes a serem instalados via Chocolatey
choco_packages = ["git", "vscode", "insomnia", "figma", "brave", "discord", "arcbrowser", "python", "spotify", "whatsapp", "googlechrome", "powertoys", "microsoft-windows-terminal"]

# Instalar os pacotes via Chocolatey
for package in choco_packages:
    print(f"Instalando {package} via Chocolatey...")
    subprocess.run(['choco', 'install', package, '-y'])

# Links e tipos de instalação dos aplicativos que não são instalados via Chocolatey
apps = [
    ("https://downloads.mongodb.com/compass/mongodb-compass-1.42.5-win32-x64.exe", "exe"),
    ("https://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-workbench-community-8.0.36-winx64.msi", "msi"),
    ("https://nodejs.org/dist/v20.13.0/node-v20.13.0-x64.msi", "msi")
]

# Baixar e instalar os aplicativos que não são instalados via Chocolatey
for app_url, app_type in apps:
    download_and_install(app_url, app_type)
