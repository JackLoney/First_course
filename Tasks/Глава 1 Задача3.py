def print_zigzag(string, rows):
    if rows == 1:  # Если строка всего одна, возвращаем исходную строку
        return string
    
    # Создаем пустые списки для каждой строки
    zigzag = [[] for _ in range(rows)]
    
    row = 0  # Текущая строка
    direction = 1  # Направление движения по строкам: 1 (вниз) или -1 (вверх)
    
    for i in string:
        zigzag[row].append(i)  # Добавляем символ в текущую строку
        
        # Если достигнута последняя строка, меняем направление на вверх
        if row == rows - 1:
            direction = -1
        
        # Если достигнута первая строка, меняем направление на вниз
        elif row == 0:
            direction = 1
        
        row += direction  # Переходим на следующую строку
    
    return ''.join([''.join(row) for row in zigzag]), zigzag # Объединяем все строки в одну строку

# Пример использования
input_string, num_rows = map(str, input().split())
num_rows = int(num_rows)
result = print_zigzag(input_string, num_rows)
print(result) 
