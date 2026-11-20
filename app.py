import gradio as gr


def saludar(nombre):
    return f"¡Hola, {nombre}! Bienvenido a mi portfolio de Seminario."


with gr.Blocks() as app:
    gr.Markdown("# Mi primera aplicación con Gradio")
    gr.Markdown("Una aplicación sencilla desarrollada para Seminario.")

    nombre = gr.Textbox(label="Tu nombre")
    boton = gr.Button("Saludar")
    mensaje = gr.Textbox(label="Mensaje")

    boton.click(
        fn=saludar,
        inputs=nombre,
        outputs=mensaje
    )


app.launch()