
a=[1,2,3,4,5,6]
b=[1,2]
# a = 12345
# print(a[1:6:2])
# print(divmod(10,3))


c='asdfg'
# print(c[1:60:2])
# print(type(repr(a)))

# print(10/3)
# print(10//3)

# print(10<100<1000)

d1={'a':1, 'b':2, 'c':3}
d2={'a':1, 'b':2, 'd':4}
d2={'c':3, 'a':1, 'b':2}
# print(d1==d2)
# print(sorted(d1.items())==sorted(d2.items()))
# print(d1!=d2)

# print(max(a))
# print(max(c))
# print(len(b))

# a=a[0:6:2]
# a=a[1::2]
# a=a[1::]
# a=a[-1::-1]
# a=a[::-1]
# print(a)
# print('aaa\naa')

# print('%s, %d, %.2f' % ('aa', 12.2, 20.1))
# print('{0:s}, {1:.0f}, {2:.2f}'.format('aa', 12.2, 20.1))
# print('aaa\r\naa'.split('\r\n'))
# print('+'.join(['q', 'w', 'e', 'r']))
# print('old+'.replace('+', '-'))
# print('aaa\r\naa'.splitlines())
# print('aaa\naa'.splitlines())
# print('   aaa  raa '.strip())
# print('aaa'.zfill(5))
# print(list('qwe'))
# print(list(x*2 for x in range(1,5)))
# print(list(x*2 for x in range(1,5)).index(4))
# d3 = dict(zip('qwe', [1,2,3,4]))
# print(d3)
# print(d3.items())

# Работа с файлами

# f = open('file.txt', 'r').readlines()
# print(f)
# f = [ x.splitlines()[0] for x in f]
# f = [ x.replace('\n', '') for x in f]
# print(f)
#
# with open('file.txt', 'a', encoding='utf8') as output_file:
#     output_file.write('2\n')


# a = [int(i) for i in input().split()]
# print(a)

#
# Яндекс
# f = open('input.txt', 'r').readline()
# a = [int(i) for i in f.split()]
# with open('output.txt', 'w', encoding='utf8') as output_file:
#     output_file.write(str(a[0]+a[1]))

# 1
# n = int(input())
# a = [int(i) for i in input().split()]
# # n = 5
# # a = [3,4,5,6,6]
# a1=sorted(a)
# if a == a1:
#     print('ok')
#
#     # print(x * 2 for x in range(1, 5))
#
# # [x.get_dict() for x in q_list]
# # for
# # v= list(lambda i: a[i], len(a))
#     res=0
#     #
#     for i in range(n):
#         # res += a[i] - a[i-1]
#         res += a[n-1] - a[i]
#     print(res)
#
# else:
#     print(-1)
# print(a)
# print(a1)




# новый
# 1
# n=int(input())
# a=[int(i) for i in input().split()]
# a1=sorted(a)
# if a==a1:
#     print(a[n-1]-a[0])
# else:
#     print(-1)




# 2
# n=int(input())
# a=[int(i) for i in input().split()]

nk=[4, 2]

a=[1,2,3,4]

# nk=[5, 3]
#
# a=[3,2,5,1,2]
#
# nk=[6, 2]
#
# a=[3,2,1,101,102,103]

# nk=[int(i) for i in input().split()]
# a=[int(i) for i in input().split()]
# d=[]
# for i in range(nk[0]):
#     j= [int(x) for x in range(nk[0]) if x!=i]
#     d.append(str(sum(sorted([abs(a[i] - a[e]) for e in j])[:nk[1]])))
# print(' '.join(d))




#
# nk=[int(i) for i in input().split()]
# a=[int(i) for i in input().split()]



# nk=[4, 2]
#
# a=[1,2,3,4]

# nk=[5, 3]
#
# a=[3,2,5,1,2]
#
# nk=[6, 2]
#
# a=[3,2,1,101,102,103]


# d=[]
# result=''
# s=range(nk[0])
# for i in s:
#     mass_diff=[]
#     for e in s:
#         if e!=i:
#             mass_diff.append(abs(a[i] - a[e]))
#
#     d.append(str(sum(sorted(mass_diff)[:nk[1]])))
#
#
# print(' '.join(d))

# nk=[int(i) for i in input().split()]
# a=[int(i) for i in input().split()]


# d=''
# for i in range(nk[0]):
#     j= [int(x) for x in range(nk[0]) if x!=i]
#     d+=str(sum(sorted([abs(a[i] - a[e]) for e in j])[:nk[1]]))+' '
# print(d.rstrip())





# 3









# 5 E




# new_list = []
# for element in a:
#     if element in b:
#         new_list.append(element)



# 6 F


def is_cross(a,b):
    ax1,ay1,ax2,ay2 = a[0],a[1],a[2],a[3]          # прямоугольник А
    bx1, by1, bx2, by2 = b[0], b[1], b[2], b[3]    # прямоугольник B
    # это были координаты точек диагонали по каждому прямоугольнику

    # 1. Проверить условия перекрытия, например, если XПA<XЛB ,
    #    то прямоугольники не пересекаются,и общая площадь равна нулю.
    #   (это случай, когда они справа и слева) и аналогично, если они сверху
    #    и снизу относительно друг друга.
    #    (XПА - это  Х Правой точки прямоугольника А)
    #    (ХЛВ - Х Левой точки прямоугольника В )
    #    нарисуй картинку (должно стать понятнее)

    xA = [ax1,ax2]  # координаты x обеих точек прямоугольника А
    xB = [bx1,bx2]  # координаты x обеих точке прямоугольника В

    yA = [ay1, ay2]  # координаты x обеих точек прямоугольника А
    yB = [by1, by2]  # координаты x обеих точек прямоугольника В

    if max(xA)<min(xB) or max(yA) < min(yB) or min(yA) > max(yB):
        return False    # не пересекаются

    # 2. Определить стороны прямоугольника образованного пересечением,
    # например,
    # если XПA>XЛB, а XЛA<XЛB, то ΔX=XПA−XЛB

    elif max(xA)>min(xB) and min(xA)<min(xB):
        dx = max(xA)-min(xB)
        return True     # пересекаются
    else:
        return False     # пересекаются


    # # 3. далее уже можно определить площадь, как произведение сторон:
    #      SAB=ΔX∗ΔY



#тесты



# result = is_cross([-1, -1, 0,0], [0, 0, 1, 1])
# print(result)

# result = is_cross([-1, 1, 0,0], [0, 0, 1, 1])
# print(result)




#result = is_cross([-5, 2, 3,-2], [2, 6, 5, 1])
#print(result, "test 1")  #True

#result = is_cross([1, 4, 6, 1], [5, 5, 7, 3])
#print(result, "test 2")  #True

#result = is_cross([5, 5, 7, 3], [1, 4, 6, 1])
#print(result, "test 3")   #True

#result = is_cross([-2, 3, 0, -2], [0, -2, 2, -4])
#print(result, "test 4")   #True

#result = is_cross([0, -2, 2, -4], [-2, 3, 0, -2])
#print(result, "test 5")   #True

#result = is_cross([2, 5, 6, 1], [3, 4, 5, 2])
#print(result, "test 6")   #True

#result = is_cross([3, 4, 5, 2], [2, 5, 6, 1])
#print(result, "test 7")   #True

#result = is_cross([1, 4, 4, 2], [1, 1, 4, -1])
#print(result, "test 8")   #True

#result = is_cross([1, 1, 4, -1], [1, 4, 4, 2])
#print(result, "test 9")   #False

#result = is_cross([-5, 1, 5, -1], [-1, 5, 1, -5])
#print(result, "test 11")   #True



# content=[]
# with open('input.txt') as file:
#     for line in file:
#         content.append([int(element) for element in line.split()])
#
#     # a = [int(i) for i in input().split()]
#
# # print(content)
# # print(content[0][0])
# n = int(content[0][0])
#
#
# # n=3
# a1=[-1,-1,1,1]
# a2=[-1,0,1,1]
# res_dict={}
# res_list=[]
# d=[]
# # print(list(range(-1,1,1)))
#
# for s in range(1, n+1):
#     # print(content[s])
#     k=0
#     for i in range(content[s][0],content[s][2],1):
#         # print(i)
#         for j in range(content[s][1],content[s][3], 1):
#             # res_list.append(s)
#             res_dict[i,j]=s
#             # k+=1
#         # res_dict[s] = k
#
#
# print(res_dict)
# # print(res_list)
#
#
# l=list(res_dict.values())
# print(l)
# for s in range(1, n+1):
#
#     # print(s)
#     # days[sq[s]] += 1
#     # d.append(str())
#     d.append(str(l.count(s)))
#     # res_list
#
#
# print(' '.join(d))

# print(res_dict)







# content=[]
# with open('input.txt') as file:
#     for line in file:
#         content.append([int(element) for element in line.split()])
#
# n = int(content[0][0])
# res_dict={}
# d=[]
#
# for s in range(1, n+1):
#     k=0
#     for i in range(content[s][0],content[s][2],1):
#         for j in range(content[s][1],content[s][3], 1):
#             res_dict[i,j]=s
#
# print(res_dict)
#
# l=list(res_dict.values())
# for s in range(1, n+1):
#     d.append(str(l.count(s)))
# res='\n'.join(d)
#
# with open('output.txt', 'w') as f:
#     f.write(res)




# days = {}
# sq = {}
#
# with open('input.txt') as f:
#     a = 0
#     for line in f:
#         if a == 0:
#             n = int(line.rstrip())
#         else:
#             days[a] = 0
#             c = line.rstrip().split()
#
#             x1 = int(c[0])
#             y1 = int(c[1])
#             x2 = int(c[2])
#             y2 = int(c[3])
#
#             x = x1
#             while x < x2:
#                 y = y1
#                 while y < y2:
#                     sq["%s_%s" % (x, y)] = a
#                     y += 1
#                 x += 1
#         a += 1
#
# print(sq)
# for s in sq:
#     days[sq[s]] += 1
#
# with open('output.txt', 'w') as f:
#     for d in days:
#         f.write(str(days[d]) + "\n")
#











# Аналитика

#
# import numpy as np
#
# n = 90
#
# probs = []
#
# for i in range(1, n + 1):  # Для каждого дня
#
#     prob_now = 1 / (i + 1)  # вычисляем вероятность успеха в этот день
#
#     prob_not_before = []
#
#     for k in range(1, i):  # И вероятность провала во все прошлые
#         prob_not_before.append(k / (k + 1))
#
#     prob_not_before = np.array(prob_not_before).prod()  # Перемножаем
#
#     probs.append(prob_not_before * prob_now)
#
# s = sum(probs)  # Считаем суммарную вероятность
#
# print(s)


# import math
# import numpy as np
# import sys
# import sympy  # Библиотека с числами Стирлинга - и такое есть
#
# sys.setrecursionlimit(10 ** 9)
#
#
# # def c(n, k):  # Cочетания
# #
# #     return (math.factorial(n)) / (math.factorial(k) * math.factorial(n - k))
#
#
# def c(n, k): # Подсчёт числа сочетаний, быстрый алгоритм без факториалов
#     if 0 <= k <= n:
#         nn = 1
#         kk = 1
#         for t in range(1, min(k, n - k) + 1):
#             nn *= n
#             kk *= t
#             n -= 1
#         return nn // kk
#     else:
#         return 0
#
#
# def s(n, k):  # Псевдоним для числа Стирлинга второго рода
#
#     return sympy.functions.combinatorial.numbers.stirling(n, k)
#
#
# def p(m, k, n):  # Вероятность рассмотреть ровно k
#
#     return float(c(m, k)) * float(math.factorial(k))* float(s(n, k)) / float((m ** n))
#
#
# pr = []
# # Тут я считаю не для долей, а для количества подарков...
# for n in range(2, 10):
#     print(n)
#     for j in range(1, 1001):
#         pr.append(p(1150, j, n))
#
#     pr = np.array(pr)
#     print(pr)
# # ...поэтому потом делю на 100
# # frac = np.array([i for i in range(1, 101)]) / 100
#
# # print(sum(pr * frac))  # Печатаем результат
#
#

import random
import numpy
a=[]
d1={}

date_mass=[]
for j in range(1, 5):


    for i in range(1, 5000000):
        choice1 = random.choice([0, 1])
        choice2 = random.choice([0, 1])
        # print('choice1 = '+str(choice1))
        # print('choice2 = '+str(choice2))

        day1=None
        day2 = None
        day_count = 1
        f1 = False
        while f1 is False:

            f1=False
            f2 = False
            choice12 = random.choice([0, 1])
            choice22 = random.choice([0, 1])
            day_count += 1
            # print('choice12 = '+str(choice12))
            # print('choice22 = '+str(choice22))
            # Успех у первого
            if day1 is None and choice1==choice12==1:
                # f1=True
                day1=day_count
                # print('choice1==choice12==1' + str(day1))
            # Успех у второго
            if day2 is None and choice2==0 and choice22==1:
                day2 = day_count
                # print('choice2==0 and choice22==1' + str(day2))

            if day1 and day2:
                f1 = True
                date_mass.append(day1-day2)
                # print('          разность = '+str(day1-day2))
            choice1 =choice12
            choice2 = choice22


    # print(date_mass)
    a.append(numpy.mean(date_mass))
    print(numpy.mean(date_mass))

print(numpy.mean(a))