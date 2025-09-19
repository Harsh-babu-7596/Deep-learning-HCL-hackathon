# Deep learning hackathon IITMandi  
# 🗣️ Indian Language Identifier + Translator  

A deep learning–powered web app that identifies the spoken Indian language from audio input and optionally translates text using Google's Gemini API.  
Built during the **HCLTech AI Innovation Challenge**.  

---

## 🚀 Overview
This project focuses on **automatic language identification (LID)** from speech audio for 10 major Indian languages. The system enables:  

- **Speech-based language classification** using MFCC features and a CNN-based deep learning model.  
- **Real-time web interface** with [Streamlit](https://streamlit.io/) for uploading `.wav` files and viewing predictions.  
- **Cross-lingual text translation** powered by Google **Gemini Pro API**.  

---

## 🧠 Supported Languages
| Class | Language  |
|-------|-----------|
| 0     | Hindi     |
| 1     | Tamil     |
| 2     | Telugu    |
| 3     | Bengali   |
| 4     | Marathi   |
| 5     | Kannada   |
| 6     | Gujarati  |
| 7     | Punjabi   |
| 8     | Malayalam |
| 9     | Urdu      |

---

## 📦 Tech Stack
- **Frontend**: Streamlit  
- **Backend**: Python (Keras, TensorFlow)  
- **Audio Processing**: `librosa`, `soundfile`  
- **AI Integration**: Google Gemini Pro API  
- **Model**: CNN trained on MFCCs (`lid_model.h5`)  

---

## 📁 Directory Structure
.
├── lid_model.h5 # Pretrained speech classification model
├── app.py # Streamlit web app
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/language-id-translator.git
cd language-id-translator
2️⃣ Create a Virtual Environment (optional)
bash
Copy code
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure Gemini API Key
Replace the placeholder in app.py:

python
Copy code
genai.configure(api_key="YOUR_GEMINI_API_KEY")
with your key from Google AI Studio.

5️⃣ Run the App
bash
Copy code
streamlit run app.py
📝 Features
🎤 Upload .wav audio files to detect language.

📊 Confidence score displayed with prediction.

🌍 Translate any input text into English via Gemini API.

💡 Lightweight, fast, and browser-based.

📈 Future Improvements
Expand support to more Indian languages and dialects.

Add noise-robust features (mel-spectrograms).

Optimize model with TensorFlow Lite for mobile/edge.

Integrate speech-to-text for full multilingual pipelines.

🏆 Hackathon Recognition
Developed as part of the HCLTech AI Innovation Challenge, demonstrating real-time multilingual speech intelligence for India’s diverse linguistic landscape.

🤝 Contributors
Harsh Vardhan – Developer, AI/ML Engineering

Google Gemini API – Generative AI translation

HCLTech Hackathon Team – Problem statement & mentorship

📜 License
This project is licensed under the MIT License – feel free to use, adapt, and improve!

