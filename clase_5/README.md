##cse 05 - Aplicaciones desplegadas en Render

## Links de los deploys en la nube
# **Gradio en Render:** https://proyecto-integrador-gradio.onrender.com
# **Streamlit en Render:** https://proyecto-integrador-streamlit.onrender.com

---

## ¿Qué hace cada aplicación?
* **App de Gradio:** Utiliza una interfaz basada en bloques (`gr.Blocks`) con componentes interactivos y eventos explícitos mediante botones.
* **App de Streamlit:** Reproduce la misma lógica, aprovechando el flujo de ejecución de Streamlit.

---

## ¿Cómo se publicó?
Ambas aplicaciones se publicaron utilizando **Render** como plataforma  mediante dos servicios web independientes:
1. Se configuró el **Root Directory** apuntando a sus respectivas carpetas (`Clase_05/gradio` y `Clase_05/streamlit`).
2. Se indicó el comando de compilación (`pip install -r requirements.txt`).
3. Se ajustó el comando de arranque para que las apps escuchen de manera universal en la dirección `0.0.0.0` y lean la variable de entorno `PORT`.

---

## Diferencias encontradas entre Gradio y Streamlit
* **Gestión de eventos vs. Ejecución lineal:** Gradio maneja la interactividad atando explícitamente eventos a componentes mediante funciones de retrollamada (`click`), mientras que Streamlit ejecuta todo el script de arriba hacia abajo cada vez que el usuario interactúa con un elemento.
* **Configuración del servidor:** En Gradio, la escucha en el puerto y la red se define directamente dentro del código de Python (`demo.launch`), mientras que en Streamlit se maneja externamente a través de los argumentos de la línea de comandos (`--server.port` y `--server.address`).
