from engines.speech_synthesizer import SpeechSynthesizer
from engines.speech_recognizer import SpeechRecognizer
import sounddevice as sd
import wavio


class SpeechService:
    """
    High-level service that unifies speech synthesis (text → voice)
    and speech recognition (voice → text).
    """

    def __init__(
        self,
        synth_rate: int = 150,
        synth_volume: float = 0.9,
        synth_language: str = "es",
        recog_language: str = "es-AR",
    ):
        # Initialize underlying engines
        self.synthesizer = SpeechSynthesizer(
            rate=synth_rate, volume=synth_volume, language=synth_language
        )
        self.recognizer = SpeechRecognizer(language=recog_language)

    def speak(self, text: str):
        """Play text aloud."""
        return self.synthesizer.speak(text)

    def save(self, text: str, filename: str = "audios/audio.wav"):
        """Save text as spoken audio (WAV file)."""
        return self.synthesizer.save(text, filename)

    def text_to_speech(self, text: str, filename: str = "audio.wav"):
        """
        High-level alias for save().
        Provided for semantic clarity (e.g., when chaining text→speech→text).
        """
        return self.save(text, filename)

    def speech_to_text(self, wav_path: str, show_all: bool = False):
        """Convert a WAV file to text using Google Speech Recognition."""
        return self.recognizer.transcribe(wav_path, show_all=show_all)

    def grabar_audio(
        self, filename="audios/grabacion.wav", duration=5, frequency=16000
    ):
        """
        Graba audio desde el micrófono y lo guarda en formato WAV.

        Args:
            filename (str): nombre del archivo de salida.
            duracion (int): duración de la grabación en segundos.
            frequency (int): frecuencia de muestreo en Hz (16000 recomendado).
        """
        try:
            print(f"Grabando {duration} segundos...")
            audio = sd.rec(
                int(duration * frequency),
                samplerate=frequency,
                channels=1,
                dtype="int16",
            )
            sd.wait()
            wavio.write(filename, audio, frequency, sampwidth=2)
            print(f"✅ Audio guardado como: {filename}")
            return filename
        except Exception as e:
            print(f"❌ Error al grabar audio: {e}")
            return None
