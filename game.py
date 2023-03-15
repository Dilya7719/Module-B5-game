num = '012'
beg = '  ┌───┬───┬───┐'
mid = '  ├───┼───┼───┤'
end = '  └───┴───┴───┘'
win_comb = ['036','147','258','012','345','678','048','246']

def print_field(f):
    print('\n    0   1   2 ')
    print(beg)
    for i in range(3):
        print(f'{num[i]} │ {f[i*3]} │ {f[i*3+1]} │ {f[i*3+2]} │')
        if i<2:
            print(mid)
    print(end)

def input_kord(player,f):
    print(f'\nХодит игрок {player}')
    while True:
        kord = input('\nЗадайте координаты поля в виде двух цифр в диапазоне 0...2,\nпервая цифра - строка, вторая цифра - столбец   ... ')
        kord = kord.replace(' ','')
        if len(kord)!=2:
            print('\nЗадайте две координаты!')
            continue
        if not(kord[0] in num and kord[1] in num):
            print('\nКоординаты заданы некорректно, повторите ввод!')
            continue
        if f[int(kord[0])*3+int(kord[1])]!=' ':
            print('\nЭта ячейка уже занята! Повторите ввод!')
            continue
        break
    f[int(kord[0])*3+int(kord[1])]=player
    print_field(f)
    return f

def check_rezult(player,f):
    check = ''.join(f)
    for comb in win_comb:
        if all([check[int(comb[0])]==player, check[int(comb[1])]==player, check[int(comb[2])]==player]):
            return True
    return False

print("""Игра "Крестики-нолики"
=======================
Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики).
Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или большой диагонали, выигрывает. 
Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали, горизонтали или большой диагонали
нет трёх одинаковых знаков, партия считается закончившейся в ничью. Первый ход делает игрок, ставящий крестики.""")
field = [' ']*9
count = 0
print_field(field)
print()
while count<9:
    count += 1
    if count%2 == 0:
        player = 'O'
    else:
        player = 'X'
    field = input_kord(player,field)
    if check_rezult(player,field):
        print(f'Игра окончена! Победа игрока {player}.')
        break
else:
    print('Игра окончена в ничью!')