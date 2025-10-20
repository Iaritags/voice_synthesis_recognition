import pyttsx3
import platform


class SpeechSynthesizer:
    """Synthesizes human speech from text using pyttsx3."""

    def __init__(self, rate: int = 150, volume: float = 0.9, language: str = "es"):
        self.engine = self._init_engine()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", max(0.0, min(volume, 1.0)))
        self._set_voice(language)

    def _init_engine(self):
        system = platform.system().lower()
        driver = (
            "sapi5"
            if "windows" in system
            else "nsss" if "darwin" in system else "espeak"
        )
        return pyttsx3.init(driver)

    def _set_voice(self, language: str):
        for v in self.engine.getProperty("voices") or []:
            name = (v.name or "").lower()
            if language in v.id.lower() or "spanish" in name or "español" in name:
                self.engine.setProperty("voice", v.id)
                break

    def speak(self, text: str):
        if not text.strip():
            raise ValueError("Text cannot be empty.")

        self.engine.say(text)
        self.engine.runAndWait()

    def save(self, text: str, filename: str = "speech.wav"):
        if not text.strip():
            raise ValueError("Text cannot be empty.")

        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        return filename
