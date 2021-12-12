import os
import requests
import random
import urllib
import re
from bs4 import BeautifulSoup
from queue import Queue
import threading
import time
from datetime import datetime


'''
1 поток выводит статистику других потоков на экран

2 поток проверяет не скачилвали ли мы эту картинку раньше

группа потоков скачивания картинок скачивает картинки из очереди, 

и группа потоков парсит штмл страницы записиывает в очередь картинки и переходит по ссылкам рекурсивно.

запущел лишь один поток, и он запускает все отсальные.
не более 5 потоков скачивающих картинки, и не более 3 которые парсят.
'''

useragents = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    ]

headers = {
    'User-Agent': random.choice(useragents)
}

# Блокировки для общих данных
lock_links = threading.Lock()
lock_imgs = threading.Lock()

# Повторяющиеся ссылки и картинки
# passed_links = ['http://bgu.ru/', 'http://bgu.ru/mailto:priem@bgu.ru']
passed_links = ['http://bgu.ru/']
passed_imgs = []
my_path = 'Картинки/'

# Очереди
# Очереди сканируемых ссылок и скачиваемых картинок
q_imgs = Queue()
q_links = Queue()
q_links.put('http://bgu.ru/')
# Очередь сообщений в консоль
q_msgs = Queue()
q_msgs.put('Основной поток запущен')
# Очереди проверяемых на повтор ссылок и картинок
q_checked_imgs = Queue()
q_checked_links = Queue()

# Переменные для управления завершением программы
# Текущее время
time_for_exit = datetime.now()
semaphore_number = threading.Semaphore(12)
mutex_exit = threading.Semaphore()
mutex_warning_exit = threading.Semaphore()


# Получение значения семафора
def get_semaphore_val():
    return 'МЬЮТЕКСЫ -- ' + str(semaphore_number.__reduce__()[2].get('_value')) + '  '+ str(mutex_exit.__reduce__()[2].get('_value')) + '  '+ str(mutex_warning_exit.__reduce__()[2].get('_value'))


# Проверка глобального мьютекса для выхода потоков
def check_mutex(num):
    if mutex_exit.__reduce__()[2].get('_value') == 0:
        print('Поток закончил работу -- ' + str(num))
        # Завершение потока
        exit()
    else:
        if 4<=num<=6:
            pass
        #     print('Я ТАКОЙ-ТО -- ' + str(num))
        # time.sleep(1)


# Проверка глобального предупредительного мьютекса для выхода потоков
def check_warning_mutex():
    # Предупредительный флаг не опущен
    if mutex_warning_exit.acquire(blocking=False) is False:
        # Опускаем предупредительный флаг
        mutex_warning_exit.release()


# Проверка картинки
def check_img(barrier, num):
    q_msgs.put('Запуск {} потока проверки картинок'.format(num))
    barrier.wait()
    while True:
        # Очередь не пустая
        if not q_checked_imgs.empty():
            # Вызов проверки предупредительного мьютекса
            check_warning_mutex()
            # Блокирующаяся очередь, во избежании коллизий
            img = q_checked_imgs.get(block=True)

            if img not in passed_imgs:
                passed_imgs.append(str(img))
                if len(re.findall(r'((jpg)|(jpeg)|(png))$', str(img))) != 0:
                    # Добавление в очередь картинок
                    q_imgs.put(img)
        check_mutex(num)


# Проверка ссылок
def check_link(barrier, num):
    q_msgs.put('Запуск {} потока проверки ссылок'.format(num))
    barrier.wait()
    while True:
        # Очередь не пустая
        if not q_checked_links.empty():
            # Вызов проверки предупредительного мьютекса
            check_warning_mutex()
            # Блокирующаяся очередь, во избежании коллизий
            link = q_checked_links.get(block=True)
            if link not in passed_links:
                passed_links.append(str(link))
                if len(re.findall(r'((mailto:))|(tel:)', str(link))) == 0:
                    # Добавление в очередь ссылок
                    q_links.put(link)
        check_mutex(num)


# Скачивание картинок, картинки берутся из очереди q_imgs
def save_img(barrier, num):
    q_msgs.put('Запуск {} потока сканирования картинок'.format(num))
    # q_msgs.put('Запуск {} потока сканирования картинок'.format(threading.current_thread().getName()))
    barrier.wait()
    while True:
        # Очередь не пустая
        if not q_imgs.empty():
            # Вызов проверки предупредительного мьютекса
            check_warning_mutex()
        img=''
        # time.sleep(1)
        # print(threading.current_thread().getName())
        # print('ТОТАЛ СЕМАФОРА = ' + str(semaphore.__reduce__()[2].get('_value')) + '\n')
        # Блокировка на доступ к общим данным разными потоками
        with lock_imgs:
            # Очередь не пустая
            if not q_imgs.empty():
                # Вызов проверки предупредительного мьютекса
                check_warning_mutex()


                # Блокирующаяся очередь, во избежании коллизий q_imgs.get(block=True)
                img = q_imgs.get(block=True)

        if img != '':
            # Вставка сообщения в очередь
            q_msgs.put('Загружается картинка: ' + str(img))
            try:
                urllib.request.urlretrieve(img, os.path.join(my_path, os.path.basename(img)))
            except Exception:
                pass

        # Устанавливаем время последнего скачивания
        # global time_for_exit
        # time_for_exit = datetime.now()

        check_mutex(num)


# Поиск ссылок и картинок, заполнение очередей для проверки ссылок и картинок
def collect_links(barrier, num):
    q_msgs.put('Запуск {} потока сканирования ссылок'.format(num))
    # q_msgs.put('Запуск {} потока сканирования ссылок'.format(threading.current_thread().getName()))
    barrier.wait()
    while True:
        if not q_links.empty():

            check_warning_mutex()
        # print('QQQ ---- '+str(num))

        # time.sleep(1)
        # Блокировка на доступ к общим данным разными потоками
        with lock_links:
            # Очередь не пустая
            if not q_links.empty():
                # print('WWW ---- '+str(num))
                # print('начало  '+str(q_links.__reduce__()[2].get('queue')))
                # print(get_semaphore_val())
                # Вызов проверки предупредительного мьютекса
                check_warning_mutex()
                # print('EEE ---- '+str(num))
                if mutex_warning_exit.acquire(blocking=False) is False:
                    pass

                # print('RRR ---- '+str(num))
                # print('середина1  ' + str(q_links.__reduce__()[2].get('queue')))
                # print(get_semaphore_val())
                # Блокирующаяся очередь, во избежании коллизий
                link = q_links.get(block=True)
                # print('TTT ---- '+str(num))

        try:
            soup = BeautifulSoup()
            href = ''
            # print('YYY ---- '+str(num))
            soup = BeautifulSoup(requests.get(url=link, headers=headers).text, 'html.parser')
            # print('UUU ---- '+str(num))
        except Exception:
            pass
        # Получение ссылок и картинок на этой странице
        # links=[]
        # print('III ---- '+str(num))
        links = soup.findAll("a", limit=5)
        # print('OOO ---- '+str(num))
        imgs = soup.findAll("img")
        # print('PPP ---- '+str(num))


        for img in imgs:
            # print('AAA ---- '+str(num))
            # print('середина2   ' + str(q_links.__reduce__()[2].get('queue')))
            # print(get_semaphore_val())
            img = img['src']
            if not re.match(r'^(http:)', str(img)):
                img = 'http://bgu.ru/' + str(img)
            # print('SSS')
            # Добавление в очередь картинок на проверку
            q_checked_imgs.put(img)
            # print('DDD ---- '+str(num))

        for link in links:
            # print('FFF ---- '+str(num))
            # print('середина3   ' + str(q_links.__reduce__()[2].get('queue')))
            # print(get_semaphore_val())
            try:
                # print('GGG ---- '+str(num))
                href = link.get('href')
            except:
                pass
            if not re.match(r'^(http:)', str(href)):
                href = 'http://bgu.ru/' + str(href)
            # print('HHH ---- '+str(num))
            # Добавление в очередь ссылок на проверку
            q_checked_links.put(href)
            # print('JJJ ---- '+str(num))
            # print('очередь на проверку   ' + str(q_checked_links.__reduce__()[2].get('queue')))
            # print(get_semaphore_val())
    # print('KKK -------- '+ str(mutex_exit.__reduce__()[2].get('_value')))

        if mutex_exit.__reduce__()[2].get('_value') == 0:
            pass
        # print('конец  ' + str(q_links.__reduce__()[2].get('queue')))
        # print('значение mutex_exit !!!!!!!!!!!! -- ' + str(mutex_exit.__reduce__()[2].get('_value')))
    # print('LLL ---- ' + str(num))
        check_mutex(num)


# Печать статистики
def print_stat(barrier, num):
    q_msgs.put('Запуск {} потока печати статистики'.format(num))
    barrier.wait()
    while True:
        # print('очередь на СТАТИСТИКУ   ' + str(q_msgs.__reduce__()[2].get('queue')))
        # Очередь не пустая
        if not q_msgs.empty():
            # Вызов проверки предупредительного мьютекса
            check_warning_mutex()
            print(q_msgs.get())
        check_mutex(num)


# Проверка условий выхода из программы и установка глобального мьютекса
def exit_program(barrier, num):
    q_msgs.put('Запуск {} потока выхода из программы'.format(num))
    barrier.wait()
    while True:
        # Очереди пустые
        if q_imgs.empty() and q_links.empty() and q_msgs.empty():

            # Поднимаем предупредительный флажок - мьютекс (установка 0)
            mutex_warning_exit.acquire(blocking=False)
            # Даем время другим потокам опустить флажок
            time.sleep(5)
            # Если никто не опустил предупредительный флажок, то поднимамем основной флаг выхода всех потоков
            if mutex_warning_exit.acquire(blocking=False) is False:
                # Установка 0 на основной мьютекс
                mutex_exit.acquire()
                print('ТОТАЛ МЬЮТЕКСА = ' + str(mutex_exit.__reduce__()[2].get('_value')) + '\n')
                print('Поток закончил работу -- ' + str(num))
                exit()
        time.sleep(5)


# Входная функция
def main():
    q_num = Queue()
    for i in range(12):
        q_num.put(i)

    barrier = threading.Barrier(4)
    # Поток печати статистики
    th_print = threading.Thread(target=print_stat, args=(barrier, q_num.get(block=False)))
    th_print.start()

    # Поток проверки ссылок
    th_check_link = threading.Thread(target=check_link, args=(barrier, q_num.get(block=False)))
    th_check_link.start()

    # Поток проверки картинок
    th_check_img = threading.Thread(target=check_img, args=(barrier, q_num.get(block=False)))
    th_check_img.start()
    # th_print.join()

    # Поток выхода из программы
    th_exit = threading.Thread(target=exit_program, args=(barrier, q_num.get(block=False)))
    th_exit.start()

    # Потоки сканирования ссылок
    barrier_collect_links = threading.Barrier(3)
    for i in range(5,8):
        # q_msgs.put('Запуск {} потока сканирования ссылок'.format(str(i)))

        th_collect_links = threading.Thread(target=collect_links, args=(barrier_collect_links, q_num.get(block=False)))
        th_collect_links.start()
        # q_msgs.put('Запуск {} потока сканирования ссылок'.format(str(i)))

    # Потоки закачки картинок
    barrier_save_img = threading.Barrier(5)
    for i in range(8,13):
        # q_msgs.put('Запуск {} потока скачивания картинок'.format(str(i)))

        th_save_img = threading.Thread(target=save_img, args=(barrier_save_img, q_num.get(block=False)))
        th_save_img.start()

    exit()


print('dd')
main()
print('aaa')