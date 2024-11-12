import argparse
import subprocess
import logging
import os
import platform
from modulo_encrypt import encrypt_file, decrypt_file
from ip_abuse_checker import check_ip_abuse
from cybersec import search_shodan
from monitor_hashing import monitor_directory
from port_scanner import scan_ports

logging.basicConfig(filename='script_final.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_os():
    """
    Verifica el sistema operativo actual y muestra el lenguaje de script correspondiente.
    """
    actual_os = platform.system()
    if actual_os == "Windows":
        print("Sistema operativo: Windows. Lenguaje ejecutable: PowerShell y Python.")
    elif actual_os == "Linux" or actual_os == "Darwin":
        print("Sistema operativo: Linux o MacOS. Lenguaje ejecutable: Bash y Python.")
    else:
        print(f"El sistema operativo {actual_os} no es compatible con este script.")
    return actual_os

def run_ps(action):
    """Ejecuta un script de PowerShell con la acción especificada."""
    try:
        # Ejecutar el script de PowerShell y pasar la acción como parámetro
        result = subprocess.run(
            ['powershell', '-ExecutionPolicy', 'ByPass', '-File', 'funciones_powershell.ps1', action],
            check=True, text=True, capture_output=True
        )
        
        # Log y mostrar el resultado
        logging.info(f"Script de PowerShell ejecutado con éxito: {action}")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar el script de PowerShell: {e}")
        print(f"Error al ejecutar el script de PowerShell: {e}")

def submenu_ps():
    """Submenú de opciones específicas de PowerShell."""
    while True:
        print("\nSubmenú PowerShell")
        print("1) Ver recursos del sistema")
        print("2) Remover archivos temporales")
        print("3) Remover archivos antiguos")
        print("4) Limpiar directorio")
        print("5) Buscar archivos ocultos")
        print("6) Consultar archivo con VirusTotal")
        print("7) Salir del Submenú PowerShell")

        option = input("Selecciona una opción: ")

        if option == '1':
            run_ps('SystemResourceData')
        elif option == '2':
            run_ps('RemoveTempFiles')
        elif option == '3':
            run_ps('RemoveOldFiles')
        elif option == '5':
            run_ps('GetHiddenFiles')
        elif option == '6':
            run_ps('AnalyzeFile')
        elif option == '7':
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def submenu_bash(path):
    """Submenú de opciones específicas de Bash."""
    while True:
        print("\nSubmenú Bash")
        print("1) Escanear puertos")
        print("2) Monitorizar red")
        print("3) Salir del Submenú Bash")

        option = input("Selecciona una opción: ")

        if option == '1':
            run_bash(f"{path}/scan_ports.sh")
        elif option == '2':
            run_bash(f"{path}/Network_monitor.sh")
        elif option == '3':
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def main():
    parser = argparse.ArgumentParser(description="Script de ciberseguridad y monitoreo.")
    parser.add_argument("-shodan", help="Busca dispositivos en Shodan", action="store_true")
    parser.add_argument("-monitor", help="Monitorea cambios en un directorio", action="store_true")
    parser.add_argument("-ip", help="Consulta datos de abuso de una IP", action="store_true")
    parser.add_argument("-scan", help="Escanea los puertos de una IP", action="store_true")
    parser.add_argument("-encrypt", help="Cifra un archivo", action="store_true")
    parser.add_argument("-decrypt", help="Descifra un archivo", action="store_true")
    parser.add_argument("-ps", help="Muestra el submenú de opciones de PowerShell", action="store_true")
    parser.add_argument("-bash", help="Muestra el submenú de opciones de Bash", action="store_true")

    args = parser.parse_args()
    actual_os = check_os()

    if args.shodan:
        query = input("Introduce la consulta para buscar en Shodan: ")
        search_shodan(query)

    elif args.monitor:
        directory = input("Introduce la ruta del directorio a monitorear: ")
        monitor_directory(directory)

    elif args.ip:
        ip_address = input("Introduce la dirección IP a consultar: ")
        check_ip_abuse(ip_address)

    elif args.scan:
        ip_address = input("Introduce la dirección IP a escanear: ")
        start_port = int(input("Introduce el puerto inicial: "))
        end_port = int(input("Introduce el puerto final: "))
        port_states = scan_ports(ip_address, start_port, end_port)
        for port, state in port_states.items():
            print(f"Puerto {port}: {state}")

    elif args.encrypt:
        file_path = input("Introduce la ruta del archivo a cifrar: ")
        encrypt_file(file_path)

    elif args.decrypt:
        enc_file_path = input("Introduce la ruta del archivo cifrado a descifrar: ")
        decrypt_file(enc_file_path)

    elif args.ps:
        submenu_ps()
                    
    elif args.bash:
        path = input("Ingresa la ruta donde se encuentran los scripts de Bash: ")
        if os.path.isdir(path):
            submenu_bash(path)
        else:
            print(f"La ruta '{path}' no existe o no es un directorio válido.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
