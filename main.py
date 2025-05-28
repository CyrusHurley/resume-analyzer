import openai
from config import OPENAI_API_KEY

def load_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def analyze_resume(resume_text):
    openai.api_key = OPENAI_API_KEY

    prompt = (
        "You are a career coach and resume expert. Read the following resume and provide:\n"
        "1. A summary of the candidate's strengths\n"
        "2. Suggestions for improvement\n"
        "3. A 1-sentence professional summary.\n\n"
        f"Resume:\n{resume_text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful resume reviewer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )

    return response['choices'][0]['message']['content']

def main():
    resume_text = load_resume("sample_resume.txt")
    analysis = analyze_resume(resume_text)
    print("\n=== Resume Analysis ===\n")
    print(analysis)

if __name__ == "__main__":
    main()
