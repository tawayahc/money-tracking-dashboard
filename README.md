# Money Tracking Dashboard

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://www.google.com/search?sca_esv=a07f0383584960a3&sxsrf=ADLYWIIfCuD6zjm-S-u-nWBQ3X7HLFXxBw:1731342911979&q=cat&udm=2&fbs=AEQNm0Btv3wNZ-5CTPTYXsjMy8VlYYTy-4rIkNOiAyyjVgQVbmeV5xRi440Us6JzhiZ_fXlfUPz0AQN6hPpdnL7mrLEXFwEa6UI1tU54K9J-HYW73ZegA4ReDmek5-qRcnvORq5YNlOS-lm9Nt3MUWphuFc-jZ-vAhOlG-mhpXZbIOnY5s4wMSgQquZe6l8XgLXlV2XRUwb2ELx7WWRkxZUXVATMOdokT4JL23LH766XclrCeUyFehR1Obt-ieBsBhQdCGasAyzwe8bugxX7IEh0BnLc484X7PlGEe1RbQLq42u_9Ors8lQ&sa=X&ved=2ahUKEwjw24L62tSJAxX83TgGHVOnGXkQtKgLegQIGRAB&biw=2338&bih=1420&dpr=1)

This repository contains a Streamlit-based web application designed to perform various tasks including category management, dashboard visualization, Thai text analysis, and a virtual assistant feature.

## Directory Structure

```plaintext
.
├── category
│   ├── category_management.py              # Manage categories
│   ├── styles.py                           # Styling for the category page
├── dashboard
│   ├── bar_chart.py                        # Bar chart generation
│   ├── line_chart.py                       # Line chart generation
│   ├── pie_chart.py                        # Pie chart generation
├── models
│   ├── fine_tuned_model.bin                # Pre-trained model file
│   ├── model_loader.py                     # Model loading utility
├── notebooks
│   ├── datasets/
│   │   ├── th-simlex-999-details.xlsx
│   │   ├── th-wordsim-353-details.xlsx
│   │   ├── thai_texts.csv
│   ├── building_word_embedding_model.ipynb # word embeddings building notebook
│   ├── web_crawling.ipynb                  # Web crawling notebook
│   ├── web_scraping.ipynb                  # Web scraping notebook
├── sidebar
│   ├── sidebar.py                          # Sidebar components for the Streamlit app
├── utils
│   ├── info_extractor.py                   # Extract information from datasets
│   ├── ocr_extractor.py                    # OCR extraction utility
│   ├── session_state.py                    # Manage Streamlit session states
├── virtual_assistant
│   ├── chatgpt_integration.py              # ChatGPT integration for virtual assistant
│   ├── chatgpt_ui.py                       # Virtual assistant UI
├── app.py                                  # Main entry point for the Streamlit app
├── categories.json                         # JSON data for categories
├── transactions.json                       # JSON data for transactions
├── requirements.txt                        # Python dependencies
├── README.md                               # Project documentation
```

## How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run app.py
   ```
