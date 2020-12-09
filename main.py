#!/usr/bin/env python3
# Money Flow Manager by CISCer Beta for Windows v0.1.2
import csv
import os
import datetime


def Clear():
    print('\n'*100)


# Colours
yellow, blue, green, mc, red = "\033[33m", "\033[34m", "\033[32m", "\033[0m", "\033[31m"  # mc - clean colours


def DateTime():
    hms = datetime.datetime.today()  # Дата и время
    date_format = hms.date()
    hour = int(hms.hour)  # Формат часов
    minute = int(hms.minute)  # Формат минут
    second = int(hms.second)  # Формат секунд
    if hour < 10:
        hour = str(0) + str(hour)
    if minute < 10:
        minute = str(0) + str(minute)
    if second < 10:
        second = str(0) + str(second)
    time_format = (str(hour), str(minute), str(second))
    time_now = ":".join(time_format) + ' ' + str(date_format)
    return time_now


time_now = DateTime()


def MainFun():
    print(blue, 'Money Flow Program v0.1.2 Beta\nby CISCer', mc)
    file_data_base = ".data.dat"
    check_file_data_base = os.path.exists(file_data_base)
    # Reader
    if check_file_data_base == True:
        # Если файл уже создан, выводтся содержимое и дальнейшее взаимодействие с программой происходит тут
        def ShowingContent():
            with open(file_data_base, encoding='utf-8') as data:
                s = 0
                reader = csv.DictReader(data, delimiter=',')
                print('\n' + yellow + '--- Все операции ---' + mc)
                for line in reader:
                    s += 1
                    row = (line["date"], line["balance"])
                    print(str(s) + '. ' + ' --> '.join(row))
        ShowingContent()

        while True:
            print('\n''1 - Посмотреть подробности' '\n' '2 - Добавить операцию')
            change = input('(1/2): ')
            if change == '-x':
                quit()
            if change == '1':
                num = int(input('Номер: '))
                Clear()
                ShowingContent()
                with open(file_data_base, encoding='utf-8') as profiles:
                    reader = csv.DictReader(profiles, delimiter=',')
                    count = 0
                    for line in reader:
                        count += 1
                        if count == num:
                            # Colours
                            if int(line["income"]) == 0:
                                cl_i = yellow
                            elif int(line["income"]) > 0:
                                cl_i = green
                            if int(line["consumption"]) > 0:
                                cl_c = red
                            if int(line["consumption"]) == 0:
                                cl_c = green
                            if int(line["consumption"]) > int(line["income"]):
                                cl_b = red
                            elif int(line["balance"]) == 0:
                                cl_b = yellow
                            elif int(line["balance"]) > 0:
                                cl_b = green
                            elif int(line["balance"]) < 0:
                                cl_b = red
                            print('\n', 'На момент', yellow, line["date"], mc,
                                  'на счету', cl_b, line["balance"], mc, '₽', '\n\n',
                                  'Доход составил', cl_i, line["income"], mc, '₽', '\n',
                                  'Примечание к доходу:', yellow, line["note_income"], mc, '\n\n',
                                  'Расход составил', cl_c, line["consumption"], '₽', mc, '\n',
                                  'Примечание к расходу:', yellow, line["note_consumption"], '\n', mc)

            elif change == '2':
                with open(file_data_base, 'a', encoding='utf-8') as data:
                    date = time_now
                    fieldnames = ['balance', 'income', 'consumption', 'date', 'note_income', 'note_consumption']
                    writer = csv.DictWriter(data, fieldnames=fieldnames)

                    income = int(input('Доход: '))
                    note_income = input('Примечание к доходу: ')
                    consumption = int(input('Расход: '))
                    note_consumption = input('Примечание к расходу: ')
                    balance = int(line["balance"]) + int(income) - int(consumption)

                    writer.writerow({'balance': balance,
                                     'income': income,
                                     'consumption': consumption,
                                     'date': date,
                                     'note_income': note_income,
                                     'note_consumption': note_consumption})
    # Запись
    if check_file_data_base == False:
        with open(file_data_base, mode="a", encoding='utf-8') as data:
            date = time_now
            fieldnames = ['balance', 'income', 'consumption', 'date', 'note_income', 'note_consumption']
            writer = csv.DictWriter(data, fieldnames=fieldnames)
            writer.writeheader()

            balance = int(input('Balance: '))

            writer.writerow({'balance': balance, 'income': 0, 'consumption': 0, 'date': date})
        MainFun()


if __name__ == '__main__':
    MainFun()
# try:
#     MainFun()
# except ValueError:
#     print('Спасибо, хорошего дня')
#     MainFun()