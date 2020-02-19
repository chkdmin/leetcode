# -*- coding: utf-8 -*-


class Solution:
    def fizzBuzz(self, n: int):
        ret = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                text = 'FizzBuzz'
            elif i % 5 == 0:
                text = 'Buzz'
            elif i % 3 == 0:
                text = 'Fizz'
            else:
                text = str(i)
            ret.append(text)
        return ret


if __name__ == '__main__':
    print(Solution().fizzBuzz(15))
