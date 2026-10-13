# Text Summarizer

A small GenAI app that converts a long passage into a short, standard, or detailed summary with key takeaways.

## Run locally

You need Python 3.10 or later and a Gemini API key. Create a key in [Google AI Studio](https://aistudio.google.com/app/apikey).

Open PowerShell in this folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Paste your API key into the app's sidebar. You can also set `GEMINI_API_KEY` in PowerShell before launching. Never commit an API key to GitHub.

## How it works

The app sends the provided text, requested detail level, and optional focus to Gemini. Its prompt requests a source-grounded summary and a list of key takeaways. The result can be downloaded as Markdown.

To use a different Gemini model, set `GEMINI_MODEL` in the shell before launching. The default is `gemini-3.8-flash`.

## Deploy on Render

This repository includes a Render Blueprint. In Render, create a new Blueprint and connect this GitHub repository; Render will build and launch the app using the settings in `render.yaml`. The free web service can sleep after inactivity, so its first request may take about a minute to load.

The public app asks visitors to enter their own Gemini API key. If you configure `GEMINI_API_KEY` in Render instead, all visitors share that key's quota. Keep the key in Render's environment settings, never in this repository.

**Privacy:** Source text is sent to Google's Gemini API when you generate a summary. Avoid private or sensitive text.
