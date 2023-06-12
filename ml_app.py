import re
import gradio as gr
from gradio import components

def data_processing(text):
    return re.sub(r'[^a-zA-Z0-9]',' ', text)

gradio_ui = gr.Interface(
    fn=data_processing,
    title="Data Processing and Modelling",
    description="Aplikasi Web Data Prosessing dan Modeling",
    inputs=components.Textbox(lines=10, label="Tulis sesuatu disini"),
    outputs=components.Textbox(label="Result"),
)

gradio_ui.launch(share=True)