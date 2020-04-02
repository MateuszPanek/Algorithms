#!/Users/mateusz/PycharmProjects/AlgorytmyIStrukturyDanych/venv/bin/python3.7
#!/bin/bash -l

import os
import shutil
import datetime

desktop_path = '/Users/mateusz/Desktop'
os.chdir(desktop_path)
cleaning_time = datetime.datetime.now().replace(hour=17, minute=0, second=0, microsecond=0)
time_now = datetime.datetime.now()


def screenshots_directory_cleaner(desktop_path):
    if time_now > cleaning_time:
        try:
            shutil.rmtree(f'{desktop_path}/Zrzuty ekranu')
        except FileNotFoundError:
            pass
    else:
        try:
            os.listdir(f'{desktop_path}/Zrzuty ekranu')
            move_screenshots(desktop_path)
        except FileNotFoundError:
            os.mkdir(f'{desktop_path}/Zrzuty ekranu')
            move_screenshots(desktop_path)

    return True


def clean_screenshots(desktop_path):
    for item in os.listdir(f'{desktop_path}/Zrzuty ekranu'):
        if 'Zrzut ekranu' in item:
            print(os.path.abspath(item))
            # os.remove(os.path.abspath(item))
    return True


def move_screenshots(desktop_path):
    for item in os.listdir(f'{desktop_path}'):
        if 'Zrzut ekranu' in item:
            shutil.move(f'{os.path.abspath(item)}', f'{desktop_path}/Zrzuty ekranu/{item}')
    return True


screenshots_directory_cleaner(desktop_path)

