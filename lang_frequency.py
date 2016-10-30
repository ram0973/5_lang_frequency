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
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def load_text_from_file(file_path: str) -> str:
    """
    Загружаем слова из текстового файла неизвестной кодировки
    :param file_path: путь к файлу
    :return: содержимое файла
    """
    with open(file_path, mode='rb') as binary_file:
        raw_data = binary_file.read()
        file_encoding = chardet.detect(raw_data)['encoding']
    with open(file_path, mode='r', encoding=file_encoding) as text_file:
        return text_file.read()


def get_words_from_text(text: str):
    """
    Возвращаем слова из text
    :param text: текст, из которого надо получить слова
    :return: очередное слово из текста
    """
    for match in re.finditer(r'[^\W|\d]+', text, flags=re.IGNORECASE):
        # генератор для экономии памяти
        yield match.group()


def get_most_frequent_words(words, count: int) -> list:
    """
    Получаем список, содержащий кортежи (слово, количество в тексте)
    -> [('foo',3),('bar',7)]
    :param words: итератор по словам
    :param count: сколько слов отбирать
    :return: список кортежей (слово, количество в тексте)
    """
    return Counter(words).most_common(count)


def print_most_frequent_words_list(words_list: list):
    """
    Печатаем список наиболее встречающихся слов
    :param words_list: список слов в виде [('foo',3),('bar',7)]
    """
    for index, value in enumerate(words_list):
        print('%d. Слово: "%s" Частота использования: %s раз' % (index + 1,
              value[0], value[1]))


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
        get_most_frequent_words(
            get_words_from_text(text_for_analyze),
            top_words_count
        )
    print_most_frequent_words_list(most_frequent_words)
