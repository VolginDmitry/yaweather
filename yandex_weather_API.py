# импортируем необходимые библиотеки
import datetime
from geopy import geocoders
import json
import pandas as pd
import requests
import sqlite3 as sl



# объявим переменную, которая будет содержать дату и время запроса
now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

# входные данные пользователя
city = input("Введите название города на русском языке:")
city = city.title()

# функция для определения широты и долготы введенного пользователем города
def geo_pos(city: str):
    geolocator = geocoders.Nominatim(user_agent="myapp")
    latitude = str(geolocator.geocode(city).latitude)
    longitude = str(geolocator.geocode(city).longitude)
    return latitude, longitude

# заключим наш код в конструкцию try/except для страховки от ошибок и внесения в БД корректных данных
try:
    # применяем функцию geo_pos
    lat_long= geo_pos(city)
    latitude = lat_long[0]
    longitude = lat_long[1]

    # переменная request_status - для внесения в БД
    request_status = 'successfully'

    # с помощью API подключимся к сервису "яндекс погода", спарсим данные, для удобства переведем ответ в формат json
    url = f'https://api.weather.yandex.ru/v2/forecast?&lang=ru_RU&limit=7&extra=true&lat={latitude}&lon={longitude}'
    headers = {"X-Yandex-API-Key": "bdfebc58-db84-4ee5-bf97-6fcabb48189d"}
    query = requests.get(url=url, headers=headers)
    json_data = json.loads(query.text)

    # создадим элементарную конструкцию по проверке названия города введенного пользователем с городом в json_data
    check_city = json_data['geo_object']['locality']['name'] == city
    if check_city == True:
        aa = 0
    else:
        print(abcd) # намеренно вызываем ошибку, чтобы в случае несовпадения перейти в блок except

    # объявим функцию по подготовке датафреймов с необходимыми признаками для разных значений времени суток(утро, день, вечер, ночь)
    def data_func(time_of_day):
        data = pd.DataFrame([(f['date'], time_of_day,
                              f['parts'][time_of_day]['temp_min'], f['parts'][time_of_day]['temp_avg'],
                              f['parts'][time_of_day]['temp_max'], f['parts'][time_of_day]['pressure_mm'],
                              f['parts'][time_of_day]['humidity'], f['parts'][time_of_day]['condition'])
                             for f in json_data['forecasts']],
                            columns=['date', 'time_of_day', 'temp_min', 'temp_avg', 'temp_max',
                                     'pressure_mm', 'humidity', 'condition'])
        return data

    # формируем датафрейм с необходимымыми признаками по ночным данным с использованием функции data_func
    night_data = data_func('night')

    # формируем датафрейм с необходимымыми признаками по утренним данным с использованием функции data_func
    morning_data = data_func('morning')

    # формируем датафрейм с необходимымыми признаками по дневным данным с использованием функции data_func
    day_data = data_func('day')

    # формируем датафрейм с необходимымыми признаками по вечерним данным с использованием функции data_func
    evening_data = data_func('evening')

    # формируем датафрейм с информацией по магнитному полю
    magnetic_field_data = pd.DataFrame([(json_data['forecasts'][f]['date'], json_data['forecasts'][f]['biomet']['index'])
                                        for f in range(4)],
                                        columns=['date', 'magnetic_field_index'])

    # функция для категорирования индексов магнитного поля
    def category_magnetic_field(row):
        if row['magnetic_field_index'] < 4:
            return 'Спокойное'
        elif row['magnetic_field_index'] == 4:
            return 'Неустойчивое'
        elif row['magnetic_field_index'] == 5:
            return 'Слабо возмущенное'
        elif row['magnetic_field_index'] == 6:
            return 'Возмущенное'
        elif row['magnetic_field_index'] == 7:
            return 'Магнитная буря'
        elif row['magnetic_field_index'] >= 8:
            return 'Большая магнитная буря'
        return 'Нет данных'

    # применяем функцию category_magnetic_field
    magnetic_field_data['magnetic_field_category'] = magnetic_field_data.apply(category_magnetic_field, axis=1)

    # для далнейшей работы объеденим датафреймы morning_data, day_data, evening_data, night_data, magnetic_field_data
    df_merge_easy = pd.concat([morning_data, day_data, evening_data, night_data]) \
                      .reset_index(drop=True) \
                      .merge(magnetic_field_data, how='left', on='date')

    # определим и округлим среднюю температуру за световой день
    df_avg_daylight_temp = df_merge_easy[df_merge_easy['time_of_day'] != 'night'] \
                                                  .groupby('date', as_index=False) \
                                                  .agg(avg_daylight_temp=('temp_avg', 'mean'))

    df_avg_daylight_temp['avg_daylight_temp'] = round(df_avg_daylight_temp['avg_daylight_temp'])

    # объеденяем датафреймы df_merge_easy и df_avg_daylight_temp
    df_merge_average = df_merge_easy.merge(df_avg_daylight_temp, how='left', on='date')

    # определяем и добавляем в df_merge_average разницу между максимальным и минимальным давлением
    df_merge_pressure = df_merge_average.groupby('date', as_index=False) \
                                        .agg(pressure_mm_min=('pressure_mm', 'min'),
                                             pressure_mm_max=('pressure_mm', 'max'))

    df_merge_pressure['pressure_mm_difference'] = df_merge_pressure['pressure_mm_max'] - \
                                                  df_merge_pressure['pressure_mm_min']

    df_merge_hard = df_merge_average.merge(df_merge_pressure, how='left', on='date')

    # объявим и применим функцию по категорированию pressure_mm_difference
    def category_pressure(row):
        if row['pressure_mm_difference'] >= 5:
            return 'Ожидается резкое изменение атмосферного давления'
        return ''

    df_merge_hard['category_pressure'] = df_merge_hard.apply(category_pressure, axis=1)

    # объявим и применим функцию по категорированию времени суток для последующей сортировки
    def time_of_day_category(row):
        if row['time_of_day'] == 'morning':
            return 1
        elif row['time_of_day'] == 'day':
            return 2
        elif row['time_of_day'] == 'evening':
            return 3
        return 4

    df_merge_hard['time_of_day_category'] = df_merge_hard.apply(time_of_day_category, axis=1)

    # отсортируем датафрейм и заполним пропуски
    df_merge_hard_sorted = df_merge_hard.sort_values(by=['date', 'time_of_day_category']) \
                                        .fillna('Нет данных') \
                                        .reset_index(drop=True)

    # формируем итоговый датафрейм
    df_final = df_merge_hard_sorted[['date', 'time_of_day', 'temp_min', 'temp_max', 'avg_daylight_temp',
                                     'condition', 'pressure_mm', 'humidity', 'magnetic_field_category',
                                     'category_pressure']]

    # Переведем названия колонок на русский язык
    df_final.columns = ['Дата', 'Время суток', 'Минимальная температура', 'Максимальная температура',
                        'Cредняя температура за световой день', 'Описание погоды', 'Атмосферное давление',
                        'Влажность','Состояние магнитного поля', 'Изменчивость атмосферного давления']

    # Переведем знучения столбцов 'Время суток' и 'Описание погоды' на русский язык
    df_final = df_final.replace(['night', 'morning', 'day', 'evening','clear','partly-cloudy', 'cloudy',
                                 'overcast','drizzle', 'light-rain', 'rain','moderate-rain',
                                 'heavy-rain','continuous-heavy-rain','showers', 'wet-snow','light-snow',
                                 'snow','snow-showers','hail','thunderstorm','thunderstorm-with-rain','thunderstorm-with-hail'],
                                ['Ночь', 'Утро', 'День', 'Вечер', 'Ясно', 'Малооблачно', 'Облачно с прояснениями',
                                 'Пасмурно', 'Морось','Небольшой дождь', 'Дождь','Умеренно сильный дождь',
                                 'Сильный дождь','Длительный сильный дождь','Ливень','дождь со снегом','Небольшой снег',
                                 'Снег','Снегопад','Град','Гроза','Дождь с грозой','Гроза с градом'])

    # сохраняем df_final в формате excel
    writer = pd.ExcelWriter('yandex_weather_7_days.xlsx')
    df_final.to_excel(writer, sheet_name='Погода', engine='xlsxwriter',index=False)
    for column in df_final:
        col_idx = df_final.columns.get_loc(column)
        writer.sheets['Погода'].set_column(col_idx, col_idx, 15)
    writer.save()

    # создаем БД
    con = sl.connect('my-test.db')

    crsr = con.cursor()

    try:
        # Создаем таблицу в БД
        sql_command = """CREATE TABLE yandex_weather (
                     city_name VARCHAR(30),
                     date DATE,
                     request_status VARCHAR(30)
                     );"""
        crsr.execute(sql_command)

    except:
        aa = 0

    # Добавляеем данные в БД
    crsr.execute(
        "INSERT INTO yandex_weather (city_name,date,request_status) VALUES ('%s','%s','%s')" % (city, now, request_status))
    con.commit()
    con.close()
    print('Выполнено!')

except:
    # данный блок срабатывает, если в блоке try была ошибка
    # Здесь выводится сообщение об ошибке и заносится информация в БД
    print('Ошибка! Убедитесь, что название города написано правильно!')

    request_status_neg = 'error'
    con = sl.connect('my-test.db')

    crsr = con.cursor()

    try:
        # Создаем таблицу в БД
        sql_command = """CREATE TABLE yandex_weather (
                     city_name VARCHAR(30),
                     date DATE,
                     request_status VARCHAR(30)
                     );"""
        crsr.execute(sql_command)

    except:
        aa = 0

    # Добавляеем данные в БД
    crsr.execute(
        "INSERT INTO yandex_weather (city_name,date,request_status) VALUES ('%s','%s','%s')" % (city, now, request_status_neg))
    con.commit()
    con.close()