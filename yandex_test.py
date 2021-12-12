# Программирование

# 1 (A)
n = int(input())
a = [int(i) for i in input().split()]
a1=sorted(a)
if a == a1:
    print('ok')

# [x.get_dict() for x in q_list]
# v= list(lambda i: a[i], len(a))
    res=0
    for i in range(n):
        # res += a[i] - a[i-1]
        res += a[n-1] - a[i]
    print(res)

else:
    print(-1)


# новый вариант
# 1 (A)
n=int(input())
a=[int(i) for i in input().split()]
a1=sorted(a)
if a==a1:
    print(a[n-1]-a[0])
else:
    print(-1)


# 2 (B)
def oc_position(choosen, oc, seats, rows): # Занять места

    with open('output.txt', 'a') as f:
        taken = []
        for seat in oc:
            taken.append("%s%s" % (choosen, seat))

        f.write("Passengers can take seats: %s\n" % " ".join(taken))

        for num in rows:
            for seat in ("A", "B", "C", "D", "E", "F"):
                if num != choosen:
                    f.write (seats[num][seat]['o'])
                else:
                    if seat in oc:
                        f.write("X")
                        seats[num][seat]['o'] = "#"
                    else:
                        f.write(seats[num][seat]['o'])
                if seat == "C":
                    f.write("_")
            f.write ("\n")
    return seats

def no_position():
    with open('output.txt', 'a') as f:
        f.write ("Cannot fulfill passengers requirements\n")

with open('input.txt') as f:
    content = [line.rstrip() for line in f]

n = int(content[0])
m = int(content[n+1])

seats = {}

for s in range(1, n+1):
    num = int(s)
    seats[num] = {}
    seats[num]['A'] = {"o": content[s][0], "s": "left", "t": "window" }
    seats[num]['B'] = {"o": content[s][1], "s": "left", "t": "" }
    seats[num]['C'] = {"o": content[s][2], "s": "left", "t": "aisle" }
    seats[num]['D'] = {"o": content[s][4], "s": "right", "t": "aisle" }
    seats[num]['E'] = {"o": content[s][5], "s": "right", "t": "" }
    seats[num]['F'] = {"o": content[s][6], "s": "right", "t": "window" }

rows = sorted(seats.keys())

left = ("A", "B", "C")
right = ("D", "E", "F")

output = []

for s in range(n+2, len(content)):
    flag_found = False
    g = content[s].split()
    ng = int(g[0])
    side = g[1]
    pref = g[2]
    # Ищем сначала свободные места
    for num in rows:
        if flag_found:
            break
        is_props = False
        count = 0
        oc = []
        i = 0

        array = right
        if side =="left":
            array = left

        while i < 3:
            if seats[num][array[i]]['o'] == '.':
                count += 1
                oc.append(array[i])
                if seats[num][array[i]]['t'] == pref:
                    is_props = True
                if count == ng:
                    if is_props: # Нашли подходящее место
                        seats = oc_position(num, oc, seats, rows)
                        flag_found = True
                        break
                    else: # Ищем дальше
                        count = 0
                        oc = []
                        if ng > 1:
                            i -= 1
            elif ng > 1 and i >= 1: # Разрыв между пассажирами, не подходит
                i = 2

            i += 1

    if not flag_found:
        no_position()


# 3 (C)
nk=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
d=[]
for i in range(nk[0]):
    j= [int(x) for x in range(nk[0]) if x!=i]
    d.append(str(sum(sorted([abs(a[i] - a[e]) for e in j])[:nk[1]])))
print(' '.join(d))

# новый вариант
# 3 (C)
nk=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

d=''
for i in range(nk[0]):
    j= [int(x) for x in range(nk[0]) if x!=i]
    d+=str(sum(sorted([abs(a[i] - a[e]) for e in j])[:nk[1]]))+' '
print(d.rstrip())


# 6 (F)
with open('input.txt') as f: # Читаем файл
    content = [line.rstrip() for line in f]
    content = list(reversed(content))

n = int(content[len(content)-1]) # Первая строка

days = []
sq_old = set()
for i in range(0, n): # Читаем все координаты
    c = content[i].split()

    sq = set()
    x1 = int(c[0])
    y1 = int(c[1])
    x2 = int(c[2])
    y2 = int(c[3])

    x   = x1
    while x < x2:
        y = y1
        while y < y2:
            sq.add("%s_%s" % (x, y))
            y += 1
        x += 1

    days.append(len(sq.difference(sq_old)))
    sq_old.update(sq)

with open('output.txt', 'w') as f:
    for d in reversed(days):
        #print (d)
        f.write(str(d)+"\n")

# новый вариант
# 6 (F)

sq = {}

with open('input.txt') as f: # Читаем файл
    a = 0
    for line in f:
        if a == 0:
            n = int(line.rstrip())
        else:
            c = line.rstrip().split()

            x1 = int(c[0])
            y1 = int(c[1])
            x2 = int(c[2])
            y2 = int(c[3])

            x = x1
            while x < x2:
                y = y1
                while y < y2:
                    sq["%s_%s" % (x, y)] = a
                    y += 1
                x += 1

        a += 1

l=list(sq.values())

with open('output.txt', 'w') as f:
    for s in range(1, n + 1):
        f.write(str(l.count(s))+"\n")

# 6 (F)
days = {}
sq = {}

with open('input.txt') as f:
    a = 0
    for line in f:
        if a == 0:
            n = int(line.rstrip())
        else:
            days[a] = 0
            c = line.rstrip().split()

            x1 = int(c[0])
            y1 = int(c[1])
            x2 = int(c[2])
            y2 = int(c[3])

            x = x1
            while x < x2:
                y = y1
                while y < y2:
                    sq["%s_%s" % (x, y)] = a
                    y += 1
                x += 1
        a += 1

print(sq)
for s in sq:
    days[sq[s]] += 1

with open('output.txt', 'w') as f:
    for d in days:
        f.write(str(days[d]) + "\n")



# Аналитика

# А
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
                # print('разность = '+str(day1-day2))
            choice1 =choice12
            choice2 = choice22

    # print(date_mass)
    a.append(numpy.mean(date_mass))
    print(numpy.mean(date_mass))

print(numpy.mean(a))


# D
with open('input.txt') as f: # Читаем файл
    content = [line.rstrip() for line in f]

(n, m) = content[0].split()

m = int(m)
n = int(n)

i = 0
matches = []

while i < 2 * m: # Читаем все матчи
    i += 1
    (a, b) = content[i].split()
    a_res = int(a) - int(b)
    b_res = int(b) - int(a)
    i += 1
    array = content[i].split()
    workers = {}
    for j, id in enumerate(array):
        if id not in workers:
            workers[id] = 0
        if j > 4:
            workers[id] += b_res
        else:
            workers[id] += a_res

    count = 0
    for id in workers:
        if workers[id] > workers['0']:
            count += 1
    matches.append(count)

with open('output.txt', 'w') as f:
    for match in matches:
        f.write(str(match)+"\n")


# E
from datetime import datetime

start_amount = 10000
start_date = int(datetime.strptime('2021-01-01 00:00:00', "%Y-%m-%d %H:%M:%S").timestamp())
end_date = int(datetime.strptime('2021-02-01 00:00:00', "%Y-%m-%d %H:%M:%S").timestamp())

answers = []
with open('input.txt') as f:
    remainder = start_amount
    for line in f:
        line = line.rstrip()
        (d, t, s) = line.split()
        timestamp = int(datetime.strptime(d + ' ' + t, "%Y-%m-%d %H:%M:%S").timestamp()) + 1
        s = int(s)
        remainder -= s
        speed = (start_amount - remainder) / ((timestamp - start_date) / 60)
        answer = round(remainder - ((end_date - timestamp) / 60) * speed, 2)
        print(answer)
        answers.append(format(answer, '.2f'))

with open('output.txt', 'w') as f:
    for a in answers:
        f.write(a+"\n")
