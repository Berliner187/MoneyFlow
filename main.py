#!/usr/bin/env python3
# Money Flow Manager by CISCer Beta for Linux v0.1.4
import csv
import os
import datetime
import time


def ClearTerminal():
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
    time_now = ":".join(time_format)
    date_now = str(date_format)
    return time_now, date_now


date_now, time_now = DateTime()

file_data_base = ".data.dat"
check_file_data_base = os.path.exists(file_data_base)


def Field():
    return ['balance', 'income', 'consumption', 'date', 'time', 'note_income', 'note_consumption', 'category']


def ShowingContent():
    ClearTerminal()
    with open(file_data_base, encoding='utf-8') as data_from_file:
        s = 0
        reader = csv.DictReader(data_from_file, delimiter=',')
        row_date_and_time = ("    Date", "Time", "Balance")
        print(yellow + '\n --- Все операции --- \n\n' + mc,
              "   >>>>  ".join(row_date_and_time))
        for line in reader:
            s += 1
            row = (line["date"], line["time"], line["balance"])
            if s < 10:
                print('0' + str(s) + '. ' + ' --> '.join(row))
            else:
                print(str(s) + '. ' + ' --> '.join(row))
            if s == 20:
                break


def SaveDataToFile(balance, income, consumption, date_now, time_now, note_income, note_consumption):
    with open(file_data_base, encoding='utf-8') as read_data:
        reading_lines = csv.DictReader(read_data, delimiter=',')
        for row in reading_lines:
            last_balance = int(row["balance"])
    if check_file_data_base == bool(True):
        balance = last_balance + int(income) - int(consumption)

    with open(file_data_base, 'a', encoding='utf-8') as data:
        writer = csv.DictWriter(data, fieldnames=Field())
        if check_file_data_base == bool(False):
            writer.writeheader()
        writer.writerow({'balance': balance,
                         'income': income,
                         'consumption': consumption,
                         'date': date_now,
                         'time': time_now,
                         'note_income': note_income,
                         'note_consumption': note_consumption})


def MainFun():
    # Reader
    if check_file_data_base == bool(True):
        # Если файл уже создан, выводтся содержимое и дальнейшее взаимодействие с программой происходит тут
        ShowingContent()

        while True:
            print('\n', green,
                  '1', mc, '- View details''\n', green,
                  '2', mc, '- Add operation')
            change = input('(1/2): ')
            if change == '-x':
                ClearTerminal()
                print('10Q, have a good day')
                quit()
            if change == '1':
                num = int(input('Number: '))
                ClearTerminal()
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

                print(green + '\n Income/Consumption - ?' + mc)
                change_income_or_consumption = input(' (1/2): ')
                if change_income_or_consumption == '1':
                    income = int(input(' Income: '))
                    note_income = input(' Note to income: ')
                    SaveDataToFile(0, income, 0, date_now, time_now, note_income, '')
                elif change_income_or_consumption == '2':
                    consumption = int(input('Consumption: '))
                    note_consumption = input('Note to consumption: ')
                    SaveDataToFile(0, 0, consumption, date_now, time_now, '', note_consumption)
                ShowingContent()
    # Запись
    elif check_file_data_base == bool(False):
        with open(file_data_base, mode="a", encoding='utf-8') as data:
            data.close()
            os.system("chmod +x main.py")

            balance = int(input('Balance: '))
            SaveDataToFile(balance, 0, 0, date_now, time_now, '', '')
        os.system('./main.py')


if __name__ == '__main__':
    ClearTerminal()
    print(blue, 'Money Flow Program v0.1.4 Beta \n by CISCer', mc)
    ClearTerminal()
    try:
        MainFun()
    except ValueError:
        print('#Error')
        time.sleep(2)
        MainFun()
