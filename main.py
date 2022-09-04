from parser import parser
from conv_file import conversion_file
import count
import os
import sys
import time

if __name__ == '__main__':
    print('ПАРСИНГ САЙТА "aftershock.news" и смотрим активность комментаторов !!!')
    request_1 = input('Осуществить парсинг ? (да/нет) : ')
    flag_request_1 = False
    while not flag_request_1:
        if request_1 == 'да':
            parser()
            conversion_file()
            flag_request_1 = True
        elif request_1 == 'нет':
            list_file = os.listdir()
            for name in list_file:
                if name == 'output.txt':
                    flag_request_1 = True
                    time_file = time.ctime(os.path.getctime(name))
                    time_file = time.strptime(time_file, "%a %b %d %H:%M:%S %Y")
                    time_file = time.strftime("%d.%m.%Y", time_file)
                    print()
                    print('*' * 100)
                    print()
                    print(f'В системе есть файл "output.txt" за {time_file}')
                    break
            else:
                print()
                print('*' * 100)
                print()
                print('ERROR : НЕТ ФАЙЛА "output.txt" . Дальнейшая работа не возможна !  ')
                sys.exit()
        else:
            flag_request_1 = False
            request_1 = input('Я не понял , так будем парсить или нет ??? (да/нет) : ')
    print()
    print('*' * 100)
    print()
    request_2 = input('Вывести 20-ку самых результативных комментаторов ? (да/нет) : ')
    flag_request_2 = False
    list_name_commet = []
    while not flag_request_2:
        if request_2 == 'да':
            flag_request_2 = True
            list_max_20 = count.count_max_20()
            count.schedule_max_20(list_max_20)
            print()
            print('*' * 100)
            print()
            for i in list_max_20:
                print(f'{i[0]} : {i[1]} комментариев')
                list_name_commet.append(i[0])
            print()
            print('*' * 100)
            print()
            flag_request_2 = True
        elif request_2 == 'нет':
            print()
            print('*' * 100)
            print()
            sys.exit()
        else:
            flag_request_2 = False
            print()
            print('*' * 100)
            print()
            request_2 = input('Не понял твоего ответа ! Введи да/нет : ')
    flag_request_3 = False
    request_3 = input('Введи имя комментатора из списка или "нет" : ')
    while not flag_request_3:
        if request_3 in list_name_commet:
            print()
            print('*' * 100)
            print()
            print(f'График активности {request_3} по дням')
            count.number_author_comments(request_3)
            print()
            print('*' * 100)
            print()
            print(f'График активности {request_3} по дням и часам')
            count.number_author_comments_hour(request_3)
            print()
            print('*' * 100)
            print()
            for i in list_max_20:
                print(f'{i[0]} : {i[1]} комментариев')
                list_name_commet.append(i[0])
            print()
            print('*' * 100)
            print()
            request_3 = input('Введи имя следующего комментатора из списка или "нет" : ')
        elif request_3 == 'нет':
            print()
            print('*' * 100)
            print()
            sys.exit()
        else:
            print()
            print('*' * 100)
            print()
            request_3 = input('Введи имя комментатора без ошибок : ')


