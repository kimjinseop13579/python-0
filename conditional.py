
# # if(i>5){ 자바, 자바스크립트 방법

# # }else{

# # }

# # if 조건식:
# #       실행할 코드
# num = 10
# if num > 5 :
#     print("크다")
#     print("10 이 크다")
# elif num < 5:
#     print("작다")
#     print("5보다 작다")

# #  변수 apple의 값이 10이상이라면 1봉지 라고 출력
# # apple 의 값이 10 미만이라면 개당 2000원
# apple = input("갯수 : ")
# apple = int(apple)

# if apple >= 10:
#     print("1봉지 8000원")
# elif apple < 10:
#     print("개당 2000원")


# res = 2
# match res:
#     case 1 | 4:
#         print("숫자 1 또는 4 이다")
#     case 2:
#         print("숫자 2 이다")
#     case int():
#         print("정수이다")


# like 좋아요 변수의 값이 100 이상이면 spot 등록 출력
# 좋아요 변수의 값이 10 이하라면 관심 spot 출력

##   정수로 변환 int(값)  실수로 변환 float(값)  문자열로 변환 str(값)


# like = int(input("좋아요 수 : "))

# if like >= 100:
#     print("spot 등록")
# elif like <=10:
#     print("관심 spot")

# 아이디 와 비밀번호 입력 받아 일치하면 로그인성공, 불일치 하면 
# 아이디 또는 비밀번호가 잘못되었습니다. 출력
# 아이디는 진섭, 비밀번호는 babo

# id = input("아이디 : ")
# pw = input("비밀번호 : ")

# if id == "진섭" and pw == "babo" :
#     print("로그인 성공")
# else :
#     print("아이디 또는 비밀번호가 잘못되었습니다")

# 파이썬에서 문자열 포함 여부 확인하는 방법
# word = "나는 김진섭 입니다."
# if '김진섭' in word:
#     print("있다")
# else:
#     print("없다")

# word = "나는 진섭이가 짝꿍일때 별로였다"

# # word 안에 동렬 이름이 없다는 것을 확인 할수 있는 코드를 만드세요

# if '이동렬' not in word:
#     print("없다")

#startswith() 함수 시작 문자열 비교
# word = "이창호 님께서 입장 하셨습니다."
# if word.startswith('이창호'):
#     print("신원 확인")
# else:
#     print("이창호 님이 아닙니다")

# # 대소문자 변환
# word = "i like banana"
# print(word.upper()) #대문자
# print(word.lower()) #소문자
# print(word.title()) #대문자 - 단어의 첫글자만

# #공백제거 - 개발시 필요필수 (이거때문에 오류나면 골치아픔)
# word = " banana "
# print(word) #공백제거 없이
# print(word.strip()) #양쪽공백 제거
# print(word.lstrip()) #왼쪽 공백제거
# print(word.rstrip()) #오른쪽 공백 제거

# #찾기
# word = "찬용이는 진섭이보다 지금이 좋다고 한다."
# print(word.find("진섭")) #있다면 위치 반환(인덱스) 없으면 -1

# print(word.index("동렬")) #인덱스 반환, 없으면 에러

# #문자열 바꾸기 .replace("현재문자열에서 변경 할 문자열", "교체할 문자열")
# word = word.replace("찬용이","성현이")
# print(word)

# #문자열 나누기 - 배열
# text = "도헌-지연-동렬-진섭"
# result = text.split("-")
# print(result)

# # 배열을 하나의 문자열로 합치기
# text = ",".join(result) # 배열값 하나하나에 , 를 넣어서 하나의 문자열 만들기
# print(text)

# #숫자냐 아니냐
# text = "123456"
# print(text.isdigit()) #문자열을 숫자로 변환하기전에 확인하는용도 isdigit (is 디지트)

# #문자 종류 확인
# text1 = "tomato"
# text2 = "  "
# text3 = "사월22"
# print(text2.isalpha()) #문자만 있냐 isalpha (is 알파)
# print(text1.isspace()) #공백이 있냐 isspace (is 스페이스)
# print(text3.isalnum()) #문자+숫자냐 isalnum (is 알 넘)

# #문자열 정렬
# text = "15"
# print(text.zfill(6)) # 함수()안에 자릿수 넣기 zfill (z 필)
# print(text.rjust(4)) # 오른쪽 R 왼쪽 L 정렬 just
# print(text.ljust(5))

# 문제1. - 공백제거와 소문자 변환 하려면??
# input 으로 입력 받아서 공백제거와 소문자 변환을 하세요

# text = input("대문자 입력 : ")
# print(text.strip().lower())

# 문제2. "행복,우울,기쁨,슬픔,화남"
# 위 문자열을 나누어 보시오

# testtext = "행복,우울,기쁨,슬픔,화남"
# result = testtext.split(",")
# print(result)

# 문제3. 회원가입시 이메일 입력을하는데 특정 주소만 가능하다.
# naver.com, gmail.com, nate.com, daum.net
# 위 4개 만 가능하다 input으로 이메일을 입력받아서 가입 가능한지 불가능 한지 출력

# email = input("이메일 입력 : ").strip().lower()
# if email.endswith("naver.com"):
#     print("가입 가능")
# elif email.find("gmail.com") != -1 :
#     print("가입 가능")
# elif email.split("@")[1] == "nate.com":
#     print("가입 가능")
# elif email.endswith("daum.net") : 
#     print("가입가능")
# else:
#     print("가입 불가능")

# 문제 4. 금액 계산하기
# 각 업체별로 입금이 되었다. 총액이 얼마인지 출력하세요
쿠팡 = "135,900원"
네이버 = "540,000원"
오드론 = "2,340,090원"

쿠팡 = 쿠팡.replace("원","").replace(",","")
네이버 = 네이버.replace("원","").replace(",","")
오드론 = 오드론.replace("원","").replace(",","")

쿠팡 = int(쿠팡)
네이버 = int(네이버)
오드론 = int(오드론)

add = str(쿠팡+네이버+오드론)
print("총금액 : "+add+"원")




