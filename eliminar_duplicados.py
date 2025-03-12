import sys
import pandas as pd

def eliminar_duplicados(archivo_csv):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(archivo_csv)
        
        # Eliminar duplicados
        df_sin_duplicados = df.drop_duplicates()
        
        # Sobrescribir el archivo original sin duplicados
        df_sin_duplicados.to_csv(archivo_csv, index=False)
        
        print(f"Se han eliminado los registros duplicados. Archivo actualizado: {archivo_csv}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python eliminar_duplicados.py <archivo.csv>")
    else:
        eliminar_duplicados('data/' + sys.argv[1])
