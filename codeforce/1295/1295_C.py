# -*- coding: utf-8 -*-


def main():
    for _ in range(int(input())):
        s = input()
        t = input()
        z = ''
        ret = 0
        d = {}
        while z != t:
            can = False
            idx = 0
            while idx < len(s):
                c = s[idx]
                v = d.get(t[len(z)])
                if v and idx <= v[-1]:
                    is_break = False
                    is_continue = False
                    for jdx in v:
                        if jdx >= idx:
                            z += s[jdx]
                            can = True
                            is_continue = True
                            idx = jdx + 1
                            if z == t:
                                is_break = True
                            break
                    if is_break:
                        break
                    if is_continue:
                        continue

                if d.get(c) is None:
                    d[c] = []
                d[c].append(idx)

                if t[len(z)] == c:
                    z += c
                    can = True
                    if z == t:
                        break
                idx += 1
            if not can:
                ret = -1
                break
            ret += 1
        print(ret)


if __name__ == '__main__':
    main()
