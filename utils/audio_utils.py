from __future__ import annotations
from pydub import AudioSegment


def normalize_audio(
    filename: str,
    channels: int = 1,
    frame_rate: int = 16000,
) -> str:
    audio = AudioSegment.from_file(filename)
    audio = audio.set_channels(channels).set_frame_rate(frame_rate).normalize()
    audio.export(filename, format="wav")
    return filename
