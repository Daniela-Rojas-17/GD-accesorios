# Miyuki Accesorios

Catálogo de accesorios hechos a mano con mostacillas Miyuki, en versión web estática y Streamlit.

## Opciones de la app Streamlit

La app incluye catálogo, inventario, recomendador por estilo/ocasión/presupuesto,
gestión del pedido, cotización con descuentos e IVA, planificación de producción,
confirmación del pedido y reabastecimiento.

Los precios del catálogo se conservan como referencia. Las recetas de materiales,
los tiempos de producción, costos y existencias son datos de demostración inventados.
El inventario y los pedidos confirmados solo se conservan en la sesión actual; no
representan existencias compartidas ni persistentes del emprendimiento.

## Publicar en Streamlit Community Cloud

1. Inicia sesión en [Streamlit Community Cloud](https://share.streamlit.io/) con la cuenta de GitHub que tiene acceso a este repositorio.
2. Selecciona **Create app** y el repositorio `Daniela-Rojas-17/GD-accesorios`.
3. Elige la rama `main` y el archivo principal `app.py`.
4. En **Advanced settings**, selecciona Python 3.12 y crea la app.
5. Cuando termine el despliegue, comparte la URL que te asigne Streamlit.

Streamlit instalará automáticamente las dependencias de `requirements.txt`. Los cambios que subas a `main` se publican automáticamente.

## Versión estática en GitHub Pages

La página estática también se publica automáticamente desde `main` con el flujo de GitHub Actions en `.github/workflows/pages.yml`:

<https://daniela-rojas-17.github.io/GD-accesorios/>
