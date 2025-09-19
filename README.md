# Deep learning hackathon IITMandi  
A deep learning–based web app that identifies the spoken Indian language from audio input and optionally translates text using Google's Gemini API.

## 🚀 Overview
This project was built for the **HCLTech AI Innovation Challenge**, focusing on automatic language identification (LID) from speech audio for 10 major Indian languages. The system performs:

- **Spoken language classification** using MFCC features and a trained deep learning model
- **Real-time web interface** for users to upload `.wav` files and receive predictions
- **Cross-lingual text translation** via the **Gemini Pro API** for multilingual applications

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

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python (Keras, TensorFlow)
- **Audio Processing**: `librosa`, `soundfile`
- **AI Integration**: Google Gemini Pro (Generative AI)
- **Model**: CNN-based architecture trained on MFCCs (`lid_model.h5`)

---
