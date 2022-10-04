# yaweather

Данный скрипт через API собирает данные на сервисе яндекс погоды на ближайшие 7 дней(отсчет от даты запроса), складывает их в excel в определенном формате и скачивает его.

Для работы скрипта требуются следующие библиотеки:

import pandas as pd

from yaweather import Russia, YaWeather

import sqlite3 as sl

import datetime

![image](https://user-images.githubusercontent.com/111370737/193848050-63d413c6-6a98-4c4d-96e9-ad232f9829ad.png)

