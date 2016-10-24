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


def load_words_from_file(file_path: str) -> list:
    """
    Загружаем слова из текстового файла неизвестной кодировки
    :param file_path: путь к файлу
    :return: список слов файла
    """
    with open(file_path, mode='rb') as binary_file:
        raw_data = binary_file.read()
        file_encoding = chardet.detect(raw_data)['encoding']
    with open(file_path, mode='r', encoding=file_encoding) as text_file:
        return re.findall(r'[^\W|\d]+', text_file.read().lower())


def get_most_frequent_words(text: list, count: int) -> list:
    """
    Получаем список, содержащий кортежи слов c их количеством в списке text
    [('foo',3),('bar',7)]
    :param text: список слов
    :param count: сколько слов отбирать
    :return: список кортежей слов и их количества
    """
    return Counter(text).most_common(count)


def print_most_frequent_words_list(words_list: list):
    """
    Печатаем список наиболее встречающихся слов
    :param words_list: список слов в виде [('foo',3),('bar',7)]
    """
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
        text_for_analyze = load_words_from_file(text_file_path)
    except OSError as error:
        print('Ошибка: %s в файле: %s' % (error.strerror, error.filename))
        exit(1)

    most_frequent_words = \
        get_most_frequent_words(text_for_analyze, top_words_count)
    print_most_frequent_words_list(most_frequent_words)
