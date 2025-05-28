import streamlit as st
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("🧠 AI Resume Analyzer")
st.markdown("Upload your resume as a `.txt` file and let GPT give you instant feedback!")

uploaded_file = st.file_uploader("Choose a resume file (.txt only)", type="txt")

if uploaded_file is not None:
    resume_text = uploaded_file.read().decode("utf-8")

    with st.spinner("Analyzing resume with GPT..."):
        prompt = (
            "You are a career coach and resume expert. Read the following resume and provide:\n"
            "1. A summary of the candidate's strengths\n"
            "2. Suggestions for improvement\n"
            "3. A 1-sentence professional summary.\n\n"
            f"Resume:\n{resume_text}"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful resume reviewer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )

            feedback = response['choices'][0]['message']['content']
            st.success("✅ Analysis Complete!")
            st.markdown("---")
            st.markdown(feedback)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
