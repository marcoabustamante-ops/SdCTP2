import requests

def obtener_ultimo_gini():
    """
    Recupera el dato del Banco Mundial y devuelve el valor float 
    del índice GINI más reciente para Argentina.
    """
    url = "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # data[0] son metadatos, data[1] es la lista de registros 
            data = response.json()
            registros = data[1]
            
            # Buscamos el primer registro que tenga un valor (el más reciente)
            for reg in registros:
                if reg['value'] is not None:
                    return float(reg['value'])
        return 0.0
    except Exception as e:
        print(f"Error en API: {e}")
        return 0.0

if __name__ == "__main__":
    # Esto te sirve para probarlo tú solo
    print(f"Resultado para C: {obtener_ultimo_gini()}")