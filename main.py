#!/usr/bin/env python3
# Money Flow Manager by CISCer Beta for Linux v0.1.3
import csv
import os
import datetime
import time


def Clear():
    os.system("clear")


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
            print('\n', green,
                  '1', mc, '- View details''\n', green,
                  '2', mc, '- Add operation')
            change = input('(1/2): ')
            if change == '-x':
                Clear()
                print('10Q, have a good day')
                quit()
            if change == '1':
                num = int(input('Number: '))
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
                            print('\n', 'At the moment', yellow, line["date"], mc,
                                  'on account', cl_b, line["balance"], mc, '₽', '\n\n',
                                  'The income was', cl_i, line["income"], mc, '₽', '\n',
                                  'Note to income:', yellow, line["note_income"], mc, '\n\n',
                                  'The consumption was', cl_c, line["consumption"], '₽', mc, '\n',
                                  'Note to consumption:', yellow, line["note_consumption"], '\n', mc)

            elif change == '2':
                with open(file_data_base, 'a', encoding='utf-8') as data:
                    date = time_now
                    fieldnames = ['balance', 'income', 'consumption', 'date', 'note_income', 'note_consumption']
                    writer = csv.DictWriter(data, fieldnames=fieldnames)

                    income = int(input('Доход: '))
                    note_income = input('Примечание к доходу: ')
                    consumption = int(input('Расход: '))
                    note_consumption = input('Примечание к расходу: ')
                    with open(file_data_base, encoding='utf-8') as read_data:
                        reading_lines = csv.DictReader(read_data, delimiter=',')
                        for row in reading_lines:
                            last_balance = int(row["balance"])
                    balance = last_balance + int(income) - int(consumption)

                    writer.writerow({'balance': balance,
                                     'income': income,
                                     'consumption': consumption,
                                     'date': date,
                                     'note_income': note_income,
                                     'note_consumption': note_consumption})
    # Запись
    elif check_file_data_base == False:
        with open(file_data_base, mode="a", encoding='utf-8') as data:
            date = time_now
            fieldnames = ['balance', 'income', 'consumption', 'date', 'note_income', 'note_consumption']
            writer = csv.DictWriter(data, fieldnames=fieldnames)
            writer.writeheader()

            balance = int(input('Balance: '))

            writer.writerow({'balance': balance, 'income': 0, 'consumption': 0, 'date': date})
        MainFun()


if __name__ == '__main__':
    Clear()
    print(blue, 'Money Flow Program v0.1.3 Beta\nby CISCer', mc)
    time.sleep(1)
    Clear()
    try:
        MainFun()
    except ValueError:
        print('10Q, have a good day')
        time.sleep(2)
        MainFun()
