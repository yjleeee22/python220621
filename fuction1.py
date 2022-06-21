# fuction1
# 함수를 정의

def times(a,b):
    return a+b, a*b

# 함수 호출
# 디버깅할 때 중단(중단점)
result = times(3,4)
print(result)


# 참조를 복사 전달
def change(x):
    #복사본(Deep copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부 :", x1)

# 호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출 후:", wordlist)

# 교집합 함수(디버깅 연습)
def intersect(prelist, postlist):
    # 지역변수로 교집합 문자 저장
    result = []
    #H(0)  |  A(1)  | M(2)
    for x in prelist:
        # x라는 글자가 postlist에 포함, 그리고 x가 아직 result에 없다
        if x in postlist and x not in result:
            result.append(x)
    return result

# 함수 호출
print(intersect("HAM", "SPAM"))    

#연습
def func2(a):
    x=2
    return a+x

print(func2(1))

def times(a=10,b=10):
    return a*b

print(times())
print(times(45))

#키워드 인자 (파라미터 명시)

def connectURI(server,port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("credu.com","8080"))
print(connectURI(port="5050", server="credu.com"))

#가변인자 함수
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

# 정의되지 않은 인자(필수, 옵션)
def userURIBuilder(server,port,**user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

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