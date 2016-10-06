# -*- coding: utf-8 -*-
import argparse
from collections import Counter
import os
import re
import sys


def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def get_named_argument(arg_name: str) -> str:
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument('--' + arg_name)
        return getattr(parser.parse_args(sys.argv[1:]), arg_name)
    else:
        print('Введите параметр в формате --%s Значение' % arg_name)
        exit(1)


def load_data(filepath: str):
    if os.path.isfile(filepath):
        try:
            with open(filepath, mode='r') as file:
                return re.findall(r'[^\W|\d]+', file.read().lower())
        except PermissionError:
            print('У вас нет прав доступа к файлу')
            exit(1)
    else:
        print('Файл не найден')
        exit(1)


def get_most_frequent_words(text):
    return Counter(text).most_common(10)


if __name__ == '__main__':
    file_path = get_named_argument('file')
    load_win_unicode_console()
    print(get_most_frequent_words(load_data(file_path)))
