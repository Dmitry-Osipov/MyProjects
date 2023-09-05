from typing import Union

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


# Метод с поиском через словарь:


def twoSum(nums: list[int], target: int) -> list[int]:
    num_to_index = {}  # Словарь для хранения чисел и их индексов

    for index, number in enumerate(nums):
        print(f'Индекс - {index}, Число - {number}')
        complement = target - number  # Вычисляем, какое число нужно для достижения цели
        print(f'Разность цели и числа - {complement}')

        print(f'Имеющийся словарь: {num_to_index}')
        if complement in num_to_index:
            return [num_to_index[complement], index]  # Возвращаем индексы чисел

        num_to_index[number] = index  # Добавляем текущее число в словарь с его индексом
        print(f'Обновлённый словарь: {num_to_index}')

    return []


print(twoSum([3, 2, 3], 6))

"""
Как это работает:
1) Мы создаем словарь num_to_index, в котором будем хранить числа и их индексы.
2) Мы проходим по списку чисел nums с помощью enumerate, чтобы получить и индексы, и числа.
3) Для каждого числа вычисляем значение complement, которое необходимо для достижения цели.
4) Если complement уже присутствует в словаре num_to_index, то это означает, что мы нашли пару чисел, дающих нужную 
   сумму.Возвращаем индексы этих чисел.
5) Если complement не найден, добавляем текущее число в словарь num_to_index со значением его индекса.
6) Если не было найдено подходящей пары чисел, возвращаем пустой список.
Этот код должен вернуть индексы чисел, дающих нужную сумму target.
"""


# Метод двух указателей:


def find_target_sum(nums: list, target: int) -> Union[list, str]:
    # Инициализируем два указателя
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            # Нашли пару чисел, сумма которых равна sum_number
            return [left, right]
        elif current_sum < target:
            # Если сумма меньше sum_number, двигаем левый указатель вправо
            left += 1
        else:
            # Если сумма больше sum_number, двигаем правый указатель влево
            right -= 1

    # Если не найдено пары чисел, сумма которых равна sum_number
    if right <= left:
        return "Пара чисел не найдена"


all_numbers = [-4, -3, 2, 4, 8, 10, 15]
all_numbers.sort()
sum_number = 5

print(find_target_sum(all_numbers, sum_number))
