import speech_recognition as sr


class SpeechRecognizer:
    """Recognizes and transcribes speech from audio files."""

    def __init__(self, language: str = "es-AR"):
        self.recognizer = sr.Recognizer()
        self.language = language

    def transcribe(self, wav_path: str, show_all: bool = False):
        with sr.AudioFile(wav_path) as source:
            audio = self.recognizer.record(source)

        return self.recognizer.recognize_google(
            audio, language=self.language, show_all=show_all
        )
