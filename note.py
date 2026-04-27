"""
카드 덱 (무늬 4가지 x 숫자 13가지 = 52장)
플레이어 패 / 딜러 패
점수 계산 (A는 1 또는 11)
1. 카드 덱 만들기
2. 덱 섞기 (shuffle)
3. 플레이어/딜러 각 2장씩 뽑기
4. 플레이어가 Hit(카드 추가) or Stand(멈춤) 선택
5. 딜러는 16이하면 무조건 Hit
6. 21 넘으면 bust → 패배
7. 최종 점수 비교 → 승패 결정

딜러 패 만들기 (딜러도 2장 뽑아야 해요)
점수 계산 - 숫자 카드는 그대로, J/Q/K는 10, A는 1 또는 11
while문으로 반복 - 지금은 히트를 한 번밖에 못해요
bust 판정 - 21 초과하면 바로 게임 오버
딜러 AI - 딜러는 16 이하면 무조건 히트
최종 승패 판정
"""
def jqk(n):
    if n == "J" or n=="Q" or n == "K":
        return "10"
    elif n== "A":
        return "11"
    else:
        return n
import random
ptn = ["♠", "♥", "♦", "♣"]
num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K",]

card_deck = []
total =0

for p in ptn:
    for n in num:
        card_deck.append(p+n)

user_deck = []
for i in range(2):
    card = random.choice(card_deck)
    card_deck.remove(card)
    user_deck.append(card)
print (user_deck)


print("카드를 더 받으시겠습니까? 1.yes 2.no")
choice = int(input("입력 : "))

if choice == 1:
    card = random.choice(card_deck)
    card_deck.remove(card)
    user_deck.append(card)
    print(user_deck)

for c in user_deck:
    n = c[1:]
    n = jqk(n)
    total += int(n)
    print(total)
    if total > 21:
        print("패배")


        





    