import os

import streamlit as st
from google import genai


st.set_page_config(page_title="Text summarizer", page_icon="✨")
st.title("✨ Text summarizer")
st.caption("Turn a long passage into a useful summary and key takeaways.")

api_key = os.getenv("GEMINI_API_KEY", "").strip()
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
fallback_model = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-3.6-flash")


def generate_with_fallback(client, prompt):
    models = list(dict.fromkeys([model, fallback_model]))
    for index, candidate in enumerate(models):
        try:
            return client.models.generate_content(model=candidate, contents=prompt)
        except Exception as exc:
            error = str(exc).upper()
            transient_overload = any(code in error for code in ("429", "500", "502", "503", "504", "UNAVAILABLE", "RESOURCE_EXHAUSTED"))
            if not transient_overload or index == len(models) - 1:
                raise
            st.info(f"{candidate} is temporarily unavailable. Trying {models[index + 1]}…")


def generation_error(exc):
    error = str(exc).upper()
    if any(code in error for code in ("503", "UNAVAILABLE", "500", "502", "504")):
        return "Gemini is temporarily busy on the available models. Please wait a moment and try again."
    if "429" in error or "RESOURCE_EXHAUSTED" in error:
        return "The Gemini request limit has been reached. Please try again later."
    return str(exc)


with st.form("summary_form"):
    source = st.text_area("Text to summarize", height=280, placeholder="Paste an article, chapter, or set of notes…")
    col1, col2 = st.columns(2)
    with col1:
        length = st.selectbox("Summary length", ["Short", "Standard", "Detailed"], index=1)
    with col2:
        focus = st.text_input("Optional focus", placeholder="Example: causes, dates, and outcomes")
    submitted = st.form_submit_button("Summarize", type="primary")

if submitted:
    st.session_state.pop("summary", None)
    if not source.strip():
        st.warning("Paste some text first.")
    elif not api_key:
        st.error("Gemini is not configured for this app. Please contact the app owner.")
    else:
        focus_instruction = f"Pay special attention to: {focus.strip()}." if focus.strip() else ""
        prompt = f"""Summarize the source text at a {length.lower()} level of detail. Start with a clear summary, then list 3–6 key takeaways as bullets. Preserve important names, numbers, and qualifications. Do not add facts that are not in the source. {focus_instruction}

<source_text>
{source}
</source_text>
"""
        try:
            with st.spinner("Summarizing…"):
                client = genai.Client(api_key=api_key)
                response = generate_with_fallback(client, prompt)
            st.session_state.summary = (response.text or "The model returned an empty response.").strip()
        except Exception as exc:
            st.error(f"Could not summarize the text: {generation_error(exc)}")

if st.session_state.get("summary"):
    st.subheader("Summary")
    st.markdown(st.session_state.summary)
    st.download_button(
        "Download summary as Markdown",
        data=st.session_state.summary,
        file_name="summary.md",
        mime="text/markdown",
    )
