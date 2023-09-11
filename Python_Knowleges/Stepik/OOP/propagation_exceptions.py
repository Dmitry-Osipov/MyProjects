"""
В файлах try_except.py и try_finally_else.py мы рассмотрели общее применение try-except-else-finally на примере простых
программ. В реальности программы куда сложнее и содержат вызовы различных функций и даже могут использовать
многопоточную реализацию. Посмотрим, как будет выглядеть сообщение об ошибке при использовании функций.
"""


def func1():
    return 1 / 0


print('Я к вам пишу - чего же боле?')
print('Что я могу ещё сказать?')
print('Теперь, я знаю, в вашей воле')
func1()  # Видим исключение в двух строчках - 9 и 15. Так произошло потому, что у нас само исключение возникло на 8
# строчке программы, а вызов функции происходит в 15 строчке. Когда вызывается та или иная функция, она помещается в
# стек вызова функции, т.е. с главного уровня нашей программы - main - была вызвана func1(). Исключение возникло на
# уровне функции, т.е. в 9 строчке и далее распространилось до основной программы на 15 строчке.
print('Меня презреньем наказать.')
print('Но вы, к моей несчастной доле')
print('Хоть каплю жалости храня,')
print('Вы не остановите меня.')

# Если определить 2 функции, которые вызывают друг друга, то мы увидим такое распространение:
# main -> func1() -> func2() тут оно зародилось, так что всё возвращается -> func1() -> main.


def func2():
    return 1 / 0


def func1():
    return func2()


func1()  # Теперь видим немного дугой стек распространения исключений: 28 -> 32 -> 35 строчки. Обрабатывать исключения
# можно на любом уровне этого стека, т.е. либо в main, либо в func1(), либо в func2(). На уровне main:


def func2():
    return 1 / 0


def func1():
    return func2()


try:
    func1()
except:
    print('ZeroDivisionError в __main__')

# На уровне func1():

def func2():
    return 1 / 0


def func1():
    try:
        return func2()
    except:
        print('ZeroDivisionError в func1')


func1()

# На уровне func2():


def func2():
    try:
        return 1 / 0
    except:
        print('ZeroDivisionError в func2')


def func1():
    return func2()


func1()
# Также важно заметить, что если мы в функции func2() обработаем ошибку, то она не дойдёт в блоке исключений до func1().