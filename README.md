# yaweather

Данный скрипт через API собирает данные на сервисе яндекс погоды на ближайшие 7 дней(отсчет от даты запроса), складывает их в excel в определенном формате и скачивает его.

Для работы скрипта требуются следующие библиотеки:

*import [pandas](https://pandas.pydata.org/docs/)*

*from [yaweather](https://pypi.org/project/yaweather/) import Russia, YaWeather*

*import [sqlite3](https://docs.python.org/3/library/sqlite3.html)*

*import [datetime](https://docs.python.org/3/library/datetime.html)*

## Формат предоставления данных в excel:

![image](https://user-images.githubusercontent.com/111370737/193848817-e78875ad-96b5-4b36-b651-1e79144d87de.png)

* date - дата, на которую сделан прогноз погоды
* time_of_day - время суток. Возможные значения: morning - утро, day - день, evening - вечер, night - ночь.
* temp_min - минимальная температура time_of_day.
* temp_max - максимальная температура time_of_day.
* average_daylight_temperature - средняя температура за световой день.
* condition - состояние погоды. Возможные значения:


clear — ясно.

partly-cloudy — малооблачно.
cloudy — облачно с прояснениями.
overcast — пасмурно.
drizzle — морось.
light-rain — небольшой дождь.
rain — дождь.
moderate-rain — умеренно сильный дождь.
heavy-rain — сильный дождь.
continuous-heavy-rain — длительный сильный дождь.
showers — ливень.
wet-snow — дождь со снегом.
light-snow — небольшой снег.
snow — снег.
snow-showers — снегопад.
hail — град.
thunderstorm — гроза.
thunderstorm-with-rain — дождь с грозой.
thunderstorm-with-hail — гроза с градом.
*
*
*
*
*
*
*
*
