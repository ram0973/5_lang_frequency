# Решение задачи [№5](https://devman.org/challenges/5/) с сайта [devman.org](https://devman.org)

## Условие задачи:

В этой задаче нужно написать скрипт, который должен принимать на вход путь до текстового файла и выводить в 
консоль десять самых популярных слов в этом файле в порядке убывания частоты.

Потом можно попробовать скормить ему разные тексты. "Война и мир". Всю Википедию. 
Кстати, такой скрипт должен нормально работать не только с русским, но и с другими языками.

## Системные требования

```
Python 3.5.2+
Внешний модуль win-unicode-console
Внешний модуль chardet
```

## Установка 

Windows

```    
git clone https://github.com/ram0973/5_lang_frequency.git
cd lang_frequency
pip install -r requirements.txt
```

Linux

```    
git clone https://github.com/ram0973/5_lang_frequency.git
cd lang_frequency
pip3 install -r requirements.txt
```

## Описание работы
Пользователь вводит путь к файлу как обязательный аргумент text,
и необязательный аргумент count - число слов для вывода.
Если аргумент count не задан, выводится количество слов из константы
MOST_FREQUENT_WORDS_COUNT_DEFAULTS в файле lang_frequency.py (по 
умолчанию 10)

Пример: 
```
python lang_frequency.py --text Hamlet.txt --count 100
```

Скрипт выводит список наиболее часто встречающихся в тексте слов, их 
порядковый номер и количество повторений. 
    
## Запуск

Windows

python lang_frequency.py --text Hamlet.txt --count 100
 
Linux
 
python3 lang_frequency.py --text Hamlet.txt --count 100

## Лицензия

[MIT](http://opensource.org/licenses/MIT)