#!/usr/bin/env python3
import sys
import requests
from datetime import datetime, timedelta


def get_code(name, name_type='enName'):
    area = requests.get("https://www.jma.go.jp/bosai/amedas/const/amedastable.json").json()
    for code in area:
        if area[code][name_type] == name:
            return code

    return None


def get_json(datetime_str):
    return requests.get(f"https://www.jma.go.jp/bosai/amedas/data/map/{datetime_str}.json").json()


def get_data(code, datetime_str=None):
    if not datetime_str:
        datetime_str = datetime.now().strftime('%Y%m%d%H0000')
        try:
            data = get_json(datetime_str)[code]
        except Exception:
            # try to get previous data
            datetime_str = (datetime.now() - timedelta(hours=1)).strftime('%Y%m%d%H0000')
            data = get_json(datetime_str)[code]
    else:
        data = get_json(datetime_str)[code]
    return data


def main():
    code = '44132'
    name_type = 'enName'
    datetime_str = None
    if len(sys.argv) > 1:
        code = sys.argv[1]
        if len(sys.argv) > 2:
            name_type = sys.argv[2]
            if len(sys.argv) > 3:
                datetime_str = sys.argv[3]
    if not code.isdigit():
        code = get_code(code, name_type)
    data = get_data(code, datetime_str)
    print(f"気温: {data['temp'][0]}℃, 湿度: {data['humidity'][0]}%")


if __name__ == '__main__':
    main()
