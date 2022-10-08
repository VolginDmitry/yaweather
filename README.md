# yaweather
<img width="877" alt="image" src="https://user-images.githubusercontent.com/111370737/194711886-39c27cea-54f5-42f3-8c0a-323f59213a90.png">


Данный скрипт через API собирает данные на сервисе Яндекс.Погода на ближайшие 7 дней(отсчет от даты запроса), складывает их в excel в определенном формате и скачивает его. А также складывает сведения о входных параметрах, дате/времени запроса и результатах работы (успешно или ошибка) в sqlite. Пользователь должен ввести название города на русском языке.

Для работы скрипта требуются следующие библиотеки:

*import [datetime](https://docs.python.org/3/library/datetime.html)*

*from [geopy](https://geopy.readthedocs.io/en/stable/index.html) import geocoders*

*import [json](https://docs.python.org/3/library/json.html)*

*import [pandas](https://pandas.pydata.org/docs/)*

*import [requests](https://requests.readthedocs.io/en/latest/index.html)*

*import [sqlite3](https://docs.python.org/3/library/sqlite3.html)*


## Формат предоставления данных в excel:

![image](https://user-images.githubusercontent.com/111370737/194717742-92778610-420d-47d7-9738-d51eec072d16.png)

* ***Дата*** - дата, на которую сделан прогноз погоды.
* ***Время суток*** - время суток. Возможные значения: утро, день, вечер, ночь.
* ***Минимальная температура*** - минимальная температура за утро, день, вечер, ночь.
* ***Максимальная температура*** - максимальная температура за утро, день, вечер, ночь.
* ***Cредняя температура за световой день*** - средняя температура за световой день(Время суток != ночь).
* ***Описание погоды*** - состояние погоды. Возможные значения: 
  
  ясно, малооблачно, облачно с прояснениями, пасмурно, морось, небольшой дождь, дождь, умеренно сильный дождь, сильный дождь, длительный сильный дождь, ливень, дождь со снегом, небольшой снег, снег, снегопад, град, гроза, дождь с грозой, гроза с градом.

* ***Атмосферное давление*** - атмосферное давление (в мм рт. ст.).
* ***Влажность*** - влажность воздуха (в процентах).
* ***Состояние магнитного поля*** - состояние магнитного поля. Возможные значения:

  спокойное (индекс магнитного поля равен менее 4).

  неустойчивое (индекс магнитного поля равен 4).

  слабо возмущенное (индекс магнитного поля равен 5).

  возмущенное (индекс магнитного поля равен 6).

  магнитная буря (индекс магнитного поля равен 7).

  Большая магнитная буря (индекс магнитного поля равен  более 7).

  Яндекс Погода показывает состояние магнитного поля на сегодня и ближайшие три дня. Прогноз на последующие дни не формируется, потому                       что его точность невысока.
* ***Идентификатор резкого изменения атмосферного давления*** - идентификатор резкого изменения атмосферного давления (разница между max и min значениями больше или равна 5 мм рт.ст.). Возможные значения:
                          
  Ожидается резкое изменение атмосферного давления - ожидается резкое изменение атмосферного давления.
  
  " " - не ожидается резкого изменения атмосферного давления.

## Формат предоставления данных в sqlite:

| city_name     | date              | request_status |
| ------------- |:-----------------:| --------------:|
| Самара        | 03-10-2022 13:53  | successfully   |
| Укпукп        | 03-10-2022 13:58  | error          |
| Москва        | 03-10-2022 13:58  | successfully   |

city_name - введеное пользователем значение.

date - дата и время выполнения скрипта.

request_status - статус выполнения скрипта - успешно/ошибка.

