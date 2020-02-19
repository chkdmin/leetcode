# -*- coding: utf-8 -*-


class Solution:
    cache = {}

    def countBitsWithAnd(self, num):
        """
        이전 숫자와 현재 숫자를 & 한 값에 +1
        """
        r = [0] * (num + 1)
        for i in range(1, num + 1):
            r[i] = r[i & (i - 1)] + 1
        return r

    def countBits(self, num: int):
        r = []
        b = 1
        for i in range(num + 1):
            if i == (b * 2):
                b = (b * 2)
            ans = 0
            while i > 0:
                cache = self.cache.get(i)
                if cache:
                    ans += cache
                    break
                i %= b
                ans += 1
            self.cache[len(r)] = ans
            r.append(ans)
        return r


if __name__ == '__main__':
    print(Solution().countBits(999))
