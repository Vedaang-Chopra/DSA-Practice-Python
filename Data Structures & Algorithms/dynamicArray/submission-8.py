class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.cp = capacity
        self.cur_p = 0  # size

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.cur_p == self.cp:
            self.resize()
        self.arr[self.cur_p] = n
        self.cur_p += 1

    def popback(self) -> int:
        val = self.arr[self.cur_p - 1]
        self.cur_p -= 1
        # optional cleanup
        # self.arr[self.cur_p] = None
        return val

    def resize(self) -> None:
        new_cp = self.cp * 2
        new_arr = [None] * new_cp
        for i in range(self.cur_p):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.cp = new_cp

    def getSize(self) -> int:
        return self.cur_p

    def getCapacity(self) -> int:
        return self.cp
