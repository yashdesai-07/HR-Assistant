import streamlit as st
from resume_utils import extract_text_from_pdf, extract_text_from_docx
from prompts import screening_prompt, sentiment_prompt
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("HR Hiring Assistant")

tab1, tab2 = st.tabs(["📄 Resume Screening", "🗣️ Sentiment Analysis"])

with tab1:
    uploaded_file = st.file_uploader("Upload Resume (.pdf/.docx)", type=["pdf", "docx"])
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        else:
            resume_text = extract_text_from_docx(uploaded_file)
        
        prompt = screening_prompt(resume_text)
        st.write("⏳ Screening in progress...")
        response = model.generate_content(prompt)
        st.success("✅ Result:")
        st.markdown(response.text)

with tab2:
    feedback_text = st.text_area("Paste Employee Feedback")
    if st.button("Analyze Feedback") and feedback_text.strip():
        prompt = sentiment_prompt(feedback_text)
        response = model.generate_content(prompt)
        st.success("✅ Sentiment Analysis:")
        st.markdown(response.text)
