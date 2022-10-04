# yaweather

Данный скрипт через API собирает данные на сервисе яндекс погоды на ближайшие 7 дней(отсчет от даты запроса), складывает их в excel в определенном формате и скачивает его.

Для работы скрипта требуются следующие библиотеки:

import pandas as pd

from yaweather import Russia, YaWeather

import sqlite3 as sl

import datetime

![image](https://user-images.githubusercontent.com/111370737/193848817-e78875ad-96b5-4b36-b651-1e79144d87de.png)
