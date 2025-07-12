from gtts import gTTS
import os

# Thư mục lưu âm thanh
output_folder = "audio_mp3"
os.makedirs(output_folder, exist_ok=True)

# Danh sách số từ 0 đến 9
numbers = {
    "number_0.mp3": "không",
    "number_1.mp3": "một",
    "number_2.mp3": "hai",
    "number_3.mp3": "ba",
    "number_4.mp3": "bốn",
    "number_5.mp3": "năm",
    "number_6.mp3": "sáu",
    "number_7.mp3": "bảy",
    "number_8.mp3": "tám",
    "number_9.mp3": "chín",
}

# Cụm từ cố định
fixed_phrases = {
    "prefix_number.mp3": "Số",
    "please_to_counter.mp3": "Vui lòng đến",
    "invite_customer.mp3": "Xin mời khách hàng"
}

# Quầy từ 1 đến 12
counters = {
    f"counter_{i}.mp3": f"Quầy số {i}" for i in range(1, 13)
}

# Gộp tất cả
text_audio_map = {**numbers, **fixed_phrases, **counters}

# Tạo từng file mp3
def create_mp3(filename, text):
    path = os.path.join(output_folder, filename)
    if os.path.exists(path):
        print(f"✅ Đã có: {filename}, bỏ qua")
        return
    print(f"🎤 Tạo: {filename} → \"{text}\"")
    tts = gTTS(text=text, lang='vi')
    tts.save(path)

# Chạy
for filename, text in text_audio_map.items():
    create_mp3(filename, text)

print("\n🎉 Hoàn tất! Đã tạo tất cả file trong thư mục:", output_folder)
