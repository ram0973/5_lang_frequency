# -*- coding: utf-8 -*-
import argparse
import re
import sys
from collections import Counter
from colorama import Fore, Style

MOST_FREQUENT_WORDS_COUNT_DEFAULTS = 10


def load_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    и раскрашивание символов
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()
        from colorama import init
        init()  # colorama


def get_text_file_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', help='Введите путь к текстовому файлу')
    parser.add_argument('--count',
                        help='Введите количество слов',
                        default=MOST_FREQUENT_WORDS_COUNT_DEFAULTS,
                        type=int)
    if parser.parse_args().text:
        return parser.parse_args().text, parser.parse_args().count
    else:
        parser.print_help()
        exit(1)


def load_data(file_path: str):
    with open(file_path, mode='r') as file:
        return re.findall(r'[^\W|\d]+', file.read().lower())


def get_most_frequent_words(text, count):
    return Counter(text).most_common(count)


def print_most_frequent_words_list(words_list):
    for number in range(len(words_list)):
        print('%d. Слово: "%s" Частота использования: %s раз' % (number + 1,
              words_list[number][0], words_list[number][1]))


if __name__ == '__main__':

    text_file_path, top_words_count = get_text_file_arguments()

    try:
        text_for_analyze = load_data(text_file_path)
    except OSError as error:
        print(Fore.RED+Style.BRIGHT, 'Ошибка: ', error.strerror, ' в файле: ',
              error.filename)
        exit(1)

    load_win_unicode_console()

    most_frequent_words = get_most_frequent_words(
        text_for_analyze, top_words_count)
    print_most_frequent_words_list(most_frequent_words)
