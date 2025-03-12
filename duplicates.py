import csv
import sys
from collections import defaultdict

def encontrar_duplicados(csv_file):
    registros = defaultdict(list)
    
    with open(csv_file, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector)  # Leer encabezado
        
        for num_linea, fila in enumerate(lector, start=2):  # Comienza en 2 por el encabezado
            clave = tuple(fila)  # Se usa la fila completa como clave
            registros[clave].append(num_linea)
    
    duplicados = {k: v for k, v in registros.items() if len(v) > 1}
    total_duplicados = sum(len(v) - 1 for v in duplicados.values())
    
    if duplicados:
        print(f"Se encontraron {total_duplicados} registros repetidos en total.")
        print("Detalles de los registros duplicados:")
        for clave, lineas in duplicados.items():
            print(f"Registro: {clave} en líneas: {lineas} (Aparece {len(lineas)} veces)")
    else:
        print("No se encontraron registros duplicados.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python duplicates.py <archivo.csv>")
    else:
        encontrar_duplicados("data/" + sys.argv[1])
