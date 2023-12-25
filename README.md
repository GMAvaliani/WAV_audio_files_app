приложение на Python для работы с аудиофайлами формата WAV

2 функции:
Функция 1:  принимает аудиофайл и позволяет изменять скорость и громкость аудиофайла
Функция 2: Расшифровка аудио (английский и русский языки) в текст (работает без доступа в интернет) логируется в JSON-формате и записываться в файл.

используемые модели:
https://alphacephei.com/vosk/models

1) vosk-model-small-en-us-0.15
2) vosk-model-small-ru-0.22


для проверки работы ввести в терминале: 

для английского языка
"python wav_app.py pub_in_london.wav 1.5 10 en"


и
для русского языка
"python wav_app.py russian.wav 3.5 20 ru" 



