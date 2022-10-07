# yaweather

Данный скрипт через API собирает данные на сервисе яндекс погоды на ближайшие 7 дней(отсчет от даты запроса), складывает их в excel в определенном формате и скачивает его. А также складывает сведения о входных параметрах, дате/времени запроса и результатах работы (успешно или ошибка) в sqlite. Пользователь должен ввести название города на русском языке.

Для работы скрипта требуются следующие библиотеки:

*import [pandas](https://pandas.pydata.org/docs/)*

*from [geopy](https://geopy.readthedocs.io/en/stable/index.html) import geocoders*

*import [sqlite3](https://docs.python.org/3/library/sqlite3.html)*

*import [datetime](https://docs.python.org/3/library/datetime.html)*

*import [requests](https://requests.readthedocs.io/en/latest/index.html)*

*import [json](https://docs.python.org/3/library/json.html)*


## Формат предоставления данных в excel:

![image](https://user-images.githubusercontent.com/111370737/194566837-41f419f3-fecf-44b4-83a7-196ec1190101.png)

* ***date*** - дата, на которую сделан прогноз погоды.
* ***time_of_day*** - время суток. Возможные значения: morning - утро, day - день, evening - вечер, night - ночь.
* ***temp_min*** - минимальная температура time_of_day.
* ***temp_max*** - максимальная температура time_of_day.
* ***average_daylight_temperature*** - средняя температура за световой день(time_of_day != night).
* ***condition*** - состояние погоды. Возможные значения:


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

* ***pressure_mm*** - Давление (в мм рт. ст.).
* ***humidity*** - Влажность воздуха (в процентах).
* ***magnetic_field_category*** - состояние магнитного поля. Возможные значения:

  Calm - спокойное (индекс магнитного поля равен менее 4).

  Unstable - неустойчивое (индекс магнитного поля равен 4).

  Weakly perturbed - слабо возмущенное (индекс магнитного поля равен 5).

  Disturbed - возмущенное (индекс магнитного поля равен 6).

  Magnetic storm - магнитная буря (индекс магнитного поля равен 7).

  Big magnetic storm - Большая магнитная буря (индекс магнитного поля равен  более 7).

  no data available - Яндекс Погода показывает состояние магнитного поля на сегодня и ближайшие три дня. Прогноз на последующие дни не формируется, потому                       что его точность невысока.
* ***category_pressure*** - идентификатор резкого изменения атмосферного давления (разница между max и min значениями больше или равна 5 мм рт.ст.). Возможные значения:
                          
  a sharp drop in atmospheric pressure is expected - ожидается резкое увеличение атмосферного давления.
  
  " " - не ожидается резкого увеличения атмосферного давления.

## Формат предоставления данных в sqlite:

| city_name     | date              | request_status |
| ------------- |:-----------------:| --------------:|
| Samara        | 03-10-2022 13:53  | successfully   |
| Jhsdcb        | 03-10-2022 13:58  | error          |
| Samara        | 03-10-2022 13:58  | successfully   |

city_name - введеное пользователем значение.

date - дата и время выполнения скрипта.

request_status - статус выполнения скрипта - успешно/ошибка.

