# yaweather

Данный скрипт через API собирает данные на сервисе яндекс погоды на ближайшие 7 дней(отсчет от даты запроса), складывает их в excel в определенном формате и скачивает его.

Для работы скрипта требуются следующие библиотеки:

*import [pandas](https://pandas.pydata.org/docs/)*

*from [yaweather](https://pypi.org/project/yaweather/) import Russia, YaWeather*

*import [sqlite3](https://docs.python.org/3/library/sqlite3.html)*

*import [datetime](https://docs.python.org/3/library/datetime.html)*

## Формат предоставления данных в excel:

![image](https://user-images.githubusercontent.com/111370737/193848817-e78875ad-96b5-4b36-b651-1e79144d87de.png)
