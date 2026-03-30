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
        while i!=1 and i not in values:
            values.add(i)
            i=self.return_sum(i)
            print(i)
            
        return i==1
                

        