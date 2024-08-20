
def all_variants(text):
    for size in range(1, len(text)+1):
        for i in range(len(text)):
            result = text[i]
            if size > 1:
                for j in range(len(text)):
                    if j <= i:
                        continue
                    if not text[j] in result:
                        result += text[j]
                    if len(result) == size:
                        yield result
                        result = text[i]
            else:
                yield result

'''Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, 
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
'''
def main():
    a = all_variants("abcd")
    for i in a:
        print(i)

'''Вывод на консоль (дожно быть):
a
b
c
ab
bc
abc'''

if __name__ == '__main__':
    main()

'''
ВНИМАНИЕ: 
для abc -- работает
для abcd -- выводит всё, кроме abd и acd!!!
'''