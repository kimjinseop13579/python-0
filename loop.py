

# print("숫자 : 1")
# print("숫자 : 2")
# print("숫자 : 3")
# print("숫자 : 4")
# print("숫자 : 5")

# # 5번 반복하는 반복문
# for i in range(101,1,-1):
#     print("숫자 : "+str(i)) 

# print("========================================================================")

# for ch in "hello":
#     print(ch)

# for name in ["차도헌", "박지연", "이성찬", "김진숙", "이동렬", "김현규"] :
#     if name.startswith("이"):
#         print(name)

# # 문제1. 1부터 10까지의 총합을 구하시오 반복문을 사용해서

# num = 0

# for add in range(1,11):
#     num += add

# print("총합 : "+str(num))

# # 문제 2. ["15,000", "13,000", "8,700", "9,000", "25,000"]
# # 배열에 출금 금액들이 저장되어있다.
# # 만원 이상 금액들에 대해 출력하세요

# print("========================================================================")

# money = ["15,000", "13,000", "8,700", "9,000", "25,000"]
# for i in range(5):
#     mon = int(money[i].replace(",",""))
#     if mon > 10000:
#         print(str(mon)+"원")

# print("========================================================================")

# for i in range(len(money)):
#     print("금액 : ",money[i])

# for i, v in enumerate(money):
#     print(i+1,v)

# print("========================================================================")

# #문제 3. [89,56,78,92,61,96,83,74]
# #203호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요
# # 80점 이상인 학생들의 위치(인덱스)도 출력

# score = [89,56,78,92,61,96,83,74]
# total = 0
# ave = 0

# for s in range(len(score)):
#     total += score[s]
#     if score[s] >= 80 :
#         print("80점 이상 학생 위치 : ",s," 점수 : ",score[s])

# ave = total/len(score)

# print ("점수 총합 : ",total)
# print ("점수 평균 : ",ave)

# while 문은 조건식이 참인경우 동작하기 때문에
# 쉽게 무한루프에 들어갈수 있다
# 하여 while 문 사용시 중단시킬수 있는 break 를 같이 사용하는게 좋다.

# num = 5
# while num > 2:
#     print("2보다 크다")
#     break

# while True:
#     num += 1
#     if num == 7: continue # 건너뛰기
#     print(num)
#     if num==10: break

# print("=============================================")
# while True:
#     cmd = input("명령어 입력 : ").strip().lower()
#     if cmd == "history":
#         print("모든 기록 출력")
#     elif cmd == "mkdir":
#         print("새로운 폴더 만들기")
#     elif cmd =="remove":
#         print("파일 삭제")
#     elif cmd == "exit":
#         print("종료")
#         break
#     else:
#         print("존재하지 않는 명령어 입니다.")

#파이썬 랜덤 사용
# import random

# num = random.randint(1,10) # random.randint(random + int)

# 동전 앞면 뒷면 맞추기 게임 만들기
# while True:
#     user = input("입력 : ").strip()
#     coin = random.randint(1,2)
#     print(coin)
#     if int(user) == coin :
#         print("성공")
#     else:
#         print("실패")
    
#     if user == "exit":
#         break

# n = random.randrange(1,10) #1~9
# game = ["가위","바위","보"]
# w = 0
# l = 0
# d = 0
# print("가위 바위 보!!! 경기~~~~!!!!!!!!! 시작~~~~~~~~~~~~~~~~~~~~~~!!!! 하겠습니다!!!!!!!!!!!!!!!!!!!!!!")
# while True:
#     print("점수판")
#     print(" 승 : ",w," 패 : ",l,"무 : ",d)
    
#     user = input("가위 바위 보!! : ").strip()

#     n = random.choice(game)
#     print(n)
#     print(user)
#     if (user =="가위" and n == "보") or (user == "바위" and n == "가위") or (user == "보" and n == "바위"):
#         print("승리 !!!!!!")
#         w += 1
#     elif user == n :
#         print("무승부!!!!!!!")
#         d += 1
#     elif user == "그만" :
#         print("그만!!!! 경기!!!!!!!!!!!!!!!!! 끝났습니다~~~!!!!!.")
#         break
#     else :
#         print("패배!!!!!!!")
#         l += 1

# cidx = game.index(com)
# uidx = game.indx(user)

# for i in range(5):
#     com = random.choice(game)
#     user = input("가위 바위 보 : ").strip()
#     print("컴퓨터 : ",com,"나",user)

#     comp = cidx - uidx #유저와 컴의 가위바위보 값 비교
# #가위 -0 바위-1 보-2 유저가 

#     if com == user:
#         print("비김")
#     elif comp == -1 or comp==2:
#         print("승리")
#     else:
#         print("패배")


