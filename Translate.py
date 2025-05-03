import os, google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def translate_with_gemini(text, target_lang):
    prompt = f"Translate this sentence to {target_lang}:\n{text}"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    return response.text.strip()
