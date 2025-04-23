# browser-use

Este proyecto es una implementación personalizada de la biblioteca [browser-use](https://github.com/browser-use/browser-use), diseñada para facilitar la interacción de agentes de inteligencia artificial con sitios web a través de navegadores reales.

## Características

- Automatización de navegación web mediante agentes inteligentes.
- Configuración sencilla mediante archivos `.env`.
- Ejemplo funcional de ejecución con `run.py`.

## Requisitos

- Python 3.7 o superior.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JeffersonRiobueno/browser-use.git
   cd browser-use
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Instala el navegador Chromium para Playwright:
   ```bash
   playwright install chromium
   ```

## Configuración

Crea un archivo `.env` en la raíz del proyecto basado en `.env-example` y agrega tus claves de API y configuraciones necesarias.

## Ejecución

Para ejecutar el agente:

```bash
python run.py
```

## Estructura del Proyecto

- `run.py`: Script principal para ejecutar el agente.
- `requirements.txt`: Lista de dependencias del proyecto.
- `.env-example`: Ejemplo de archivo de configuración de entorno.
- `report/`: Carpeta destinada a almacenar informes generados por el agente.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cambios o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
