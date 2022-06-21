# demoloop.py
# 반복구문

value = 5
while value > 0:
    print(value)
    value -= 1

print("--- 반복종료 ---")

#순회가능한 형식(시퀀스 형식)
for item in [1,2,3]:
    print(item)

print(bool(True))
print(bool(()))

lst=["apple",100,3.14]
for item in lst:
    print(item,type(item))

lst2=[1,2,3,4,5,6,7,8,9,19]
for item in lst2:
    if item>5:
        break
    print("Item:{0}".format(item))

lst3=list(range(20))
for item in lst3:
    if item %2==0:
        continue
    print("Item:{0}".format(item))

# 구구단 출력
for x in [2,3,4,5,6]:
    print("---{0}단 출력---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x,y,x*y))


print("---break---")
lst4 = list(range(1,11))
print(lst4)
for i in lst4:
    if i > 5: 
        break
    print("Item:{0}".format(i))

print("---continue---")
for i in lst4:
    # %는 나머지 값
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))


years = list(range(2000,2023))
print(years)
days = list(range(1,32))
print(days)

#리스트 컴프리헨션(리스트 임베딩)
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

#tuple에 담은 데이터
tp = ("apple", "orange juice", "kiwi")
print([len(i) for i in tp])

d = {100:"apple", 200:"banana", 300:"orange"}
[v.upper() for v in d.values()]

#필터링하는 함수
lst = [10,25,30]
iterL = filter(None,lst)
for item in iterL:
    print(item)

print("---필터링---")
def getBiggerThan20(i):
    return i >20

iterL = filter(getBiggerThan20,lst)
for item in iterL:
    print(item)

print("---람다함수---")

iterL = filter(lambda x:x>20,lst)
for item in iterL:
    print(item)