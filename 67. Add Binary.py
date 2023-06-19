class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        x = int(a, 2)
        y = int(b,2)
        return bin(x + y)[2:]
        '''

        sum_b = ""
        carry = 0
        if len(a) > len(b):
            for i in range(len(b), len(a)):
                b = '0' + b
        else:
            for i in range(len(a), len(b)):
                a = '0' + a
        for i in range(len(a)-1,-1,-1):

            temp = int(a[i]) + int(b[i]) + carry 
            if temp == 0:
                sum_b = "0" + sum_b
                carry = 0
            elif temp == 1:
                sum_b = "1" + sum_b
                carry = 0
            elif temp == 2:
                sum_b = "0" + sum_b
                carry = 1
            else:
                sum_b = "1" + sum_b
                carry = 1
        if carry == 1:
            sum_b = "1" + sum_b
        return sum_b