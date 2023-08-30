print('Я к вам пишу - чего же боле?')
print('Что я могу ещё сказать?')
print('Теперь, я знаю, в вашей воле')
print(a)
print('Меня презреньем наказать.')
print('Но вы, к моей несчастной доле')
print('Хоть каплю жалости храня,')
print('Вы не остановите меня.')

"""
При выполнении программы сработает ошибка (исключение) NameError: name 'a' is not defined. Часть программы у
нас отработала (та часть, что идёт до исключительной ситуации). Но далее работа прерывается. Помимо этого, исключения
бывают. Например, NameError, TypeError, ValueError, ZeroDivisionError и т.д. Также исключения бывают нескольких типов:
те ошибки, которые возникают в процессе выполнения программы называются исключениями в процессе выполнения;
есть ещё исключения в процессе компиляции - это, как правило, синтаксические ошибки (такие ошибки не дадут выполнить ни
единой строчки).
Когда мы делаем обработку исключений, то нас интересуют именно исключения в момент выполнения, ибо при компиляции нужно
просто писать правильно программу, тут ничего не сделаешь. А вот в момент исполнения можно что-то сделать. В основном
ошибки в момент выполнений порождает пользователь при некорректных вводных (например, открытие несуществующего файла,
некорректное заполнение полей ввода и т.п.). Всех проблем заранее предусмотреть невозможно, поэтому важно уметь
обрабатывать исключения. Как это сделать?
Для этого существует блок try-except. Мы как бы говорим попробовать программе выполнить действие. Далее прописываем блок
except: обязательно пишем тип ошибки, который можем получить, а затем что делать, если мы её получили. Таким образом, мы
не получим исключения, и программа будет работать дальше.
"""

try:
    f = open('myfile.md')
except FileNotFoundError:
    print('Невозможно открыть программу')

# Для того чтобы отловить 2 типа ошибок сразу, можно прописывать блоки except друг за другом.
try:
    x, y = map(int, input('Введите целые числа: ').split())
    res = x / y
except ValueError:
    print('Ошибка тип данных')
except ZeroDivisionError:
    print('Деление на 0')

# Также, чтобы отловить 2 ошибки сразу, можно использовать круглые скобки в одном блоке except. Но обычно пишут блоки
# except друг за другом, ибо тогда мы раздельно можем обрабатывать разные типы ошибок.
try:
    x, y = map(int, input('Введите целые числа: ').split())
    res = x / y
except (ValueError, ZeroDivisionError):
    print('Недопустимые данные')

"""
Существует определённая иерархия классов-исключений, во главе которой стоит Base Exception. Большая часть 
классов-исключений наследуется от класса Exception. Понимание иерархии нам даёт то, что благодаря одному базовому классу
мы можем отлавливать сразу несколько исключений более простым образом. Например, ZeroDivisionError, FloatingPointError, 
OverflowError наследуются от ArithmeticError, который наследуется от Exception. Т.е. прописав в блоке except 
ArithmeticError можно обрабатывать сразу несколько исключений.
"""

try:
    x, y = map(int, input('Введите целые числа: ').split())
    res = x / y
except ArithmeticError:
    print('Недопустимые данные')

"""
Также можно использовать для обработки исключений сам класс Exception, но он будет ловить все исключения, а это 
не рекомендуется. Т.е. если сначала прописать ValueError, то при ошибке ValueError обработает исключений именно этот 
блок, а если первым поставить блок Exception, то он будет ловить вообще все ошибки, и до последующего блока ValueError 
очередь даже не дойдёт. Однако если всё же требуется использовать Exception, то архитектура поимки исключений строится 
таким образом: сначала специализированные исключения, а потом общие. Также, если требуется поймать все исключения, то 
можно прописать except без указания каких-либо классов.
"""

try:
    x, y = map(int, input('Введите целые числа: ').split())
    res = x / y
except ValueError:
    print('Недопустимые данные')
except:
    print('Ошибка')

try:
    x, y = map(int, input('Введите целые числа: ').split())
    res = x / y
except Exception:
    print('Ошибка')
except ValueError:
    print('Недопустимые данные')
