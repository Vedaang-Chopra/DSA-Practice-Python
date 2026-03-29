class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.cp = capacity
        self.cur_p = 0
        # print(self.array)

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.cur_p<self.cp:
            self.set(self.cur_p, n)
            self.cur_p+=1
        else:
            self.resize()
            self.set(self.cur_p, n)
            self.cur_p+=1
            
            
        # print(self.arr)

    def popback(self) -> int:
        ele = self.arr.pop(self.cur_p-1)
        self.cur_p-=1
        return ele

    def resize(self) -> None:
        self.arr += [None] * self.cp
        self.cp*=2

    def getSize(self) -> int:
        c=0
        for i in self.arr:
            if i!=None:
                c=c+1
            else:
                continue
        return c
    
    def getCapacity(self) -> int:
        return self.cp