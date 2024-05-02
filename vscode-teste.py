import os
import subprocess
import requests

def download_vscode_installer():
    # URL do instalador do VSCode para Windows (64 bits)
    url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"

    # Nome do arquivo de destino
    filename = "vscode_installer.exe"

    # Realiza o download do arquivo
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    return filename

def install_vscode_installer(installer_path):
    # Executa o instalador do VSCode
    subprocess.run([installer_path, "/silent"], check=True)

def main():
    # Diretório de trabalho
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Baixa o instalador do VSCode
    installer_path = download_vscode_installer()

    # Instala o VSCode
    install_vscode_installer(installer_path)

    print("Visual Studio Code foi instalado com sucesso!")

if __name__ == "__main__":
    main()
