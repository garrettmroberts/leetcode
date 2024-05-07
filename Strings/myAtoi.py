class Solution:
    def shorten_number(self, s: str) -> str:
        if int(s) > 2**31 - 1:
            s = str(2**31 - 1)
        elif int(s) < -2**31: 
            s = str(-2**31)
        return s
    
    def myAtoi(self, s: str) -> int:
        i = 0
        started = False
        number = '0'
        for i in range(len(s)):
            if started:
                if s[i].isnumeric():
                    number += s[i]
                else:
                    return int(self.shorten_number(number))
            else:
                if s[i] == '-' or s[i] == '+':
                    number = s[i] + number
                    started = True
                elif s[i].isnumeric():
                    number += s[i]
                    started = True
                elif s[i] == ' ':
                    pass
                else:
                    return int(self.shorten_number(number))
            i += 1
                
        return int(self.shorten_number(number))