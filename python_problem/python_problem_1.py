num = 0
players = ["playerA", "playerB"]
turn = 0

while True:
    current_player = players[turn]
    try:
        count = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
        if count not in [1, 2, 3]:
            print("1,2,3 중 하나를 입력하세요")
            continue
    except ValueError:
        print("정수를 입력하세요")
    
    for i in range(1, count + 1):
        num += 1
        print(f"{current_player}: ", num)
        if num >= 31:
            exit()
    turn = 1 - turn
