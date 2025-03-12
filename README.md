# zonaprop-scrap

Scraper de Zonaprop. Basado en https://github.com/Sotrosca/zona-prop-scraper.

## Modo de uso:

**1- Instalar las dependencias** declaradas en el archivo `requirements.txt`:

Con pip:

```bash
pip install -r requirements.txt
```

**2- Ejecutar el script `zonaprop-scraping.py`** pasando como argumento la url de la página de Zonaprop que se desea scrapear (por default se utilizará la url: https://www.zonaprop.com.ar/departamentos-alquiler.html):

```bash
python zonaprop-scraping.py <url>
```

Por ejemplo:

```bash
python zonaprop-scraping.py https://www.zonaprop.com.ar/departamentos-alquiler.html
```

**3-** El script generará un **archivo `.csv`** en el directorio `data` con las URLs de los inmuebles.
