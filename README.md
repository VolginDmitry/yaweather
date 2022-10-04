# yaweather

Данный скрипт через API собирает данные на сервисе яндекс погоды на ближайшие 7 дней(отсчет от даты запроса), складывает их в excel в определенном формате и скачивает его.

Для работы скрипта требуются следующие библиотеки:

import pandas as pd
from yaweather import Russia, YaWeather
import sqlite3 as sl
import datetime

date	time_of_day	temp_min	temp_max	average_daylight_temperature	condition	pressure_mm	humidity	magnetic_field_category	category_pressure
2022-10-04	morning	10	12	10	cloudy	741	80	Calm	a sharp drop in atmospheric pressure is expected
2022-10-04	day	10	12	10	rain	743	83	Calm	a sharp drop in atmospheric pressure is expected
2022-10-04	evening	8	9	10	light-rain	745	88	Calm	a sharp drop in atmospheric pressure is expected
2022-10-04	night	10	11	10	light-rain	740	83	Calm	a sharp drop in atmospheric pressure is expected![image](https://user-images.githubusercontent.com/111370737/193848050-63d413c6-6a98-4c4d-96e9-ad232f9829ad.png)

