import os
import shutil
import time

def deleteFiles(directory):
    total_files = 0
    deleted_files = 0
    files_in_use = []

    for dirpath, dirnames, filenames in os.walk(directory):
        total_files += len(filenames)

        for file in filenames:
            routeFile = os.path.join(dirpath, file)

            try:
                os.remove(routeFile)
                deleted_files += 1
            except PermissionError as e:
                files_in_use.append(routeFile)

        progress = deleted_files / total_files if total_files > 0 else 0
        time.sleep(0.5)
        progress_bar(total_files, progress)

    if len(files_in_use) > 0:
        print("\nArchivos en uso (No eliminados):")
        for file in files_in_use:
            print(file)

    progress_bar(total_files, 1)

    print("\n")
    print(f"Archivos eliminados: {deleted_files}")

def optimizeStorage(directories):
    for directory in directories:
        if os.path.exists(directory):
            print(f"\nDirectorio: {directory}")
            deleteFiles(directory)
        else:
            print(f"El directorio {directory} no existe.")

def progress_bar(total, progress):
    bar_length = 50
    filled_length = int(round(bar_length * progress))
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    percentage = round(progress * 100, 2)
    print(f'[{bar}] {percentage}% complete', end='\r')

# Configuración
directoriesToOptimize = [
    r"C:\Windows\Logs",
    r"C:\Windows\Temp",
    r"C:\Users\YourUser\AppData\Local\Temp"
]

# Ejecución
optimizeStorage(directoriesToOptimize)
print("\n¡Tarea completada!")
