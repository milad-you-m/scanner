num = ('0','1','2','3','4','5','6','7','8','9')
alph = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_')
keywords = ('int', 'float', 'if', 'else', 'while', 'for','long', 'double')
point = '.'
exponent = ('e','E')
sign = ('+','-')
ch = ('(',')','{','}')

class scanner :
    def __init__(self) :
        self.state = 0
        self.char = ''
        self.word = ''
        self.file = open('./input.txt', 'r')
        self.output = open('./output.txt', 'w')

    def scan(self):
        while True :
            self.char = self.file.read(1)
            self.char.lower()
            self.word += self.char
            match self.state :
                case 0:     #intiger DFA (q0)
                    if  self.char  in num:
                        self.state = 1
                    elif self.char in sign :
                        self.state = 2
                    else :
                        self.state = 6
                case 1:     #intiger DFA (q1)
                    if self.char in num :
                        self.state = 1
                    elif self.char in exponent :
                        self.state = 3
                    elif self.char == " " or self.char == "\n" :
                        self.output.write(self.word,' is intiger\n')
                        self.word = ''
                        self.state = 0
                    else :
                        self.state = 8
                case 2:    #intiger DFA (q2)
                    if self.char in num :
                        self.state = 1
                    else :
                        self.state = 8
                case 3:   #intiger DFA (q3)
                    if self.char in num :
                        self.state = 5
                    elif self.char in sign :
                        self.state = 4
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 4: #intiger DFA (q4)
                    if self.char in num :
                        self.state = 5
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 5:  #intiger DFA (q5)
                    if self.char in num :
                        self.state = 5
                    elif self.char == " " or self.char == "\n" :
                        self.output.write(self.word,' is intiger\n')
                        self.word = ''
                        self.state = 0
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 6: #float DFA (q6)
                    if self.char == point :
                        self.state = 7
                    else :
                        self.state = 16
                case 7: #float DFA (q7)
                    if self.char in num :
                        self.state = 10
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 8: #float DFA (q8)
                    if self.char == point :
                        self.state = 7
                    elif self.char in num :
                        self.state = 9
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 9: #float DFA (q9)
                    if self.char in num :
                        self.state = 9
                    elif self.char == point :
                        self.state = 11
                    else :
                        self.output.write(self.word,' not recognized\n')
                        self.word = ''
                        self.state = 0
                case 10: #float DFA (q10)
                    if self.char in num :
                        self.state = 10
                    elif self.char in exponent :
                        self.state = 13
                    elif self.char == " " or self.char == "\n" :
                        self.output.write(self.word,' is float\n')
                        self.word = ''
                        self.state = 0
                    else :
                        self.output.write(self.word,' not recognized\n')
                        self.word = ''
                        self.state = 0
                case 11: #float DFA (q11)
                    if self.char in num :
                        self.state = 12
                    elif self.char in exponent :
                        self.state = 13
                    elif self.char == " " or self.char == "\n" :
                        self.output.write(self.word,' is float\n')
                        self.word = ''
                        self.state = 0
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 12: #float DFA (q12)
                    if self.char in num :
                        self.state = 12
                    elif self.char in exponent :
                        self.state = 13
                    elif self.char == " " or self.char == "\n" :
                        self.output.write(self.word,' is float\n')
                        self.word = ''
                        self.state = 0
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 13: #float DFA (q13)
                    if self.char in num :
                        self.state = 15
                    elif self.char in sign :
                        self.state = 14
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 14: #float DFA (q14)
                    if self.char in num :
                        self.state = 15
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 15: #float DFA (q15)
                    if self.char in num :
                        self.state = 15
                    elif self.char == " " or self.char == "\n" :
                        self.output.write(self.word,' is float\n')
                        self.word = ''
                        self.state = 0
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 16: #identifier DFA (q16)
                    if self.char in alph :
                        self.state = 17
                    else :
                        self.state = 18
                case 17: #identifier DFA (q17)
                    if self.char in alph or self.char in num :
                        self.state = 17
                    elif self.char == " " or self.char == "\n" :
                        if self.word in keywords :
                            self.output.write(self.word,' is keyword\n')
                        else :
                            self.output.write(self.word,' is identifier\n')
                        self.word = ''
                        self.state = 0
                    else :
                        self.state = 18
                case 18: #string DFA (q18)
                    if self.char == '"' :
                        self.state = 19
                    else :
                        self.state = 21
                case 19: #string DFA (q19)
                    if self.char != '"' :
                        self.state = 19
                    else :
                        self.state = 20
                case 20: #string DFA (q20)
                    self.output.write(self.word,' is string\n')
                    self.word = ''
                    self.state = 0
                case 21: #char DFA (q21)
                    if self.char == "'" :
                        self.state = 22
                    else :
                        self.state = 25
                case 22: #char DFA (q22)
                    if self.char != "'" :
                        self.state = 23
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 23: #char DFA (q23)
                    if self.char == "'" :
                        self.state = 24
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 24: #char DFA (q24)
                    self.output.write(self.word,' is charachter\n')
                    self.word = ''
                    self.state = 0
                case 25: #comment DFA (q25)
                    if self.char == '/' :
                        self.state = 26
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 26: #comment DFA (q26)
                    if self.char == '/' :
                        self.state = 27
                    elif self.char == '*' :
                        self.state = 29
                    else :
                        self.output.write(self.word,' is not recognized\n')
                        self.word = ''
                        self.state = 0
                case 27: #comment DFA (q27)
                    if self.char != '\n' :
                        self.state = 27
                    else :
                        self.state = 28
                case 28: #comment DFA (q28)
                    self.word = ''
                    self.state = 0
                case 29: #comment DFA (q29)
                    if self.char != '*' :
                        self.state = 29
                    else :
                        self.state = 30
                case 30: #comment DFA (q30)
                    if self.char == '/' :
                        self.state = 28
                    else :
                        self.state = 29
        
        
        self.file.close()
        self.output.close()


if __name__ == '__main__':
    s = scanner()
    s.scan()