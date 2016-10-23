# -*- coding: utf-8 -*-
import argparse
import re
import sys
import chardet
from collections import Counter

MOST_FREQUENT_WORDS_COUNT_DEFAULTS = 10


def load_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    и раскрашивание символов
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def load_text_from_file(file_path: str):
    raw_data = open(file_path, mode='rb').read()
    file_encoding = chardet.detect(raw_data)['encoding']
    with open(file_path, mode='r', encoding=file_encoding) as file:
        return re.findall(r'[^\W|\d]+', file.read().lower())


def get_most_frequent_words(text, count):
    return Counter(text).most_common(count)


def print_most_frequent_words_list(words_list):
    for number in range(len(words_list)):
        print('%d. Слово: "%s" Частота использования: %s раз' % (number + 1,
              words_list[number][0], words_list[number][1]))


if __name__ == '__main__':

    load_win_unicode_console()

    parser = argparse.ArgumentParser()
    parser.add_argument('--text', help='Введите путь к текстовому файлу')
    parser.add_argument('--count',
                        help='Введите количество слов',
                        default=MOST_FREQUENT_WORDS_COUNT_DEFAULTS,
                        type=int)
    if parser.parse_args().text:
        # неверный путь обработается далее в OSError
        text_file_path = parser.parse_args().text
        # тут проверка, целое ли это число будет в argparse
        top_words_count = abs(parser.parse_args().count)
    else:
        parser.print_help()
        exit(1)

    try:
        text_for_analyze = load_text_from_file(text_file_path)
    except OSError as error:
        print('Ошибка: %s в файле: %s' % (error.strerror, error.filename))
        exit(1)

    most_frequent_words = \
        get_most_frequent_words(text_for_analyze, top_words_count)
    print_most_frequent_words_list(most_frequent_words)
