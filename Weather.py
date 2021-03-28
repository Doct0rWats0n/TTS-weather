from gtts import gTTS
import requests

API = ''

responce = requests.get('http://api.openweathermap.org/data/2.5/weather?' +
                        'q=London&units=metric&appid={}'.format(API))
weather = responce.json()

tts = gTTS(f"Погода: \n{weather['main']['temp']} градусов по цельсию\n" +
           f"Ветер {weather['wind']['speed']} метров в секунду", lang='ru')
tts.save('weather.mp3')
