import numpy as np
import librosa
import tensorflow as tf

class_map = {
    0: "Hindi", 1: "Tamil", 2: "Telugu", 3: "Bengali", 4: "Marathi",
    5: "Kannada", 6: "Gujarati", 7: "Punjabi", 8: "Malayalam", 9: "Urdu"
}

def get_features(audio_path):
    y, sr = librosa.load(audio_path, sr=16000)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.expand_dims(mfcc, axis=(0, -1))  # (1, time, mfcc, 1)

def predict_language(model, audio_path):
    features = get_features(audio_path)
    preds = model.predict(features)
    class_id = np.argmax(preds)
    return class_id, preds[0][class_id]
