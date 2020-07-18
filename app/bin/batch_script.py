import sys
from os import path as p
app_home = p.abspath(p.join(p.dirname(p.abspath(__file__)), '..'))
sys.path.append(app_home)

from conf.city_conf import CITY_CONF
from lib import weather
from lib.db import query, context


def main():
    hourly_data = []
    daily_data = []
    # 並列化したい
    for value in CITY_CONF.values():
        city_id = value['id']
        response = weather.fetch_weather(**value['location'])
        hourly_data += [
            (city_id, d['dt'],
             d['weather'][0]['main'],
             d['weather'][0]['description'],
             d['temp'],
             d['humidity'],
             d['pressure']) for d in response['hourly']]
        daily_data += [
            (city_id, d['dt'],
             d['weather'][0]['main'],
             d['weather'][0]['description'],
             d['temp']['day'],
             d['humidity'],
             d['pressure']) for d in response['daily']]

    with context.db_connection() as connection:
        with context.will_commit(connection):
            cursor = connection.cursor()
            query.delete_hourly_climate(cursor)
            query.insert_hourly_climate(cursor, hourly_data)

        with context.will_commit(connection):
            cursor = connection.cursor()
            query.delete_daily_climate(cursor)
            query.insert_daily_climate(cursor, daily_data)


if __name__ == '__main__':
    main()
