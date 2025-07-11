import requests
import wave
import io

# ✅ 10 câu tiếng Anh có nghĩa, có nhiều từ dài (3–4 âm tiết)
sentences = [
    "The conversation between the manager and the employee revealed important organizational decisions for next month.",
    "Educational institutions must continuously adapt their curriculum to meet the demands of modern technological developments.",
    "She presented a compelling argument supported by detailed research and statistical information from multiple sources.",
    "Despite the complexity of the operation, the surgeon performed each step with precision and confidence.",
    "The documentary highlighted environmental degradation and urged international cooperation to address climate change.",
    "He emphasized the significance of communication in building trust and maintaining healthy professional relationships.",
    "The unexpected cancellation of the conference disappointed participants who had traveled from various global destinations.",
    "Implementing automation in manufacturing significantly improved efficiency while reducing human error and labor costs.",
    "After evaluating several alternatives, the committee selected the most sustainable and economically feasible solution.",
    "Although the presentation contained technical terminology, the speaker maintained clarity and engaged the audience effectively."
]

# 🎯 Đếm số từ thủ công
def count_words(sentence):
    words = sentence.strip().replace(".", "").replace(",", "").replace("?", "").replace("!", "")
    return len(words.split())

# 📏 Tính thời lượng WAV từ bytes
def get_wav_duration(wav_bytes):
    with wave.open(io.BytesIO(wav_bytes), 'rb') as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        duration = frames / float(rate)
        return duration

# 📡 Gửi request đến API TTS
def call_tts(text, api_key):
    url = "https://api.typecast.ai/v1/text-to-speech"
    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": api_key
    }
    payload = {
        "voice_id": "tc_62a8975e695ad26f7fb514d1",
        "text": text,
        "model": "ssfm-v21",
        "language": "eng",
        "prompt": {
            "emotion_preset": "normal",
            "emotion_intensity": 1
        },
        "output": {
            "volume": 100,
            "audio_pitch": 0,
            "audio_tempo": 1,
            "audio_format": "wav"
        },
        "seed": 42
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        print(f"❌ API error: {response.status_code} - {response.text}")
        return None

# 🧮 Tính tốc độ nói
def measure_speech_rate(sentence, api_key):
    num_words = count_words(sentence)
    print(f"\n🗣️ Sentence: {sentence}")
    print(f"🔢 Word count: {num_words}")
    
    audio = call_tts(sentence, api_key)
    if audio:
        duration = get_wav_duration(audio)
        print(f"⏱️ Duration: {duration:.2f} seconds")
        rate = num_words / duration
        print(f"⚡ Speech rate: {rate:.2f} words/second")
        return rate
    else:
        print("⚠️ Failed to get audio.")
        return None

# 🚀 Chạy đo cho tất cả câu
if __name__ == "__main__":
    your_api_key = "__pltJ25TCA4rDjXvRBg4u8tHQtAwoFXsJrkQB73YqR8U"  # 🔁 Nhập API key thật tại đây
    rates = []

    for i, sentence in enumerate(sentences):
        print(f"\n--- Test #{i+1} ---")
        rate = measure_speech_rate(sentence, your_api_key)
        if rate:
            rates.append(rate)

    if rates:
        avg = sum(rates) / len(rates)
        print(f"\n✅ Average speech rate: {avg:.2f} words/second")


# Example output 1:
# Duration: 3.90s for 11 words
# Speech Rate: 2.82 words/sec
# --- Test #1 ---

# 🗣️ Sentence: The conversation between the manager and the employee revealed important organizationa l decisions for next month.
# 🔢 Word count: 15
# ⏱️ Duration: 6.55 seconds
# ⚡ Speech rate: 2.29 words/second

# --- Test #2 ---

# 🗣️ Sentence: Educational institutions must continuously adapt their curriculum to meet the demands  of modern technological developments.        
# 🔢 Word count: 15
# ⏱️ Duration: 7.35 seconds
# ⚡ Speech rate: 2.04 words/second

# --- Test #3 ---

# 🗣️ Sentence: She presented a compelling argument supported by detailed research and statistical inf ormation from multiple sources.
# 🔢 Word count: 15
# ⏱️ Duration: 7.35 seconds
# ⚡ Speech rate: 2.04 words/second

# --- Test #4 ---

# 🗣️ Sentence: Despite the complexity of the operation, the surgeon performed each step with precisio n and confidence.
# 🔢 Word count: 15
# ⏱️ Duration: 6.10 seconds
# ⚡ Speech rate: 2.46 words/second

# --- Test #5 ---

# 🗣️ Sentence: The documentary highlighted environmental degradation and urged international cooperat ion to address climate change.
# 🔢 Word count: 13
# ⏱️ Duration: 7.10 seconds
# ⚡ Speech rate: 1.83 words/second

# --- Test #6 ---

# 🗣️ Sentence: He emphasized the significance of communication in building trust and maintaining heal thy professional relationships.
# 🔢 Word count: 14
# ⏱️ Duration: 7.30 seconds
# ⚡ Speech rate: 1.92 words/second

# --- Test #7 ---

# 🗣️ Sentence: The unexpected cancellation of the conference disappointed participants who had travel ed from various global destinations.
# 🔢 Word count: 15
# ⏱️ Duration: 7.35 seconds
# ⚡ Speech rate: 2.04 words/second

# --- Test #8 ---

# 🗣️ Sentence: Implementing automation in manufacturing significantly improved efficiency while reduc ing human error and labor costs.
# 🔢 Word count: 14
# ⏱️ Duration: 7.70 seconds
# ⚡ Speech rate: 1.82 words/second

# --- Test #9 ---

# 🗣️ Sentence: After evaluating several alternatives, the committee selected the most sustainable and  economically feasible solution.
# 🔢 Word count: 14
# ⏱️ Duration: 7.20 seconds
# ⚡ Speech rate: 1.94 words/second

# --- Test #10 ---

# 🗣️ Sentence: Although the presentation contained technical terminology, the speaker maintained clar ity and engaged the audience effectively.    
# 🔢 Word count: 15
# ⏱️ Duration: 7.30 seconds
# ⚡ Speech rate: 2.05 words/second

# ✅ Average speech rate: 2.04 words/second