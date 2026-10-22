import gradio as gr

# 1. función original o de saludo
def saludar(nombre):
    return f"Hola {nombre}, ¡bienvenido a la clase!"

# 2. función propia nueva conectada a un componente nuevo (un Slider)
def calcular_cuadrado(numero):
    resultado = numero ** 2
    return f"El cuadrado de {numero} es: {resultado}"

# 3. interfaz usando Blocks
with gr.Blocks() as demo:
    gr.Markdown("# Actividad Clase 4 - Seminario de Actualización")
    
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

# 4. Corremos la app generando el link temporal
demo.launch(share=True)