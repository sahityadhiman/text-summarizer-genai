# Text Summarizer — Clear Summaries and Key Takeaways

> **Paste a long passage. Choose a level of detail. Keep the key points.**

Text Summarizer is a small generative AI app that turns a passage into a short, standard, or detailed summary followed by key takeaways. An optional focus tells Gemini which details matter most to the reader.

## 🚀 Live Demo

**Try the app:** [text-summarizer-genai.onrender.com](https://text-summarizer-genai.onrender.com)

## 📂 GitHub Repository

[github.com/sahityadhiman/text-summarizer-genai](https://github.com/sahityadhiman/text-summarizer-genai)

---

## 💡 Problem

Long articles, chapters, and notes can take a while to review. A useful summary needs to preserve important facts and qualifications without adding unsupported details.

### Core Question

**Can a reader get a concise, adjustable summary that stays grounded in the passage they provide?**

## 🎯 Our Solution

Paste text, choose a summary length, and optionally enter a focus such as causes, dates, or outcomes. Gemini is prompted to summarize the source, preserve important names and numbers, avoid adding facts, and list the main takeaways.

## 🔄 Summarization Workflow

1. Paste an article, chapter section, or set of notes.
2. Choose Short, Standard, or Detailed.
3. Optionally specify a focus for the summary.
4. Generate a summary followed by 3–6 key takeaways.
5. Download the result as a Markdown file.

## ✨ Key Features

### 📏 Adjustable Detail
Choose a short, standard, or detailed result.

### 🎯 Optional Focus
Ask the summary to pay special attention to a topic, dates, causes, outcomes, or another useful angle.

### 🔑 Key Takeaways
The response is prompted to include 3–6 concise takeaways after the summary.

### 📌 Source-Grounded Prompt
Gemini is asked to preserve names, numbers, and qualifications and not add facts that are missing from the source.

### ⬇️ Downloadable Result
Download the summary and takeaways as `summary.md`.

### 🔐 Bring Your Own Gemini Key
Enter a Gemini API key in the sidebar, or configure a server key for a private deployment. The public demo currently asks each visitor for their own key.

## 🧪 Current Prototype

The deployed prototype demonstrates text-only summarization in a single Streamlit page. Results are available in the current session and can be downloaded as Markdown. The app does not save summaries to a database or accept file uploads.

## 🛠️ Technology Stack

- **Python** — application logic
- **Streamlit** — interactive web interface
- **Google Gemini** — summarization and takeaways
- **google-genai** — Gemini Python SDK
- **Render** — public web hosting

## 🏗️ Architecture

~~~~text
Reader
  │
  ├── Source text
  ├── Summary length
  └── Optional focus
          │
          ▼
Streamlit app (app.py)
          │
          ▼
Google GenAI SDK
          │
          ▼
Gemini model
          │
          ▼
Summary + key takeaways
          │
          ▼
Markdown preview and download
~~~~

## 🚀 Run Locally

### Requirements

- Python 3.10 or later
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Windows PowerShell

~~~~powershell
git clone https://github.com/sahityadhiman/text-summarizer-genai.git
cd text-summarizer-genai
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
$env:GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
streamlit run app.py
~~~~

### macOS or Linux

~~~~bash
git clone https://github.com/sahityadhiman/text-summarizer-genai.git
cd text-summarizer-genai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
streamlit run app.py
~~~~

You can also paste your key into the app’s password field in the sidebar instead of setting an environment variable. Never commit a real API key to GitHub.

## ⚙️ Configuration

| Variable | Required | Default | Purpose |
|---|---:|---|---|
| `GEMINI_API_KEY` | No, if entered in the sidebar | — | Gemini API key used by the app. A server-configured key is shared by all visitors. |
| `GEMINI_MODEL` | No | `gemini-3.8-flash` | Gemini model name passed to the SDK. |

## ☁️ Deploy on Render

This repository includes a Render Blueprint in `render.yaml`. Create a Blueprint in Render and connect this GitHub repository; Render reads the Blueprint to install the pinned dependencies and start Streamlit.

The public demo is deployed on Render’s free web service. Free services can sleep while idle, so the first visit after inactivity may take about a minute to load. The demo does not have a shared Gemini key configured; visitors enter their own key in the sidebar.

## 🔒 Privacy and Limitations

- The source text and optional focus are sent to Google Gemini when a summary is generated.
- A key entered in the public app is sent to the app server for the Gemini request. Use a key only with a deployment you trust.
- Gemini can omit details or produce incorrect summaries even when asked to stay within the source. Check important facts against the original passage.
- Do not paste confidential, personal, or sensitive information into the public demo.
- This is a lightweight text prototype; it has no file upload, user accounts, or persistent history.
