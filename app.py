import os

import streamlit as st
from google import genai


st.set_page_config(page_title="Text summarizer", page_icon="✨")
st.title("✨ Text summarizer")
st.caption("Turn a long passage into a useful summary and key takeaways.")

server_api_key = os.getenv("GEMINI_API_KEY", "")
user_api_key = st.sidebar.text_input(
    "Gemini API key",
    value="",
    type="password",
    help="Enter your own key if the app owner has not configured one. It is not saved to the project files.",
)
api_key = user_api_key or server_api_key
if server_api_key:
    st.sidebar.caption("A server-managed key is configured. Requests share its quota.")
model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
st.sidebar.caption(f"Model: {model}")

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
        st.error("Enter a Gemini API key in the sidebar first.")
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
                response = client.models.generate_content(model=model, contents=prompt)
            st.session_state.summary = (response.text or "The model returned an empty response.").strip()
        except Exception as exc:
            st.error(f"Could not summarize the text: {exc}")

if st.session_state.get("summary"):
    st.subheader("Summary")
    st.markdown(st.session_state.summary)
    st.download_button(
        "Download summary as Markdown",
        data=st.session_state.summary,
        file_name="summary.md",
        mime="text/markdown",
    )
