#camel_move возвращает список всех возможных ходов верблюда с текущих координат (x, y)
def camel_move(x, y):
    move = {
        (x + 1, y + 3), (x + 1, y - 3),
        (x - 1, y + 3), (x - 1, y - 3),
        (x + 3, y + 1), (x + 3, y - 1),
        (x - 3, y + 1), (x - 3, y - 1)
    }
    return move

#place_figure размещает фигуру на доске по заданным координатам, обновляет ее матрицу и вызывает функцию camel_move для определения всех возможных позиций после размещения верблюда
def place_figure(x, y, matrix):
    move = {
        (x + 1, y + 3), (x + 1, y - 3),
        (x - 1, y + 3), (x - 1, y - 3),
        (x + 3, y + 1), (x + 3, y - 1),
        (x - 3, y + 1), (x - 3, y - 1)
    }
    matrix[x][y] = '#'
    for i in move:
        x_1, y_1 = i[0], i[1]
        if len(matrix) > x_1 >= 0 and len(matrix) > y_1 >= 0:
            matrix[x_1][y_1] = '*'
    return matrix

#board_place размещает заданные фигуры по их координатам
def board_place(matrix, placed_figure):
    for x, y in placed_figure:
        place_figure(x, y, matrix)
    return matrix

#board_recursion рекурсия для поиска возможных комбинаций.
def board_recursion(N, L, place_x, place_y, answers, answer, cnt ):
    if cnt == L: #Если cnt равно L, то значит все элементы уже расставлены
        remember_answer = tuple(answer)
        answers.add(remember_answer)

        #Вывод первой возможной расстановки
        if len(answers) == 1:
            matrix = board_place([['0' for _ in range(N)] for _ in range(N)], remember_answer)
            for row in matrix:
                print(" ".join(row))
        return
    
    
    for i in range(place_x, N):
        #Если в строке есть поставленная фигура, то перебор идёт от этой фигуры
        if i == place_x:
            begin_y = place_y

        #Если таких нет, то перебор идёт от начала
        else:
            begin_y = 0
        for j in range(begin_y, N):
            if not camel_move(i, j).intersection(answer) and (i, j) not in answer :
                answer.add((i, j))
                board_recursion(N, L, i, j, answers, answer, cnt + 1)
                answer.discard((i, j))

def main():
    #Присваиваем переменным значения из input.txt
    with open('input.txt', "r") as file:
        N, L, K = map(int, file.readline().split())

        placed_figure = set()

        for i in file.readlines():
            x, y = map(int, i.split())
            placed_figure.add((x, y))


    answers = set()

    board_recursion(N, L, 0, 0, answers, placed_figure, 0)
    #Проверка наличия ответа и запись его в output.txt
    if answers != set(): 
        print('Кол-во решений:', len(answers))
        answer_final = [" ".join(map(str, answer)) + '\n' for answer in answers] 
    
        with open('output.txt', "w") as file:
            file.writelines(answer_final)
    else:
        print('Решений нет')
        with open('output.txt', "w") as file:
            file.writelines('No solution')
if __name__ == "__main__":
    main()