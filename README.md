# Language Translator Application

This project is a Flask-based web application that translates text from one language to another using a pre-trained machine translation model (NLLB-200). The application provides a user-friendly interface for selecting languages and entering text, and it returns the translated output along with the computation time.

## Overview

The application allows users to translate text by:
1. Selecting the input language. (150+ language support)
2. Selecting the target output language. (150+ language support)
3. Entering the text they wish to translate.
4. Submitting the request to view the translated text and computation time.

## Features

- **Translation Pipeline**: The app leverages the NLLB-200 (No Language Left Behind) model for accurate translation across 200 languages. This model, developed by Meta, is specifically optimized for low-resource languages, making it ideal for global use.
- **Language Selection**: The app dynamically fetches supported languages from the backend, allowing users to select from the available options.
- **Spinner for Loading Indicator**: To improve user experience, a spinner appears when the translation process is ongoing, and it disappears once the translation is complete.
- **Computation Time**: After translation, the time taken to perform the translation is displayed.

## Technology Stack

- **Flask**: Used as the backend framework to handle HTTP requests, render templates, and communicate with the translation model.
- **HTML, CSS, and JavaScript**: The frontend is built with HTML and CSS for styling and JavaScript (AJAX) for handling asynchronous requests.
- **Hugging Face Transformers**: The NLLB-200 model is loaded via the Hugging Face Transformers library, using a pre-trained model for multi-lingual text translation. Visit [HF model link](https://huggingface.co/facebook/nllb-200-distilled-600M) for downloading the model
- **CUDA Support**: If available, the application utilizes GPU processing via CUDA to speed up the translation process.

## Model: NLLB-200

[The NLLB-200 model](https://huggingface.co/facebook/nllb-200-distilled-600M), "No Language Left Behind," is a state-of-the-art machine translation model developed by Meta, supporting translations across 200 languages, especially for low-resource languages. By using a sequence-to-sequence model architecture, NLLB-200 achieves high translation quality by leveraging a massive multilingual dataset and advanced training techniques.

This model provides:
- High accuracy across multiple language pairs.
- Low latency, making it well-suited for applications requiring quick responses.
- Language codes for each supported language, allowing flexible input and output language options.

## File Structure

- `flask_app.py`: Main application file handling routing, translation processing, and language list retrieval.
- `app.py`: it is the api code for deployment purpose
- `templates/index.html`: Frontend layout for user interaction with the translation app.
- `static/style.css`: Custom CSS for styling the frontend interface.
- `nllb_supported_languages.py`: Contains language data, used for language selection in the frontend.

## Setup Instructions

1. **Install Python Packages**: Make sure to install *Flask*, *Transformers*, and *Torch* (for GPU support if available).
   ```shell
   pip install flask transformers torch

2. Download and Save Model: Download the NLLB-200 model and save it in your desired directory. This application is set to load the model locally from
    `D:/Language Translator/model` you can save it anywhere you want just pass the path in the `*pretrained_model_name_or_path*` parameter.

3. Run the Application:
    ```shell
    python flask_app.py


For any queries you can contact me through my mail id [mail](aryachakraborty.official@gmail.com) or text me in linkedin [LinkedIn](https://www.linkedin.com/in/arya-chakraborty2002/)