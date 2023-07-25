import requests
import dill
import pandas as pd
import os
from urllib.parse import urlencode

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'


def T1_obr():
    public_key = 'https://disk.yandex.lt/d/UdHX5-LHLd17tQ'  # Сюда вписываете вашу ссылку
    # Получаем загрузочную ссылку
    final_url = base_url + urlencode(dict(public_key=public_key))
    response = requests.get(final_url)
    download_url = response.json()['href']
    # Загружаем файл и сохраняем его
    download_response = requests.get(download_url)

    name_of_datafile = 'T1_obr.dat'
    tmp_count = 0
    tmp_name_of_datafile = name_of_datafile + ''
    while tmp_count < 100:
        tmp_count += 1
        if os.path.exists(os.path.join(os.getcwd(), tmp_name_of_datafile)):
            # если файл существует, то меняем название
            tmp_name_of_datafile = name_of_datafile[:-4] + f'_{tmp_count}' + '.dat'
        else:
            break
    name_of_datafile = tmp_name_of_datafile
    with open(name_of_datafile, 'wb') as f:  # Здесь укажите нужный путь к файлу
        f.write(download_response.content)
    with open(name_of_datafile, 'rb') as f:
        df = dill.load(f)
    os.remove(os.path.join(os.getcwd(), name_of_datafile))
    return df


if __name__ == '__main__':
    df = T1_obr()
    print(df)
