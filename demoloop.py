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
