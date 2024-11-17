import gradio as gr
import lemma_module as lemma
import syllables_and_POS as sylPOS
import re

def lemmatize_main(text: str) -> dict:

    matches = re.finditer(r"[\w-]+", text)

    result = []

    for word in matches:
        result.append({
            "entity": lemma.get_lemma(word.group(0)),
            "start": word.start(),
            "end": word.end(),
            "word": word.group(0)
        })

    return {"text": text, "entities": result}

def syllables_and_POS_main(text: str) -> dict:
    
    matches = re.finditer(r"[\w-]+", text)

    result = []

    for word in matches:
        result.append({
            "entity": sylPOS.main(word.group(0)),
            "start": word.start(),
            "end": word.end(),
            "word": word.group(0)
        })

    return {"text": text, "entities": result}

with gr.Blocks(theme=gr.themes.Monochrome()) as app:
    gr.Markdown('# Лабораторна робота')
    gr.Markdown('Лематизація, поділ на склади та визначення частини мови слів')

    with gr.Tab("Лематизація"):
        title='Автоматичний лематизатор'
        
        with gr.Row():
            with gr.Column():
                textbox = gr.Textbox(
                    label="Текст для лематизації",
                    info='Введіть текст для автоматичної лематизації.'
                )
                test_texts = gr.Examples(
                    label="Тестові тексти",
                    examples=[
                        "Сонце повільно ховалося за обрієм.",
                        "У супермаркеті сьогодні було дуже людно.",
                        "Кіт стрибнув на стіл і перекинув чашку.",
                        "Холодний вітер нагадував про наближення зими."
                    ],
                    inputs=textbox
                )
            with gr.Column():
                lemmatized_text = gr.HighlightedText(
                    label='Результат'
                )
                submit_btn = gr.Button("Лематизувати", variant="primary")
    
    submit_btn.click(fn=lemmatize_main, inputs=textbox, outputs=lemmatized_text)

    with gr.Tab("Складоподіл та частина мови"):
        title='Автоматичний лематизатор'
        
        with gr.Row():
            with gr.Column():
                textbox = gr.Textbox(
                    label="Текст для опрацювання",
                    info='Введіть текст, щоб автоматично поділити слова в ньому на склади та визначити їхню частиномовну належність.'
                )
                test_texts = gr.Examples(
                    label="Тестові тексти",
                    examples=[
                        "Сонце повільно ховалося за обрієм.",
                        "У супермаркеті сьогодні було дуже людно.",
                        "Кіт стрибнув на стіл і перекинув чашку.",
                        "Холодний вітер нагадував про наближення зими."
                    ],
                    inputs=textbox
                )
            with gr.Column():
                syllables_result = gr.HighlightedText(
                    label='Результат'
                )
                submit_btn = gr.Button("Опрацювати", variant="primary")
    
    submit_btn.click(fn=syllables_and_POS_main, inputs=textbox, outputs=syllables_result)

app.launch()