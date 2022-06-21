# 호출
print(userURIBuilder("credu.com","80", id="kim", passwd="1234"))
print(userURIBuilder("credu.com","80", id="kim", passwd="1234",
    name="mike"))

#람다 함수(간결한 함수 정의)
g= lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())