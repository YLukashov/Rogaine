import sys
sys.setrecursionlimit(10 ** 9) # увеличение глубины рекурсии, так как в питоне изначальный максимум равен 1000

n = 12  # контрольные пункты
m = 13  # дороги

g = [[1], [0, 2, 3], [1, 4, 5, 6], [1, 7], [2, 8], [2, 6], [2, 5], [3, 9, 10], [4, 9], [7, 8], [7, 11], [10]]  # g[i] - в какие вершины можно попасть из i
points = [0, 1, 3, 1, 3, 1, 1, 2, 3, 2, 6, 1] # points[i] сколько можно получить очков, если была пройдена вершина i
times = []  # times[i][j] - время в минутах между вершиной i и j по ребру
for i in range(12):
    h = [-1 for j in range(12)]
    times.append(h)

times[0][1] = 5
times[1][2] = 45
times[1][3] = 15
times[2][4] = 40
times[2][5] = 2.5
times[2][6] = 2.5
times[5][6] = 2.5
times[4][8] = 20
times[8][9] = 25
times[9][7] = 12
times[3][7] = 10
times[7][10] = 72
times[10][11] = 20

# расстояние из i в j по ребру такое же, как и из j в i
for i in range(12):
    for j in range(12):
        if times[i][j] != -1:
            times[j][i] = times[i][j]


point_max = 0
route_max = []

MAX_VISIT = 49
# Количество очков, если посетить вершины all_vertexes
def count_point(all_vertexes):
    ans = 0
    set_all_vertexes = set()  # уникальные посещенные вершины

    for v in all_vertexes:
        set_all_vertexes.add(v)

    for v in set_all_vertexes:
        ans += points[v]
    return ans


# потеря очков с учетом штрафа
def loss_of_points(time_happen):
    if time_happen <= 180:
        return 0
    time_happen -= 180
    if time_happen < 5:
        return -1
    if time_happen < 10:
        return -2
    if time_happen < 15:
        return -3
    if time_happen < 20:
        return -4
    if time_happen < 25:
        return -5
    if time_happen < 30:
        return -6
    if time_happen < 35:
        return -7
    if time_happen < 40:
        return -8
    if time_happen < 45:
        return -9


# rec(текущее затраченное время, текущая вершина, посещенные вершины)
def rec(cur_time, cur_vertex, visited):
    global point_max
    global route_max
    if cur_vertex == 0 and cur_time <= 215:  # Текущая вершина финиш и мы не затратили более 180 минут
        new_point = count_point(visited) + loss_of_points(cur_time)
        if new_point == 16:
            print(visited)
        if new_point > point_max:
            point_max = new_point
            route_max = visited
    if cur_time >= 215 or len(visited) > MAX_VISIT:
        return
    else:
        for child in g[cur_vertex]:
            new_cur_time = cur_time + times[cur_vertex][child]
            new_visited = [child]
            for vis_vert in visited:
                new_visited.append(vis_vert)
            rec(new_cur_time, child, new_visited)


rec(0, 0, [0])
