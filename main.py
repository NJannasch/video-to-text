# In advance install the following
# sudo apt update && sudo apt install ffmpeg
# pip3 install git+https://github.com/openai/whisper.git -q
# pip3 install pytube

import pytube
import whisper
import argparse

def main():
    parser = argparse.ArgumentParser(description='Download and transcribe audio from a YouTube video')
    parser.add_argument('--link', required=True, help='YouTube video link')
    args = parser.parse_args()

    # Configuration
    video = args.link
    video_file = "video.mp4"

    # Converting and downloading as 'MP4' file
    data = pytube.YouTube(video)
    audio = data.streams.get_audio_only()
    audio.download(output_path="", filename=video_file)

    model = whisper.load_model("base")
    text = model.transcribe(video_file)

    # Printing the transcription
    print("_______________________")
    print("____ Video Content ____")
    print("_______________________")
    print(text['text'])

if __name__ == "__main__":
    main()
