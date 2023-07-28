koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

import random
random.shuffle(koloda)

print('Поиграем в Blackjack?')
count = 0

while True:
    choice = input('Будете брать карту? yes/no\n')
    if choice == 'yes':
        current = koloda.pop()
        print('Вам попалась карта', current)
        count += current
        if count > 21:
            print('К сожалению, Вы проиграли, Ваше количество очков: ', count)
            break
        elif count == 21:
            print('У Вас 21 очко. Вы победили!')
            break
        else:
            print('Ваше количество очков: ', count)
    elif choice == 'no':
        print('Вы закончили игру. Ваше количество очков: ', count)
        break
print('До новых встреч!')