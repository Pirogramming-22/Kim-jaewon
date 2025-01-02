def brGage(num, current_player):
    try:
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
    
    return num, False


#코드 블록 자체의 중복성이 아닌 코드의 논리적 흐름 중 재사용성에 입각하여 중복 코드 추출

num = 0
players = ["playerA", "playerB"]
turn = 0

while True:
    current_player = players[turn]
    no_current_player = players[1 - turn]
    num, is_over = brGage(num, current_player)

    if is_over:
        print(f"{no_current_player} win!")
        break

    turn = 1 - turn
    
