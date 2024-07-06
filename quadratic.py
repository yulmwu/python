import math

def solve_quadratic(a, b, c): # quadratic = 이차
    '''
    x = (-b + sqrt(b^2 - 4ac) / 2a) 또는
    x = (-b - sqrt(b^2 - 4ac) / 2a)
    '''
    discriminant = b**2 - 4*a*c # 판별식

    if discriminant < 0: # D < 0 (복소수일 경우, 해 없음)
        return None, None

    elif discriminant == 0: # D = 0 (중근) (x = -b / 2a)
        x = -b / (2*a)
        return x, None
    else: # D > 0 (서로 다른 두 실수)
        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return x1, x2

def calculate_vertex(a, b, c): # vertex = 꼭짓점
    vertex_x = -b // (2 * a)  # 꼭짓점의 x = -b / 2a
    vertex_y = int(a * vertex_x ** 2 + b * vertex_x + c)  # 식에 대입해서 꼭짓점의 y 구함

    return vertex_x, vertex_y

def draw_graph(a, b, c, row = 12, col = 24):
    if a == 0:
        raise ValueError('이차방정식이 아닙니다')
    
    midpoint_row = row // 2 # 표현할 x(row) 최대의 중점
    midpoint_col = col // 2 # 표현할 y(col) 최대의 중점

    # 그래프 2차원 배열 구성
    graph = [[' ' for _ in range(row + 1)] for _ in range(col + 1)]
    '''
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],     [col, row] = [y, x]
    '''

    for i in range(row):
        graph[midpoint_col][i] = '-' # x 축

    for i in range(col):
        graph[i][midpoint_row] = '|' # y 축

    graph[midpoint_col][row] = '>' # x 축 구분
    graph[0][midpoint_row] = '^' # y 축 구분
    graph[midpoint_col][midpoint_row] = 'O' # 원점 O

    coords = []

    for x in range(row): # x 축 반복
        if not 0 <= x < row: # x의 범위가 표시할 최대 x축의 범위에 해당하지 않는가(0 이상, 최대 x축 미만)
            continue

        x_coord = x - midpoint_row # x 축의 중점을 기준으로 x 움직임 (표시용)
        # x = 표시할 graph 배열상의 인덱스
        # x_coord = 좌표상의 x의 값

        y_coord = a * x_coord ** 2 + b * x_coord + c # 이차방정식 계산 ax^2 + bx + c
        # y = 표시할 graph 배열상의 인덱스
        # y_coord = 좌표상의 y의 값

        y = midpoint_col - int(y_coord) # y축의 중점을 기준으로 y 움직임 (표시용)
        if 0 <= y < col: # 표시할 최대 x, y 범위에 해당하는가
            coords.append((x_coord, y_coord))
            graph[y][x] = '*'

    return '\n'.join(map(lambda x: ' '.join(x), graph)), coords


a, b, c = 1, -2, -3
graph, coords = draw_graph(a, b, c)
print(graph)
print('좌표:', ', '.join(map(str, coords)))
print(f'꼭짓점의 좌표: {calculate_vertex(a, b, c)}')

x1, x2 = solve_quadratic(a, b, c)
print(f'{a:+}x^2{b:+}x{c:+} = 0 의 해: {x1} 또는 {x2}')
