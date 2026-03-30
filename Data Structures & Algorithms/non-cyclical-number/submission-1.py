class Solution:
    def return_sum(self, i):
        sum=0
        # print(i)
        while i >0:
            print(i, end='')
            digit= i%10
            sum+=(digit**2)
            i=i//10
            print(",", i)
        print("sum:", sum)
        return sum

    def isHappy(self, n: int) -> bool:
        values =set()
        # print((i//100)%10)
        i=n
        while True:
            val=self.return_sum(i)
            print(val)
            if val==1:
                return True
            if val in values:
                break
            else:
                values.add(val)
            i=val
        return False
                

        