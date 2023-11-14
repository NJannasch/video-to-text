# In advance install the following
# sudo apt update && sudo apt install ffmpeg
# pip3 install git+https://github.com/openai/whisper.git -q
# pip3 install pytube

import pytube
import whisper

# Configuration
video = "https://www.youtube.com/watch?v=xLMbTSax_PI&t=9s"
video_file="video.mp4"

# Converting and downloading as 'MP4' file
data = pytube.YouTube(video)
audio = data.streams.get_audio_only()
audio.download(output_path="", filename=video_file)

model = whisper.load_model("base")
text = model.transcribe(video_file)

# Printing the transcribe
print(text['text'])
