import random

def brGage(num, current_player):
    try:
        if current_player == "computer":
            count = random.randint(1, 3)
        else:
            count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if count not in [1, 2, 3]:
                print("1,2,3 중 하나를 입력하세요")
                return num, False
    except ValueError:
        print("정수를 입력하세요")
        return num, False
    
    for i in range(1, count + 1):
        num += 1
        print(f"{current_player}: ", num)
        if num >= 31:
            return num, True
    
    return num, True


#코드 블록 자체의 중복성이 아닌 코드의 논리적 흐름 중 재사용성에 입각하여 중복 코드 추출

#Step9를 위해 player2대신 computer를 넣어 자동으로 count를 결정해버리면
#player가 3보다 큰 숫자나 정수가 아닌 문자를 입력할 때 사용자의 input을 다시 받지 않고 computer가 그 다음 count를 이어가는 문제 발생.
#따라서 player가 3보다 큰 숫자나 정수가 아닌 문자를 입력할 때 다시 input을 받도록 수정

num = 0
players = ["computer", "player"]
turn = 0

while True:
    current_player = players[turn]
    no_current_player = players[1 - turn]
    num, is_well_playing = brGage(num, current_player)

    if not is_well_playing:
        continue

    if num >= 31:
        print(f"{no_current_player} win!")
        break

    turn = 1 - turn
    
