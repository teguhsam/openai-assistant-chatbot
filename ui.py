import gradio as gr
from chatbot import chat

def create_ui():
    with gr.Blocks() as ui:
        with gr.Row():
            chatbot = gr.Chatbot(height=500)
            image_output = gr.Image(height=500)
        with gr.Row():
            msg = gr.Textbox(label="Chat with our AI Assistant:")
        with gr.Row():
            clear = gr.Button("Clear")

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            user_message = history[-1][0]
            bot_message, image = chat(user_message, history[:-1])
            history[-1][1] = bot_message
            return history, image

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, [chatbot, image_output]
        )
        clear.click(lambda: None, None, chatbot, queue=False)

    return ui
