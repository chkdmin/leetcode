# -*- coding: utf-8 -*-


def find(x, y, t, nodes, mark, index):
    if index < 0 or index >= len(nodes):
        return 0

    xt, yt = nodes[index]
    need_time = abs(xt - x) + abs(yt - y)
    if need_time > t or mark[index]:
        return 0

    right = index + 1
    for i in range(index + 1, len(nodes)):
        if not mark[i]:
            right = i
            break

    left = index - 1
    for i in range(index - 1, 0, -1):
        if not mark[i]:
            left = i
            break

    print(left, right)
    mark[index] = True
    ret = 1 + max(find(xt, yt, t - need_time, nodes, mark, left),
                  find(xt, yt, t - need_time, nodes, mark, right))
    mark[index] = False
    return ret


def main():
    x0, y0, ax, ay, bx, by = map(int, input().split())
    xs, ys, t = map(int, input().split())
    nodes = []

    xf, yf = x0, y0
    xi, yi = x0, y0
    index = 0
    while True:
        ct = abs(xs - xi) + abs(ys - yi)
        if ct > t:
            if xi > xs or yi > ys:
                break
            else:
                xi, yi = ax * xi + bx, ay * yi + by
                continue

        nodes.append((xi, yi))

        ft = abs(xs - xf) + abs(ys - yf)
        if ct < ft:
            xf, yf = xi, yi
            index = len(nodes) - 1

        xi, yi = ax * xi + bx, ay * yi + by

    print(nodes, index, len(nodes))
    print(find(xs, ys, t, nodes, [False for _ in range(len(nodes))], index))


if __name__ == '__main__':
    main()
