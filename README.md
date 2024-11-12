# PIA_G2_PC
 Módulos y scripts sobre tareas de ciberseguridad


Este proyecto es un conjunto de herramientas para tareas de ciberseguridad y monitoreo de redes, que utiliza **Python**, **PowerShell** y **Bash** para interactuar con el sistema y realizar tareas automatizadas. Incluye funciones como la búsqueda de dispositivos en Shodan, monitoreo de cambios en directorios, consulta de abuso de IPs, escaneo de puertos, cifrado y descifrado de archivos, y ejecución de comandos de PowerShell para realizar tareas del sistema.

## Funcionalidades

El script permite ejecutar varias funciones relacionadas con la ciberseguridad y la administración de sistemas, tales como:

- **Búsqueda en Shodan**: Consulta dispositivos expuestos a internet.
- **Monitoreo de directorios**: Detecta cambios en los archivos dentro de un directorio.
- **Consulta de abuso de IP**: Proporciona información sobre posibles abusos de una IP específica.
- **Escaneo de puertos**: Realiza un escaneo de puertos en una IP dada.
- **Cifrado y descifrado de archivos**: Permite cifrar y descifrar archivos sensibles.
- **Ejecución de scripts PowerShell y Bash**: Ejecuta funciones de PowerShell para la gestión de recursos del sistema, limpieza de archivos y análisis con VirusTotal.

## Requisitos

- **Python 3.x**
- **PowerShell** (solo en Windows)
- **Bash** (solo en Linux/macOS)
- **Librerías Python**:
    - `argparse`
    - `subprocess`
    - `logging`
    - `platform`
    - `os`
    - `modulo_encrypt`
    - `ip_abuse_checker`
    - `cybersec`
    - `monitor_hashing`
    - `port_scanner`

Instalar las dependencias de Python:
```bash
pip install -r requirements.txt

Notas importantes sobre personalización:
- En la sección de **Personalización de rutas**, se menciona que las rutas de los scripts de PowerShell y Bash deben ser ajustadas si es necesario, dependiendo del sistema y la ubicación de los archivos. Asegúrate de actualizar los archivos de PowerShell (`funciones_powershell.ps1`) y los scripts de Bash (`scan_ports.sh`, `Network_monitor.sh`) con rutas correctas en tu máquina.
- Si usas Windows, asegúrate de tener permisos de ejecución de scripts de PowerShell (puedes hacerlo ejecutando `Set-ExecutionPolicy RemoteSigned` en PowerShell con privilegios de administrador).
