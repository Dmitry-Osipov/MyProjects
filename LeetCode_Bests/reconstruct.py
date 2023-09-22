"""
В файле задано уравнение вида q + w = e (q, w, e >= 0). Некоторые цифры могут быть заменены знаком вопроса,
например 2? + ?5 = 69.
Восстановите выражение до верного равенства.
Предложите хотя бы одно решение или сообщите, что его нет.
Напишите класс Equation, содержащий метод getSolution, который будет считывать уравнение из файла и восстановит его до
верного равенства.
Выведите сначала строку формата "Given the equation: {выражение из файла}".
А затем верните строку формата "Result: {цельное выражение}".
Если выражение не имеет решений - верните строку "No solution".

Пример:
Given the equation: ? + 4 = 9
Result: 5 + 4 = 9
"""


class Equation:
    @staticmethod
    def get_solution(equation: str) -> str:
        new_equation, target = equation.split('=')
        target = int(target)
        for digit in range(10):
            try:
                modified_equation = new_equation.replace('?', str(digit))
                if eval(modified_equation) == target:
                    return (f'Given the equation: {equation}\n'
                            f'Result: {modified_equation}= {target}')
            except SyntaxError:
                continue

        return 'No solution'


example1 = '? + 8 = 16'
example2 = '?4 + 3? = 78'
example3 = '?20 + ?70 = 690'
example4 = '2? + ?5 = 69'
example5 = '?34 + 21?3 = 2891'
example6 = '?2 + 3? = 45'

print(Equation.get_solution(example1))
print(Equation.get_solution(example2))
print(Equation.get_solution(example3))
print(Equation.get_solution(example4))
print(Equation.get_solution(example5))
print(Equation.get_solution(example6))
