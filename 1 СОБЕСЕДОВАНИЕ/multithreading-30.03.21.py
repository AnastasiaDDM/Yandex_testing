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
semaphore = threading.Semaphore(5)
mutex_exit = threading.Semaphore()
mutex_warning_exit = threading.Semaphore()

# Проверка глобального мьютекса для выхода потоков
def check_mutex():
    if mutex_exit.__reduce__()[2].get('_value') == 0:
        print('Поток закончил работу -- ' + threading.current_thread().getName())
        # Завершение потока
        exit()


# Проверка картинки
def check_img(barrier):
    while True:
        # Очередь не пустая
        if not q_checked_imgs.empty():
            # Блокирующаяся очередь, во избежании коллизий
            img = q_checked_imgs.get(block=True)

            if img not in passed_imgs:
                passed_imgs.append(str(img))
                if len(re.findall(r'((jpg)|(jpeg)|(png))$', str(img))) != 0:
                    # Добавление в очередь картинок
                    q_imgs.put(img)
        check_mutex()


# Проверка ссылок
def check_link(barrier):
    while True:
        # Очередь не пустая
        if not q_checked_links.empty():
            # Блокирующаяся очередь, во избежании коллизий
            link = q_checked_links.get(block=True)
            if link not in passed_links:
                passed_links.append(str(link))
                if len(re.findall(r'(^(mailto:))|(tel:)', str(link))) == 0:
                    # Добавление в очередь ссылок
                    q_links.put(link)
        check_mutex()


# Скачивание картинок, картинки берутся из очереди q_imgs
def save_img(barrier):
    while True:
        # print(threading.current_thread().getName())
        # print('ТОТАЛ СЕМАФОРА = ' + str(semaphore.__reduce__()[2].get('_value')) + '\n')

        # Очередь не пустая
        if not q_imgs.empty():

            # Занимаем место, уменьшаем значеине семафора на 1
            # ЕГО Я НЕ ИСПОЛЬЗУЮ! НО, ВЕРОЯТНО, МОЖНО ПОПРОБОВАТЬ УПРАВЛЯТЬ ВЫХОДОМ ИЗ ПРОГРАММЫ ИМ!
            semaphore.acquire()
            # print('уменьшаем = '+str(semaphore.__reduce__()[2].get('_value'))+'\n')

            # Блокировка на доступ к общим данным разными потоками
            with lock_imgs:
                # Блокирующаяся очередь, во избежании коллизий q_imgs.get(block=True)
                img = q_imgs.get(block=True)

            # Вставка сообщения в очередь
            q_msgs.put('Загружается картинка: ' + str(img))

            urllib.request.urlretrieve(img, os.path.join(my_path, os.path.basename(img)))

            # Освобождаем место, увеличиваем значеине семафора на 1
            # ЕГО Я НЕ ИСПОЛЬЗУЮ! НО, ВЕРОЯТНО, МОЖНО ПОПРОБОВАТЬ УПРАВЛЯТЬ ВЫХОДОМ ИЗ ПРОГРАММЫ ИМ!
            semaphore.release()
            # Устанавливаем время последнего скачивания
            global time_for_exit
            time_for_exit = datetime.now()
            # print('увеличиваем = '+str(semaphore.__reduce__()[2].get('_value'))+'\n')
        check_mutex()


# Поиск ссылок и картинок, заполнение очередей для проверки ссылок и картинок
def collect_links(barrier):

    while True:

        # Очередь не пустая
        if not q_links.empty():

            # Блокировка на доступ к общим данным разными потоками
            with lock_links:
                # Блокирующаяся очередь, во избежании коллизий
                link = q_links.get(block=True)

            soup = BeautifulSoup(requests.get(url=link, headers=headers).text, 'html.parser')

            # Получение ссылок и картинок на этой странице
            links = soup.findAll("a", limit=1)
            imgs = soup.findAll("img")

            for img in imgs:
                img = img['src']
                if not re.match(r'^(http:)', str(img)):
                    img = 'http://bgu.ru/' + str(img)

                # Добавление в очередь картинок на проверку
                q_checked_imgs.put(img)

            for link in links:
                try:
                    href = link.get('href')
                except:
                    pass
                if not re.match(r'^(http:)', str(href)):
                    href = 'http://bgu.ru/' + str(href)

                # Добавление в очередь ссылок на проверку
                q_checked_links.put(href)

        check_mutex()


# Печать статистики
def print_stat(barrier):
    while True:
        # Очередь не пустая
        if not q_msgs.empty():
            print(q_msgs.get())
        check_mutex()


# Проверка условий выхода из программы и установка глобального мьютекса
def exit_program(barrier):
    while True:

        if (datetime.now() - time_for_exit).seconds > 5:
            # Установка 0 на мьютекс
            mutex_exit.acquire()
            print('ТОТАЛ МЬЮТЕКСА = ' + str(mutex_exit.__reduce__()[2].get('_value')) + '\n')
            print('Поток закончил работу -- ' + threading.current_thread().getName())
            exit()
        time.sleep(5)


# Входная функция
def main():

    barrier = threading.Barrier(4)
    # Поток печати статистики
    th_print = threading.Thread(target=print_stat, args=(barrier,))
    th_print.start()

    # Поток проверки ссылок
    th_check_link = threading.Thread(target=check_link, args=(barrier,))
    th_check_link.start()

    # Поток проверки картинок
    th_check_img = threading.Thread(target=check_img, args=(barrier,))
    th_check_img.start()
    # th_print.join()

    # Поток выхода из программы
    th_exit = threading.Thread(target=exit_program, args=(barrier,))
    th_exit.start()

    # Потоки сканирования ссылок
    barrier_collect_links = threading.Barrier(3)
    for i in range(5,8):
        q_msgs.put('Запуск {} потока сканирования ссылок'.format(str(i)))

        th_collect_links = threading.Thread(target=collect_links, args=(barrier_collect_links,))
        th_collect_links.start()

    # Потоки закачки картинок
    barrier_save_img = threading.Barrier(5)
    for i in range(8,13):
        q_msgs.put('Запуск {} потока скачивания картинок'.format(str(i)))

        th_save_img = threading.Thread(target=save_img, args=(barrier_save_img,))
        th_save_img.start()

    exit()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     q_msgs.put('Запуск 5 потоков скачивания картинок')
    #     executor.map(save_img, range(5))

    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     q_msgs.put('Запуск 3 потоков сканирования ссылок')
    #     executor.map(collect_links, range(5))


print('dd')
main()
print('aaa')