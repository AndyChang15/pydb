# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:02:03 2023

@author: User
"""

from pytube import YouTube
from pydub import AudioSegment
import openai

# 設定要下載的影片 URL
url = "https://www.youtube.com/watch?v=IvOdTbIYZs4"

# 建立 YouTube 物件
yt = YouTube(url)

# 取得影片的音軌
audio_stream = yt.streams.filter(only_audio=True).first()

# 下載音軌到指定的路徑
#audio_stream.download(output_path="D:\web_py\path", filename="audio")
audio_stream.download(output_path=r"D:\web_py\path", filename="audio")

# 讀取下載下來的音檔
#audio_file = AudioSegment.from_file("D:\web_py\path")

#audio_file = AudioSegment.from_file("D:\web_py\path\audio")
audio_file = AudioSegment.from_file(r"D:\web_py\path\audio")


# 切割音檔成多個小檔案
chunk_size = 100 * 1000  # 100 秒
chunks = [audio_file[i:i+chunk_size] for i in range(0, len(audio_file), chunk_size)]

# 使用 OpenAI 的 Audio API 將每個小檔案轉成文字，然後合併在一起
openai.api_key = "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"
transcript = ""
for chunk in chunks:
    with chunk.export("temp.wav", format="wav") as f:
        result = openai.Audio.transcribe("whisper-1", f)
        transcript += result["text"]

# 印出轉換後的文字
print(transcript)