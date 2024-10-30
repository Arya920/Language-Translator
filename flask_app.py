from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from nllb_supported_languages import Languages
import time
import torch


def translate(text, input_language_code, output_language_code, max_length):
    start = time.time()
    model = AutoModelForSeq2SeqLM.from_pretrained(pretrained_model_name_or_path='D:/Language Translator/model',
                                                  local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path = 'D:/Language Translator/model',
                                              local_files_only=True)

    translator = pipeline('translation', model=model,
                          tokenizer=tokenizer,
                          src_lang=input_language_code,
                          tgt_lang=output_language_code,
                          max_length=max_length,
                          device="cuda" if torch.cuda.is_available() else "cpu"
                          )
    translated_text = translator(text)
    computation_time = time.time() - start
    return translated_text[0]['translation_text'], computation_time

languages = Languages()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_languages')
def get_languages():
    # Send a dictionary of language codes and their readable names to the frontend
    return jsonify({'languages': languages.list_languages()})


@app.route('/translate', methods=['POST'])
def translate_api():
    # Get the selected input and output languages (which are the keys/codes) directly from the form
    input_language_index = request.form['input_language']
    output_language_index = request.form['output_language']

    input_language_code = languages.list_keys()[int(input_language_index)]
    output_language_code = languages.list_keys()[int(output_language_index)]

    input_text = request.form['input_text']

    # Translate using the language codes
    translated_text, computation_time = translate(input_text, input_language_code, output_language_code, 400)

    return jsonify({'translated_text': translated_text, 'computation_time': round(computation_time,1)})


if __name__ == '__main__':
    app.run(debug=True)
