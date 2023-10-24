# VulnScanner

VulnScanner es una herramienta de escaneo de vulnerabilidades que utiliza `nmap` y `searchsploit` para identificar y verificar vulnerabilidades en servicios detectados en un objetivo.

## Instalación

Antes de ejecutar la herramienta, asegúrate de tener instalado `nmap` y `searchsploit`. Luego, instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

## Uso

Para utilizar VulnScanner:

```bash
./vulnscanner_v1.py [IP o DOMINIO OBJETIVO]
```

Por ejemplo:
```bash
./vulnscanner_v1.py example.com
```
o
```bash
./vulnscanner_v1.py X.X.X.X
```


## Estructura del Proyecto

- **vulnscanner_v1.py**: El script principal de la herramienta.
- **/test**: Contiene pruebas unitarias para la herramienta.
- **/examples**: Ejemplos de cómo usar la herramienta.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un "fork" del repositorio y envía un "pull request" con tus cambios.

