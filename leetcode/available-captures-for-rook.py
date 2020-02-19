# -*- coding: utf-8 -*-


class Solution:
    def numRookCaptures(self, board):
        ry = rx = -1
        count = 0
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 'R':
                    ry = y
                    rx = x
                    break
        # left side
        for y in range(ry - 1, -1, -1):
            if board[y][rx] != '.':
                if board[y][rx] == 'p':
                    count += 1
                break
        # right side
        for y in range(ry + 1, len(board)):
            if board[y][rx] != '.':
                if board[y][rx] == 'p':
                    count += 1
                break
        # top side
        for x in range(rx - 1, -1, -1):
            if board[ry][x] != '.':
                if board[ry][x] == 'p':
                    count += 1
                break
        # bottom side
        for x in range(rx + 1, len(board[rx])):
            if board[ry][x] != '.':
                if board[ry][x] == 'p':
                    count += 1
                break
        return count


if __name__ == '__main__':
    Solution().numRookCaptures(
        [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]])
