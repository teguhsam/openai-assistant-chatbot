from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from config import openai

TALKER_MODEL = "tts-1"
VOICE = "onyx"

def talker(message):
    response = openai.audio.speech.create(
        model=TALKER_MODEL,
        voice=VOICE,
        input=message
    )
    audio_stream = BytesIO(response.content)
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    play(audio)
