def solve():
    # Вводим количество вершин и рёбер
    n, m = map(int, input("Введите количество вершин и рёбер: ").split())

    # Если количество рёбер нечётное — решения нет
    if m % 2 == 1:
        print(-1)
        return

    edges = []
    print("Введите рёбра графа (по два числа через пробел):")
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    # # Если количество рёбер нечётное — решения нет
    # if m % 2 == 1:
    #     print(-1)
    #     return

    # Чередуем направление рёбер
    print("Ориентированные рёбра:")
    for i, (u, v) in enumerate(edges):
        if i % 2 == 0:
            print(u, v)
        else:
            print(v, u)


# Запускаем
solve()