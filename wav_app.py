### приложение на Python для работы с аудиофайлами формата WAV

""" Функция 1: Модификация аудиофайла
Эта функция принимает аудиофайл и позволяет изменять скорость и громкость аудиофайла

Функция 2: Расшифровка аудио в текст
Данная функция использует open-source библиотеки для офлайн распознавания речи (работает без доступа в интернет) и преобразования аудиофайла в текстовый формат

Дополнительные требования:
Результат расшифровки должен логироваться в JSON-формате и записываться в файл."""


# решение имеет линейную временную и пространственную сложность O(n) относительно размера входных данных

from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import wave
import json
import sys

def modify_audio(file_path, speed_factor=1.0, volume_change=0.0):
    audio = AudioSegment.from_wav(file_path)
    audio = audio.speedup(playback_speed=speed_factor)
    audio += volume_change
    modified_path = "modified_" + file_path
    audio.export(modified_path, format="wav")
    return modified_path

def transcribe_audio(file_path, model_choice):
    model_path = 'vosk-model-small-en-us-0.15' if model_choice == 'en' else 'vosk-model-small-ru-0.22'
    model = Model(model_path)
    wf = wave.open(file_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))

    results.append(json.loads(rec.FinalResult()))
    return results

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python wav_app.py <audio_file> <speed_factor> <volume_change> <model_choice>")
        sys.exit(1)

    file_path = sys.argv[1]
    speed_factor = float(sys.argv[2])
    volume_change = float(sys.argv[3])
    model_choice = sys.argv[4]  # 'en' или 'ru'

    # Обработка аудио
    modified_path = modify_audio(file_path, speed_factor, volume_change)

    # Расшифровка аудио
    transcription = transcribe_audio(modified_path, model_choice)

    with open('transcription.json', 'w', encoding='utf-8') as f:
        json.dump(transcription, f, ensure_ascii=False, indent=4)




