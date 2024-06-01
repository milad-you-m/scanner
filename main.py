num = ('0','1','2','3','4','5','6','7','8','9')
alph = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_')
keywords = ('int', 'float', 'if', 'else', 'while', 'for','long', 'double')
point = '.'
exponent = ('e','E')
sign = ('+','-')
symbol = ('(',')','{','}')
operator = ('+','-','*','/','++','--','+=','-=','*=','/=')

class scanner :
    def __init__(self) :
        self.next = 0
        self.state = 0
        self.char = ''
        self.word = ''
        self.file = open('./input.txt', 'r')
        self.output = open('./output.txt', 'w')
        self.output.write('-------------This is the output of the scanner------------')

    def scan(self):
        while True :
            if (self.next == self.state):
                self.char = self.file.read(1)
                if ((self.char==" " or self.char=="\n")and self.state==0) :
                    continue
                self.char = self.char.lower()
                self.word += self.char
            else :
                self.state = self.next
            match self.state :
                case 0:     #intiger DFA (q0)
                    if  self.char  in num:
                        self.state = 1
                        self.next = 1
                    elif self.char in sign :
                        self.state = 2
                        self.next = 2
                    else :
                        self.next = 6
                case 1:     
                    if self.char in num :
                        self.state = 1
                        self.next = 1
                    elif self.char in exponent :
                        self.state = 3
                        self.next = 3
                    elif self.char == " " or self.char == "\n" :
                        self.output.write('\n'+self.word[:self.word.__len__()-1]+' is intiger')
                        self.word = ''
                        self.state = 0
                        self.next = 0
                    else :
                        self.next = 8
                case 2:   
                    if self.char in num :
                        self.state = 1
                        self.next = 1
                    else :
                        self.next = 8
                case 3:   
                    if self.char in num :
                        self.state = 5
                        self.next = 5
                    elif self.char in sign :
                        self.state = 4
                        self.next = 4
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                        
                case 4:
                    if self.char in num :
                        self.state = 5
                        self.next = 5
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 5:  
                    if self.char in num :
                        self.state = 5
                        self.next = 5
                    elif self.char == " " or self.char == "\n" or self.char == '':
                        self.output.write('\n'+self.word[:self.word.__len__()-1]+' is intiger')
                        self.word = ''
                        self.state = 0
                        self.next = 0
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 6: #float DFA (q6)
                    if self.char == point :
                        self.state = 7
                        self.next = 7
                    else :
                        self.next = 16
                case 7: 
                    if self.char in num :
                        self.state = 10
                        self.next = 10
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 8: 
                    if self.char == point :
                        self.state = 7
                        self.next = 7
                    elif self.char in num :
                        self.state = 9
                        self.next = 9
                    else:
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 9:
                    if self.char in num :
                        self.state = 9
                        self.next = 9
                    elif self.char == point :
                        self.state = 11
                        self.next = 11
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 10:
                    if self.char in num :
                        self.state = 10
                        self.next = 10
                    elif self.char in exponent :
                        self.state = 13
                        self.next = 13
                    elif self.char == " " or self.char == "\n" :
                        self.output.write('\n'+self.word[:self.word.__len__()-1]+' is float')
                        self.word = ''
                        self.state = 0
                        self.next = 0
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 11: 
                    if self.char in num :
                        self.state = 12
                        self.next = 12
                    elif self.char in exponent :
                        self.state = 13
                        self.next = 13
                    elif self.char == " " or self.char == "\n" :
                        self.output.write('\n'+self.word[:self.word.__len__()-1]+' is float')
                        self.word = ''
                        self.state = 0
                        self.next = 0
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 12:
                    if self.char in num :
                        self.state = 12
                        self.next = 12
                    elif self.char in exponent :
                        self.state = 13
                        self.next = 13
                    elif self.char == " " or self.char == "\n" :
                        self.output.write('\n'+self.word[:self.word.__len__()-1]+' is float')
                        self.word = ''
                        self.state = 0
                        self.next = 0
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 13: 
                    if self.char in num :
                        self.state = 15
                        self.next = 15
                    elif self.char in sign :
                        self.state = 14
                        self.next = 14
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 14: 
                    if self.char in num :
                        self.state = 15
                        self.next = 15
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 15: 
                    if self.char in num :
                        self.state = 15
                        self.next = 15
                    elif self.char == " " or self.char == "\n" :
                        self.output.write('\n'+self.word[:self.word.__len__()-1]+' is float')
                        self.word = ''
                        self.state = 0
                        self.next = 0
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 16: #identifier DFA (q16)
                    if self.char in alph :
                        self.state = 17
                        self.next = 17
                    else :
                        self.next = 18
                case 17:
                    if self.char in alph or self.char in num :
                        self.state = 17
                        self.next = 17
                    elif self.char == " " or self.char == "\n" :
                        if self.word.strip() in keywords :
                            self.output.write('\n'+self.word[:self.word.__len__()-1]+' is keyword')
                        else :
                            self.output.write('\n'+self.word[:self.word.__len__()-1]+' is identifier')
                        self.word = ''
                        self.state = 0
                        self.next = 0
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 18: #string DFA (q18)
                    if self.char == '"' :
                        self.state = 19
                        self.next = 19
                    else :
                        self.next = 21
                case 19: 
                    if self.char == '' :
                        self.output.write('\n'+self.word[:self.word.__len__()-1].replace('\n', '') + ' is not recognized')
                    elif self.char != '"' :
                        self.state = 19
                        self.next = 19
                    else :
                        self.state = 20
                        self.next = 20
                case 20: 
                    self.output.write('\n'+self.word[:self.word.__len__()-1]+' is string')
                    self.word = ''
                    self.state = 0
                    self.next = 0
                case 21: #char DFA (q21)
                    if self.char == "'" :
                        self.state = 22
                        self.next = 22
                    else :
                        self.next = 25
                case 22: 
                    if self.char != "'" :
                        self.state = 23
                        self.next = 23
                    else :
                        self.state = 24
                        self.next = 24
                case 23: 
                    if self.char == "'" :
                        self.state = 24
                        self.next = 24
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 24: 
                    self.output.write('\n'+self.word[:self.word.__len__()-1]+' is charachter')
                    self.word = ''
                    self.state = 0
                    self.next = 0
                case 25: #comment DFA (q25)
                    if self.char == '/' :
                        self.state = 26
                        self.next = 26
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 26: 
                    if self.char == '/' :
                        self.state = 27
                        self.next = 27
                    elif self.char == '*' :
                        self.state = 29
                        self.next = 29
                    else :
                        if (self.word in operator ):
                            self.output.write('\n'+self.word +' is operator')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        elif (self.word in symbol ):
                            self.output.write('\n'+self.word +' is symbol')
                            self.word = ''
                            self.state = 0
                            self.next = 0
                        else :
                            self.next = -1
                case 27: 
                    if self.char != '\n' :
                        self.state = 27
                        self.next = 27
                    else :
                        self.state = 0
                        self.next = 0
                        self.word =''
                case 29: 
                    if self.char != '*' :
                        self.state = 29
                        self.next = 29
                    else :
                        self.state = 30
                        self.next = 30
                case 30: 
                    if self.char == '/' :
                        self.state = 0
                        self.next = 0
                        self.word = ''
                    else :
                        self.state = 29
                        self.next = 29
                case -1:
                    while self.char != ' ' and self.char != '\n' and self.char != '':
                        self.char = self.file.read(1)
                        self.word += self.char
                    self.output.write('\n'+self.word[:self.word.__len__()-1]+' is not recognized')
                    self.word = ''
                    self.state = 0
                    self.next = 0
            if self.char == '' :
                break
            else :
                continue
        
        self.file.close()
        self.output.close()


if __name__ == '__main__':
    s = scanner()
    s.scan()