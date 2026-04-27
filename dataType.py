#dataType.py
# 리스트, 튜플
# 리스트 - 여러가지 데이터를 저장 관리 하기 위해 파이썬 자료구조이다.
# 튜플도 리스트와 같은데 차이점은 리스트는 수정이 가능하지만
# 튜플은 수정이 불가능하다.

# 리스트 - 순서유지, 인덱스를 통해 접근, 추가,수정,삭제가능
# 다른 자료형도 저장가능
number = [ 10,20,30,40,50 ]
empty = []
name = list()

print( number[0] )
print( number[-2] ) # 뒤에서 부터 시작 10(0), 50(-1), 40(-2)

# 리스트 자르기
num = number[2:4] # 2번 index 부터 4번 index 전까지
print(num)
num2 = number[:3] # 시작부터 3번 index 전까지
print(num2)
num3 = number[2:] # 2번 index 부터 끝까지
print(num3)

# 리스트 수정
number[2] =100
print(number)

# 리스트 추가
number.append(60) # 리스트의 마지막에 추가
print(number)

number.insert(2,500) #리스트에 원하는 위치에 추가(인덱스, 값)
print(number)

#리스트 값 삭제
number.remove(100) #리스트에서 삭제할 데이터 입력
print(number)
number.pop(1) #리스트에서 삭제할 데이터의 인덱스 입력
print(number)
del number[2] #인덱스로 삭제
print(number)

# #리스트 크기(길이)
# print(len(number))

# for num in number:
#     print(num)

# for i , num in enumerate(number):
#     print( i, num )

# #리스트 검색
# print( 40 in number ) #값의 존재여부 True, False
# print( number.index(55) ) #인덱스 찾기 - 없으면 오류
# # index를 통해 인덱스를 찾기 전에 in으로 존재여부 확인 먼저 하기

# #리스트 정렬
# number.sort() #기본 정렬은 오름차순이다.
# print(number)
# number.sort(reverse=True)
# print( number )

# 리스트는 일반적으로 많이 사용되는 자료구조이다.
# 자바에서 List (ArrayList)를 많이 사용 된다면 파이썬은 리스트이다.
# 여러 데이터를 저장할수 있고, 수정, 추가 가능하고 반복문 사용 쉽고
# 정렬, 검색도 되고 그래서 사용하기 좋은 녀석이다.

#리스트 문제 풀기!!!!!!!!!!!!!!!!!!!!!!!!!
# 문제1. 5명의 이름이 저장되어있는 리스트 만들기
# 5명의 이름 출력하는 반복문 만들기
namelist = ["차도헌","이성찬","황성현","이창호","강하영"]
print(type(namelist))
for name in namelist:
    print(name)

# 문제2. 정도전이라는 이름을 추가하고 출력하시오

namelist.append("정도전")
print(namelist[-1])

# 문제3. 리스트에 김유신이 있는지 확인하는 코드 작성하기
if "김유신" in namelist:
    print("등록된 이름이다")
else:
    print("등록되지 않은 이름이다.")

#문제4. 이름 리스트에 내림차순으로 정렬하여 출력하시오
namelist.sort(reverse=True)
print(namelist)

#문제 5. 과일의 이름이 두글자인 과일만 출력하시오
#힌트 : len
frute = ["사과","바나나","파인애플","딸기","오렌지","포도","배"]
frute.sort() # 딸기, 바나나, 배, 사과, 오렌지, 파인애플, 포도
price = [5000, 8000, 12000, 9500, 15500, 20400, 9000,]

# for fr in range(len(frute)):
#     if len(frute[fr]) == 2:
#         print(frute[fr])

#문제 6. 과일 검색 프로그램 만들기
# 과일이름 키보드를 통해 입력받는다.
# 입력한 과일이 리스트에 있다면 판매중, 없다면 품절 이라고 출력

# while True:
#     print("종료를 원하시면 3 을 입력해주세요")
#     user = input("과일을 입력해 주세요 : ")

#     if (user in frute) == True:
#         print("판매중")
#     elif user == "3" :
#         print("프로그램을 종료합니다")
#         break
#     else:
#         print("품절")



# 문제 7. 구매 할 과일을 입력 하면 총 지불금액 얼마인지 출력
# 단, 과일은 1개 구매할수도 있고 여러개 구매할수도 있어야 한다.


# total = 0

# while True:
#     print("================메뉴=================")
#     print(frute)
#     user = input("구매할 과일을 입력해주세요 : ").strip()
#     count = int(input("과일의 개수를 입력해주세요 : ").strip())
#     if user in frute:
#         idx = frute.index(user)
#         pic = price[idx]
#         pay = pic*count
#         total += pay
#         print(str(pay)+"원")
#     else:
#         print("다시 입력해수세요")
    
#     next = input("추가 구매를 원하시면 1 그만하시길원하시면 2번을 눌러주세요")

#     if int(next) == 1:
#         break

# print("총합 : ",total,"원")
# ==============================================================================
# fname = input("구매할 과일 입력 : ").split()

# total = 0

# for f in fname:
#     if f in frute:
#         idx = frute.index(f)
#         total += price[idx]
# print("총금액 : ", total)
#=================================================================================

# 튜플 - 리스트처럼 여러 데이터를 저장할수있는 자료형이다.
#  저장한 데이터를 수정 할 수 없다.
#  데이터를 보호하기 위한 목적
#  속도와 메모리 효율성 
#  딕셔너리의 키로 사용
#  여러개의 값을 변환(return) 시킬때

# 튜플 만들기 

number = (10,20,30,40) #작은 괄호 - 튜플, 대괄호 - 리스트
print(number)
print(type((1,2,3,4)))
print(type((10,))) #값을 하나만 넣을때는 뒤에 콤마를 넣어줘야 튜플로 인식됨

print(number[1])#인덱스 0 부터 시작

#number[0] = 100 값변경 안됨 오류뜸

#튜플 슬라이싱(자르기)
print(number[1:3]) 

# 튜플 검색
print( 10 in number )
print( number.index(20))

# 리스트와 다른점
# 수정불가 , 추가불가, 삭제불가
# number.append(200) 추가도 안됨 오류뜸
# number.remove(20) 안됨 오류뜸
# number.pop(20) 안됨 오류뜸
# del number[2] 안됨 오류뜸

print( number.count(20)) #특정값 갯수 구하기

data = 10,20,30,40,50 # 패킹 - 여러값을 하나로 묶기
print(type(data))

a,b,c,d,e = data # 언패킹 - 묶여있는값 여러개로 나누기
print(a,b,c,d,e)

red = 20
blue = 10

red,blue = blue,red
print(red,blue)

# 함수 반환 여러개
def get():
    return 10,20,30,40


# 리스트 <--> 튜플
info = ("다음주","금요일","빨간날","그래서","우리는","5월6일에","봐요")
#info[0]="이번주" 오류
info_list = list(info)  # 튜플 -> 리스트로 변환
info_list[0]="이번주"

info = tuple(info_list) #리스트 -> 튜플 변환
print(info) 






