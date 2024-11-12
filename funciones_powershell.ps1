#ingresa la ruta absoluta de cada modulo


# Importar los módulos necesarios (asumiendo que están ubicados en la misma ruta que el script)
Import-Module "C:\Program Files\WindowsPowerShell\Modules\PResources\System_Resources.psm1"
Import-Module "C:\Program Files\WindowsPowerShell\Modules\PResources\limpieza_archivosd.psm1"
Import-Module "C:\Program Files\WindowsPowerShell\Modules\PResources\archivosocultosd.psm1"
Import-Module "C:\Program Files\WindowsPowerShell\Modules\PResources\Virus-total.psm1"

# Funciones para ejecutar según la opción

function EjecutarSystemResourceData {
    SystemResourceData
}

function EjecutarRemoveTempFiles {
    Remove-TempFiles
}

function EjecutarRemoveOldFiles {
    Remove-OldFiles
}

function EjecutarGetHiddenFiles {
    Get-HiddenFiles
}

function EjecutarAnalyzeFile {
    AnalyzeFile
}

# Comprobamos el argumento pasado para ejecutar la función correspondiente
param(
    [string]$accion
)

switch ($accion) {
    "SystemResourceData" { EjecutarSystemResourceData }
    "RemoveTempFiles" { EjecutarRemoveTempFiles }
    "RemoveOldFiles" { EjecutarRemoveOldFiles }
    "GetHiddenFiles" { EjecutarGetHiddenFiles }
    "AnalyzeFile" { EjecutarAnalyzeFile }
    default { Write-Host "Acción no válida." }
}