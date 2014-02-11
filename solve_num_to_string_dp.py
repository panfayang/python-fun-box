class NumToString():
    def __init__(self):
        self.dic = {}
        for i in range(26):
            self.dic[i+1] = chr(97+i)
            
    def decode(self, num):
        result = []
        if len(num) ==0:
            return [""]
        if len(num)==1:
            return [self.dic[int(num)]]
        if len(num)>1:
            lastTwo = int(num[-2]+num[-1])
            last = int(num[-1])
            if lastTwo<27:
                return [string + self.dic[lastTwo] for string in self.decode(num[0:-2])] +[string + self.dic[last] for string in self.decode(num[0:-1])]
            else:
                return [string + self.dic[last] for string in self.decode(num[0:-1])]
        else:
           last = num[0]
           return [string + self.dic[last] for string in self.decode(num[0:-1])]

    def decoder(self,num):
        if isinstance(num, int):
            return self.decode(str(num))
        else:
            return "invalid input"
        
hello = NumToString()
print hello.decoder(1123)
