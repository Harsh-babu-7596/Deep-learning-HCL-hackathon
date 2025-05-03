import streamlit as st
import numpy as np
import librosa
import soundfile as sf
import google.generativeai as genai
import tensorflow as tf  # or use tflite_runtime.interpreter

# Load model
model = tf.keras.models.load_model("lid_model.h5")

# Load Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def get_features(audio_path):
    y, sr = librosa.load(audio_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.expand_dims(mfcc, axis=(0, -1))  # (1, time, n_mfcc, 1)

def predict_language(audio_path):
    features = get_features(audio_path)
    pred = model.predict(features)
    class_id = np.argmax(pred)
    return class_id, pred[0][class_id]

def translate_with_gemini(text, target_lang):
    prompt = f"Translate this sentence to {target_lang}:\n{text}"
    response = genai.GenerativeModel("gemini-pro").generate_content(prompt)
    return response.text.strip()

# Streamlit UI
st.title("🗣️ Indian Language Identifier + Translator")

uploaded_file = st.file_uploader("Upload an audio file (.wav)", type=["wav"])
if uploaded_file:
    st.audio(uploaded_file)

    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    class_id, conf = predict_language("temp.wav")
    language = {0: "Hindi",
    1: "Tamil",
    2: "Telugu",
    3: "Bengali",
    4: "Marathi",
    5: "Kannada",
    6: "Gujarati",
    7: "Punjabi",
    8: "Malayalam",
    9: "Urdu"
    }[class_id]
    

    st.success(f"Detected Language: **{language}** (Confidence: {conf:.2f})")

    input_text = st.text_input("Enter text to translate:")
    if input_text:
        translated = translate_with_gemini(input_text, "English")
        st.write("**Translation:**", translated)
