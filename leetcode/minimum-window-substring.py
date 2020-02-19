# -*- coding: utf-8 -*-
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)  # hash table to store char frequency
        missing = len(t)  # total number of chars we care
        start = end = i = 0
        for j, char in enumerate(s, 1):  # index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:  # match all chars
                while i < j and need[s[i]] < 0:  # remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1  # make sure the first appearing char satisfies need[char]>0
                missing += 1  # we missed this first char, so add missing by 1
                if end == 0 or j - i < end - start:  # update window
                    start, end = i, j
                i += 1  # update i to start+1 for next window
        return s[start:end]

    def min_window_by_brute_force(self, s: str, t: str) -> str:
        start = end = -1
        min_ = 9999
        for i in range(len(s)):
            f = [a for a in t]
            for j in range(i, len(s)):
                if s[j] in f:
                    f.remove(s[j])
                if not f:
                    if min_ > j - i + 1:
                        min_ = j - i + 1
                        start = i
                        end = j + 1
                    break
        return s[start:end]


if __name__ == '__main__':
    print(Solution().min_window_by_brute_force('fasdkalmdblab', 'ab'))
    print(Solution().minWindow('ADOBECODEBANCAB', 'ABC'))
