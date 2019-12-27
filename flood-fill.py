# -*- coding: utf-8 -*-


DIRECTION = (
    (-1, 0),  # TOP
    (1, 0),  # BOTTOM
    (0, -1),  # LEFT
    (0, 1),  # RIGHT
)


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        for r, c in DIRECTION:
            nr = sr + r
            if nr < 0 or nr >= len(image):
                continue

            nc = sc + c
            if nc < 0 or nc >= len(image[nr]):
                continue

            if image[nr][nc] != image[sr][sc]:
                continue

            prev = image[sr][sc]
            image[sr][sc] = None
            self.floodFill(image, nr, nc, newColor)
            image[sr][sc] = prev
        image[sr][sc] = newColor
        return image


if __name__ == '__main__':
    print(Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
