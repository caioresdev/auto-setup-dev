import os
import subprocess

# Função para instalar um software utilizando o gerenciador de pacotes Chocolatey (Windows)
def install_with_choco(software):
    subprocess.run(['choco', 'install', software, '-y'])

# Função para instalar um software utilizando o gerenciador de pacotes npm
def install_with_npm(package):
    subprocess.run(['npm', 'install', '-g', package])

# Função para instalar um software utilizando o gerenciador de pacotes pip
def install_with_pip(package):
    subprocess.run(['pip', 'install', package])

# Lista de softwares a serem instalados
softwares = [
    "git",
    "vscode",
    "docker-desktop",
    "windows-terminal",
    "insomnia",
    "figma",
    "drawio",
    "powertoys",
    "devtoys",
    "mongodb-compass-community",
    "mysql",
    "chrome",
    "brave",
    "notion",
    "discord",
    "whatsapp",
    "spotify",
    "lively-wallpaper",
    "python",
    "nodejs"
]

# Solicitar e-mail ao usuário
email = input("Digite seu endereço de email: ")

# Instalar os softwares
for software in softwares:
    install_with_choco(software)

# Instalar clientes MongoDB e MySQL
install_with_choco("mongodb-compass-community")
install_with_choco("mysql")

# Instalar Python e NodeJS
install_with_choco("python")
install_with_choco("nodejs")

print("Instalação completa!")
