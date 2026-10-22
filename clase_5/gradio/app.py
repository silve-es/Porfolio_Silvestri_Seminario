import os
import gradio as gr

# Función de saludo original
def saludar(nombre):
    return f"Hola {nombre}, ¡bienvenido a mi app en Render con Gradio!"

# Función nueva
def calcular_cuadrado(numero):
    resultado = numero ** 2
    return f"El cuadrado de {numero} es: {resultado}"

# Interfaz con Blocks
with gr.Blocks() as demo:
    gr.Markdown("# Aplicación con Gradio en Render")
    
    with gr.Row():
        nombre_input = gr.Textbox(label="Tu nombre")
        salida_texto = gr.Textbox(label="Respuesta")
        btn_saludar = gr.Button("Saludar")
        btn_saludar.click(fn=saludar, inputs=nombre_input, outputs=salida_texto)

    with gr.Row():
        slider_input = gr.Slider(minimum=1, maximum=10, step=1, label="Elegí un número")
        salida_slider = gr.Textbox(label="Resultado")
        btn_calcular = gr.Button("Calcular cuadrado")
        btn_calcular.click(fn=calcular_cuadrado, inputs=slider_input, outputs=salida_slider)

# Configuración  para servidores en la nube (Render)
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)