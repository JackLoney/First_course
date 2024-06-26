import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox)

from PySide6.QtGui import QColor


class CamelGameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Camel Game")
        self.setGeometry(650, 200, 600, 600)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.placed_figure = set()
        
        # 1. Выбор размера доски
        self.label_board_size = QLabel("Размер доски:")
        self.spin_board_size = QSpinBox()
        self.spin_board_size.setMinimum(1)
        self.spin_board_size.setMaximum(20)
        self.spin_board_size.setValue(4) #Значение по умолчанию 
        
        # 2. Поле для ввода кол-ва поставленных фигур + поле для их координат
        self.label_placed_figures = QLabel("Поставленные фигуры:")
        self.line_placed_figures_count = QLineEdit()
        self.line_placed_figures_count.setPlaceholderText("Кол-во фигур")
        self.label_coordinates = QLabel("Координаты (x, y):")
        self.line_coordinates = QLineEdit()
        self.line_coordinates.setPlaceholderText("x, y")
        self.button_add_figure = QPushButton("Добавить фигуру")
        self.button_add_figure.clicked.connect(self.add_figure)
        self.button_input = QPushButton("Импортировать из 'input.txt'")
        self.button_input.clicked.connect(self.import_input)
        self.button_show = QPushButton("Показать добавленные")
        self.button_show.clicked.connect(self.show_coordinates)
        self.button_show.setEnabled(False)
        # 3. Поле для ввода необходимых фигур на доске
        self.label_required_figures = QLabel("Фигуры которые необходимо поставить:")
        self.spin_required_figures = QSpinBox()
        self.spin_required_figures.setMinimum(1)
        self.spin_required_figures.setMaximum(100)  # Достаточно большое значение
        
        # 4. Поле из клеток для отображения решения
        self.label_solution = QLabel("Кол-во решений: None")
        self.table_solution = QTableWidget()  # Создаём таблицу
        self.table_solution.horizontalHeader().setVisible(False)  # Скрываем заголовки столбцов
        self.table_solution.verticalHeader().setVisible(False)  # Скрываем заголовки строк
        self.table_solution.setColumnCount(0)  # Пока нет столбцов
        self.table_solution.setRowCount(0)  # Пока нет строк
        self.table_solution.verticalHeader().setDefaultSectionSize(50)
        self.table_solution.horizontalHeader().setDefaultSectionSize(50)

        # Кнопка "Решить"
        self.button_solve = QPushButton("Решить")
        self.button_solve.clicked.connect(self.solve)
        
        # Кнопка очистить"
        self.button_clear = QPushButton("Очистить")
        self.button_clear.clicked.connect(self.clear_board)
        # Расположение элементов на сетке
        self.grid.addWidget(self.label_board_size, 0, 0)
        self.grid.addWidget(self.spin_board_size, 0, 1)
        self.grid.addWidget(self.label_placed_figures, 1, 0)
        self.grid.addWidget(self.line_placed_figures_count, 1, 1)
        self.grid.addWidget(self.label_coordinates, 2, 0)
        self.grid.addWidget(self.line_coordinates, 2, 1)
        self.grid.addWidget(self.button_add_figure, 2, 2)
        self.grid.addWidget(self.button_show, 3, 0)
        self.grid.addWidget(self.button_input, 3, 1)
        self.grid.addWidget(self.label_required_figures, 4, 0)
        self.grid.addWidget(self.spin_required_figures, 4, 1)
        self.grid.addWidget(self.label_solution, 5, 0)
        self.grid.addWidget(self.table_solution, 6, 0, 1, 3)  # Занимает 3 столбца
        self.grid.addWidget(self.button_solve, 7, 0, 1, 3)  # Занимает 3 столбца
        self.grid.addWidget(self.button_clear, 8, 0, 1, 3) # Занимает 3 столбца

    def add_figure(self):
        try:
            figure_count = int(self.line_placed_figures_count.text())
            self.line_placed_figures_count.setReadOnly(1)
            x, y = map(int, self.line_coordinates.text().split(","))
            self.placed_figure.add((x, y))
            if len(self.placed_figure) > 0:
                self.button_show.setEnabled(True)
            if len(self.placed_figure) == figure_count:
                self.line_placed_figures_count.setReadOnly(1)
                self.line_coordinates.clear()
                self.line_coordinates.setPlaceholderText("Все координаты на месте")
                self.line_coordinates.setReadOnly(1)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Некорректные данные. Проверьте ввод.")
            return

        # Очистите поля ввода после добавления фигуры
        self.line_coordinates.clear()

    def solve(self):
        try:
            N = self.spin_board_size.value()
            L = self.spin_required_figures.value()
            placed_figure = self.placed_figure

            answers = set()
            Fisrt_Solution = list()
            board_recursion(N, L, 0, 0, answers, placed_figure, 0, Fisrt_Solution)
            if answers != set():
                self.label_solution.setText(f"Кол-во решений: {len(answers)}")
                print('Кол-во решений:', len(answers))
                answer_final = [" ".join(map(str, answer)) + '\n' for answer in answers] 
                self.table_solution.setColumnCount(N)
                self.table_solution.setRowCount(N)
                for i in range(N):
                    for j in range(N):
                        item = QTableWidgetItem()
                        if Fisrt_Solution[i][j] == '#':
                            item.setBackground(QColor("green"))
                        elif Fisrt_Solution[i][j] == '*':
                            item.setBackground(QColor("blue"))
                        self.table_solution.setItem(i, j, item)
                with open('output.txt', "w") as file:
                    file.writelines(answer_final)
            else:
                QMessageBox.information(self, "Результат", "Решений нет")
                print('Решений нет')
                with open('output.txt', "w") as file:
                    file.writelines('No solution')
        except Exception as e:
                QMessageBox.warning(self, "Ошибка", str(e))
    
    def clear_board(self):
        self.placed_figure = set()
        self.line_placed_figures_count.setReadOnly(0)
        self.line_placed_figures_count.clear()
        self.table_solution.clear()
        self.line_coordinates.setPlaceholderText("x, y")
        self.line_coordinates.setReadOnly(0)
        self.label_solution.setText("Кол-во решений: None")
    
    def import_input(self):
        with open('input.txt', "r") as file:
            N, L, K = map(int, file.readline().split())
            self.spin_board_size.setValue(N)
            self.spin_required_figures.setValue(L)
            self.line_placed_figures_count.setText(str(K))
            for i in file.readlines():
                x, y = map(int, i.split())
                self.placed_figure.add((x, y))
            if len(self.placed_figure) > 0:
                self.button_show.setEnabled(True)
            if len(self.placed_figure) == K:
                self.line_coordinates.clear()
                self.line_placed_figures_count.setReadOnly(1)
                self.line_coordinates.setPlaceholderText("Все координаты на месте")
                self.line_coordinates.setReadOnly(1)

    def show_coordinates(self):
        QMessageBox.information(self, 'Координаты', str(self.placed_figure))

if __name__ == "__main__":
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
    def board_recursion(N, L, place_x, place_y, answers, answer, cnt, First_Solution):
        if cnt == L: #Если cnt равно L, то значит все элементы уже расставлены
            remember_answer = tuple(answer)
            answers.add(remember_answer)

            #Вывод первой возможной расстановки
            if len(answers) == 1:
                matrix = board_place([['0' for _ in range(N)] for _ in range(N)], remember_answer)
                First_Solution.extend(matrix)
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
                    board_recursion(N, L, i, j, answers, answer, cnt + 1, First_Solution)
                    answer.discard((i, j))

    app = QApplication(sys.argv)
    window = CamelGameWindow()
    window.show()
    sys.exit(app.exec())