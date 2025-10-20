from services.speech_service import SpeechService
from utils.audio_utils import normalize_audio


def main():
    speech_service = SpeechService(synth_language="es", recog_language="es-AR")

    text = input("Escribí el texto para convertir a voz: ").strip()

    if not text:
        return print("No ingresaste texto")

    # Speak
    speech_service.speak(text)

    # Save text -> audio
    speech_service.save(text)

    option = input("\n¿Deseás grabar audio para transcribirlo? (s/n): ").strip().lower()

    if option != "s":
        return print("Omitiendo grabación y transcripción.")

    # Record audio
    audio_captured = speech_service.grabar_audio()

    # Normalize audio for better recognition
    normalized_audio = normalize_audio(audio_captured)

    # Audio -> Text
    text = speech_service.speech_to_text(normalized_audio, show_all=False)
    print("Transcripción:", text)


if __name__ == "__main__":
    main()
