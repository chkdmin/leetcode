# -*- coding: utf-8 -*-


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [-1] * k
        self.front = 0
        self.rear = 0

    def getPrevFront(self):
        return self.front + 1 if self.front + 1 < len(self.deque) else 0

    def getNextFront(self):
        return self.front - 1 if self.front - 1 >= 0 else len(self.deque) - 1

    def getPrevRear(self):
        return self.rear - 1 if self.rear - 1 >= 0 else len(self.deque) - 1

    def getNextRear(self):
        return self.rear + 1 if self.rear + 1 < len(self.deque) else 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if not self.isEmpty():
            self.front = self.getNextFront()
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if not self.isEmpty():
            self.rear = self.getNextRear()
        self.deque[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.deque[self.front] = -1
        if not self.isEmpty():
            self.front = self.getPrevFront()
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.deque[self.rear] = -1
        if not self.isEmpty():
            self.rear = self.getPrevRear()
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.front == self.rear and self.deque[self.front] == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.deque[self.getNextFront()] != -1 and self.deque[self.getNextRear()] != -1


if __name__ == '__main__':

    c = MyCircularDeque(607)
    print(1, c.insertFront(503))
    print(c.front, c.rear, c.deque)
    print(2, c.insertLast(930))
    print(c.front, c.rear, c.deque)
    print(3, c.getFront())
    print(c.front, c.rear, c.deque)
    print(4, c.getFront())
    print(c.front, c.rear, c.deque)
    print(5, c.isEmpty())
    print(c.front, c.rear, c.deque)
    print(6, c.isEmpty())
    print(c.front, c.rear, c.deque)
    print(7, c.getFront())
    print(c.front, c.rear, c.deque)
    print(8, c.deleteLast())
    print(c.front, c.rear, c.deque)
    print(9, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(10, c.getRear())
    print(c.front, c.rear, c.deque)
    print(11, c.insertLast(519))
    print(c.front, c.rear, c.deque)
    print(12, c.getRear())
    print(c.front, c.rear, c.deque)
    print(13, c.getFront())
    print(c.front, c.rear, c.deque)
    print(14, c.insertFront(774))
    print(c.front, c.rear, c.deque)
    print(15, c.isEmpty())
    print(c.front, c.rear, c.deque)
    print(16, c.insertLast(796))
    print(c.front, c.rear, c.deque)
    print(17, c.isEmpty())
    print(c.front, c.rear, c.deque)
    print(18, c.getFront())
    print(c.front, c.rear, c.deque)
    print(19, c.isFull())
    print(c.front, c.rear, c.deque)
    print(20, c.insertLast(902))
    print(c.front, c.rear, c.deque)
    print(21, c.getFront())
    print(c.front, c.rear, c.deque)
    print(22, c.getRear())
    print(c.front, c.rear, c.deque)
    print(23, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(24, c.insertLast(695))
    print(c.front, c.rear, c.deque)
    print(25, c.getFront())
    print(c.front, c.rear, c.deque)
    print(26, c.getFront())
    print(c.front, c.rear, c.deque)
    print(27, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(28, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(29, c.insertFront(69))
    print(c.front, c.rear, c.deque)
    print(30, c.getFront())
    print(c.front, c.rear, c.deque)
    print(31, c.getRear())
    print(c.front, c.rear, c.deque)
    print(32, c.getRear())
    print(c.front, c.rear, c.deque)
    print(33, c.isEmpty())
    print(c.front, c.rear, c.deque)
    print(34, c.getRear())
    print(c.front, c.rear, c.deque)
    print(35, c.getRear())
    print(c.front, c.rear, c.deque)
    print(36, c.isFull())
    print(c.front, c.rear, c.deque)
    print(37, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(38, c.getFront())
    print(c.front, c.rear, c.deque)
    print(39, c.insertLast(780))
    print(c.front, c.rear, c.deque)
    print(40, c.insertFront(665))
    print(c.front, c.rear, c.deque)
    print(41, c.isFull())
    print(c.front, c.rear, c.deque)
    print(42, c.getRear())
    print(c.front, c.rear, c.deque)
    print(43, c.insertFront(128))
    print(c.front, c.rear, c.deque)
    print(44, c.insertLast(750))
    print(c.front, c.rear, c.deque)
    print(45, c.getRear())
    print(c.front, c.rear, c.deque)
    print(46, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(47, c.getRear())
    print(c.front, c.rear, c.deque)
    print(48, c.insertLast(47))
    print(c.front, c.rear, c.deque)
    print(49, c.deleteLast())
    print(c.front, c.rear, c.deque)
    print(50, c.isFull())
    print(c.front, c.rear, c.deque)
    print(51, c.insertLast(530))
    print(c.front, c.rear, c.deque)
    print(52, c.getFront())
    print(c.front, c.rear, c.deque)
    print(53, c.getFront())
    print(c.front, c.rear, c.deque)
    print(54, c.getRear())
    print(c.front, c.rear, c.deque)
    print(55, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(56, c.getRear())
    print(c.front, c.rear, c.deque)
    print(57, c.getFront())
    print(c.front, c.rear, c.deque)
    print(58, c.insertFront(291))
    print(c.front, c.rear, c.deque)
    print(59, c.deleteLast())
    print(c.front, c.rear, c.deque)
    print(60, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(61, c.getRear())
    print(c.front, c.rear, c.deque)
    print(62, c.insertFront(982))
    print(c.front, c.rear, c.deque)
    print(63, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(64, c.deleteLast())
    print(c.front, c.rear, c.deque)
    print(65, c.insertFront(632))
    print(c.front, c.rear, c.deque)
    print(66, c.insertLast(384))
    print(c.front, c.rear, c.deque)
    print(67, c.getFront())
    print(c.front, c.rear, c.deque)
    print(68, c.insertFront(61))
    print(c.front, c.rear, c.deque)
    print(69, c.insertLast(684))
    print(c.front, c.rear, c.deque)
    print(70, c.getFront())
    print(c.front, c.rear, c.deque)
    print(71, c.getFront())
    print(c.front, c.rear, c.deque)
    print(72, c.insertLast(524))
    print(c.front, c.rear, c.deque)
    print(73, c.insertLast(179))
    print(c.front, c.rear, c.deque)
    print(74, c.getFront())
    print(c.front, c.rear, c.deque)
    print(75, c.getFront())
    print(c.front, c.rear, c.deque)
    print(76, c.insertLast(948))
    print(c.front, c.rear, c.deque)
    print(77, c.getRear())
    print(c.front, c.rear, c.deque)
    print(78, c.insertLast(992))
    print(c.front, c.rear, c.deque)
    print(79, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(80, c.insertFront(125))
    print(c.front, c.rear, c.deque)
    print(81, c.getRear())
    print(c.front, c.rear, c.deque)
    print(82, c.getRear())
    print(c.front, c.rear, c.deque)
    print(83, c.getFront())
    print(c.front, c.rear, c.deque)
    print(84, c.insertLast(2))
    print(c.front, c.rear, c.deque)
    print(85, c.deleteFront())
    print(c.front, c.rear, c.deque)
    print(86, c.insertLast(971))
    print(c.front, c.rear, c.deque)
    print(87, c.isEmpty())
    print(c.front, c.rear, c.deque)
    print(88, c.deleteLast())
    print(c.front, c.rear, c.deque)
    print(89, c.insertFront(214))
    print(c.front, c.rear, c.deque)
    print(90, c.insertLast(173))
    print(c.front, c.rear, c.deque)
    print(91, c.insertLast(962))
    print(c.front, c.rear, c.deque)

