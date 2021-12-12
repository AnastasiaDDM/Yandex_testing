# a='qweeqq'
# b='wqe'
# from counter import Counter
import collections

# def count():
    # ar_a = collections.Counter(a)
    # ar_b = collections.Counter(b)
    # print(ar_a)
    # print(ar_b)
    # if ar_a == ar_b:
    #     return True
    # return False
    # dict_a={}
    #
    # for i in a:
    #     if i in dict_a:
    #         dict_a[i] += 1
    #     else:
    #         dict_a[i] = 1
    # print(dict_a)
# print(count())

# n=2
# def gen(cur, open, close, n):
#
#     if len(cur)==2*n:
#         print(cur)
#         return True
#     if open < n:
#         gen(cur+'(', open+1, close, n)
#     if close < open:
#         gen(cur+')', open, close+1, n)
# gen('', 0, 0, n)


'''
 1 задача
 Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями». Проще говоря, нужно проверить, какое количество символов из S входит в J.
'''
a=[int(i) for i in input().split()]
j = list(input())
s = list(input())

count = 0
for i in s:
    if i in j:
        count +=1
print(count)


'''
2 задача
Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.
Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.
'''
data = []
with open('input.txt') as file:
    [data.append(int(i)) for i in file]

n = data[0]
cur = 0
result=0
for el in range(1,n+1):
    print(data[el])
    if data[el]>0:
        cur = cur + 1
        result = max(result, cur)
        # array_repeat[8]=1
    else:
        # array_repeat.append(cur)
        cur =0
with open('output.txt', 'w') as file:
    file.write(str(result))
print(data)


'''
3 задача
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.
Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный объем памяти в процессе работы.
!!!Формат ввода!!!
Первая строка входного файла содержит единственное число n, n ≤ 1000000.
На следующих n строк расположены числа — элементы массива, по одному на строку. Числа отсортированы по неубыванию.
'''
with open('input.txt') as f:
    a=0
    prev = 0
    res=[]
    for line in f:
        if a == 0:
            n = int(line.rstrip())
            a = 1
        else:
            next = int(line.rstrip())
            if prev != next:
                res.append(str(next))
            prev = next
with open('output.txt', 'w') as f:
    f.write('\n'.join(res))


'''
4 задача
Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, упорядоченные лексикографически
В задаче используются только круглые скобки.
Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.
!!!Формат вывода!!!
Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.
'''
n = int(input())
def generate(cur, open, close):
    if len(cur) == 2*n:
        print(cur)
        # return 1
    if open < n:
        generate(cur+'(', open+1, close)
    if open > close:
        generate(cur+')', open, close+1)
generate('', 0, 0)


'''
5 задача
Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами, т. е. отличаются ли они только порядком следования символов.
Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами, т. е. отличаются ли они только порядком следования символов.
!!!Формат ввода!!!
Входной файл содержит две строки строчных латинских символов, каждая не длиннее 100 000 символов. Строки разделяются символом перевода строки.
!!!Формат вывода!!!
Выходной файл должен содержать единицу, если строки являются анаграммами, и ноль в противном случае.
'''
str_1=input()
str_2=input()

def generate(line):
    dict_count={}
    for i in line:
        if i in dict_count:
            dict_count[i]+=1
        else:
            dict_count[i] =1
    return dict_count

res=0
if len(str_1) == len(str_2):
    if generate(str_1)==generate(str_2):
        res =1
print(res)
