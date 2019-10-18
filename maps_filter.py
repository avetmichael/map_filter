#281
arr = [0, 1, -2, -3, 4, 0, -5, 6, 7, -8, 13]
res = list(filter(lambda b: b > 0, arr))
res = list(map(lambda b: b, res))
print(res)

#282
res1 = list(filter(lambda b: b != 0, arr))
res1 = list(map(lambda b: b, res1))
print(res1)

#283
res2 = list(filter(lambda b: b % 2 == 1, arr))
res2 = list(map(lambda b: b, res2))
print(res2)

#284
a = int(input("mutqagreq a: "))
c = int(input("mutqagreq c: "))
res3 = list(filter(lambda b: a <= b and b <= c, arr))
res3 = list(map(lambda b: b, res3))
print(res3)

#285
p = int(input("mutqagreq p: "))
res4 = list(filter(lambda b: b % p == 0, arr))
res4 = list(map(lambda b: b, res4))
print(res4)

#286
res5 = list(filter(lambda b: b % 2 == 0, arr))
res5 = list(map(lambda b: b, res5))
print(res5)

#290
res6 = list(filter(lambda b: b % 6 == 1, arr))
res6 = list(map(lambda b: b, res6))
print(res6)