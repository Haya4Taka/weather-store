def insert_hourly_climate(cursor, data):
    stmt = 'INSERT INTO weather_hourly ' \
            '(city_id, datetime, weather, weather_description, temp, humidity, pressure)' \
            'VALUES (%s, FROM_UNIXTIME(%s), %s, %s, %s, %s, %s)'
    cursor.executemany(stmt, data)


def insert_daily_climate(cursor, data):
    stmt = 'INSERT INTO weather_daily ' \
            '(city_id, datetime, weather, weather_description, temp, humidity, pressure)' \
            'VALUES (%s, FROM_UNIXTIME(%s), %s, %s, %s, %s, %s)'
    cursor.executemany(stmt, data)


def delete_hourly_climate(cursor):
    stmt = 'DELETE FROM weather_hourly'
    cursor.execute(stmt)


def delete_daily_climate(cursor):
    stmt = 'DELETE FROM weather_daily'
    cursor.execute(stmt)
