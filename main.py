from random import choice
from collections import Counter
from datetime import datetime, time
import re

# воспользовался текстовым файлом с именами из другой задачи
with open('randomNames.txt', encoding='utf-8') as fl: namesList = [line.strip() for line in fl]
'''
    1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
    (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
'''
def f(namesList, N):
    '''
    :param1: базовый список имен
    :param2: количество элементов в списке имен
    :return: генерируемый список имен длины (N) из базового

    '''
    return [choice(namesList) for _ in range(N)]

bigNamesList = f(namesList, 100)
print(bigNamesList)

'''
    2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
'''
def getPopName(bigNamesList):

# # Вариант 1 (работает только для первого вхождения)
#     return max(set(bigNamesList), key=bigNamesList.count)

# Вариант 2 (возвращает словарь вида {'имя':'частота встречаемости'})
    bigNamesCounter = Counter(bigNamesList)
    maxC = max(bigNamesCounter.values())
    return {k: v for k, v in bigNamesCounter.items() if v == maxC}

moustPopNames = getPopName(bigNamesList)
print(moustPopNames)

'''
    3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
'''

def getInfreqLetter(bigNamesList):


# # Вариант 1 (только первое найденное минимальное значение)
#     return min(set(x[0] for x in bigNamesList), key=bigNamesList.count)

# Вариант 2 (возвращает словарь вида {'Первая буква имени':'частота встречаемости'})

    InfreqFirstLetter = Counter([x[0] for x in bigNamesList])
    minL = min(InfreqFirstLetter.values())
    return {k: v for k, v in InfreqFirstLetter.items() if v == minL}


firstInfreqLetter = getInfreqLetter(bigNamesList)
print(firstInfreqLetter)



'''
4.  В файле с логами найти дату самого позднего лога (по метке времени)
'''
# # Вариант 1 (ищет самое позднее время в логе и возвращает дату-время в формате <дата-время> )
#
# pattern = re.compile('\d\d:\d\d:\d\d')
# maxTime = ''
#
# with open('log') as fl:
#     for idx, line in enumerate(fl):
#         timeLine = pattern.findall(line)[0]
#         if maxTime < timeLine:
#             maxTime = timeLine
#             dateLine = line
#
# # # строка
# # print(dateLine[:19])
#
# # дата-время
# print(datetime.strptime(dateLine[:19],'%Y-%m-%d %H:%M:%S'))

# Вариант 2 (ищет самую позднюю дату в логе и возвращает дату-время в формате <строка>)

with open('log') as fl: print(max(line[:19] for line in fl))