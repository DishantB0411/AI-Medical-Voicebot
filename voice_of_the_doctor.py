import os
import subprocess
import platform
from gtts import gTTS
from dotenv import load_dotenv
from pydub import AudioSegment
import elevenlabs
from elevenlabs.client import ElevenLabs
load_dotenv()
ELABS_API_KEY = os.getenv('ELABS_API_KEY')

#Step1a : Setup Text to Speech-TTS-model (gTTs)
def text_to_speech_with_text_old(input_text, output_filepath):
    language = 'en'

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath)

#Step1b : Setup Text to Speech-TTS-model(Elevenlabs)
def text_to_speech_elevenlabs_old(input_text, output_filepath ):
    client = ElevenLabs(api_key = ELABS_API_KEY)
    audio = client.generate(
        text = input_text,
        voice = '2EiwWnXFnvU5JabPnv8n',
        output_format = 'mp3_22050_32',
        model = 'eleven_turbo_v2'
    )
    elevenlabs.save(audio, output_filepath )

#Step2 : Use Model for Text output to Voice

def text_to_speech_with_gtts(input_text, output_filepath):
    language = 'en'

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath)
    audio = AudioSegment.from_mp3(output_filepath)
    audio.export("formatted.wav", format="wav")
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "formatted.wav").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_elevenlabs(input_text, output_filepath ):
    client = ElevenLabs(api_key = ELABS_API_KEY)
    audio = client.generate(
        text = input_text,
        voice = '2EiwWnXFnvU5JabPnv8n',
        output_format = 'mp3_22050_32',
        model = 'eleven_turbo_v2'
    )
    elevenlabs.save(audio, output_filepath )
    audio = AudioSegment.from_mp3(output_filepath)
    audio.export("formatted.wav", format="wav")
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "formatted.wav").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")