def get_result(s):
    I=1
    V=5
    X=10
    L=50
    C=100
    D=500
    M=1000
    s='i'+s
    numbers=list()
    for i in s:
        if i=='M':
            if s[s.index(i)-1] == 'C':
                numbers.append(900)
                s=s.replace('CM','')
            else:
                # s=s.replace(s[s.index(i)],'')
                s = s[:s.index(i)] + s[s.index(i)+1:]
                numbers.append(M)
        elif i=='D':
            if s[s.index(i)-1] == 'C':
                numbers.append(400)
                s=s.replace('CD','')
            else:
                # s=s.replace(i,'')
                s = s[:s.index(i)] + s[s.index(i)+1:]
                numbers.append(D)
        elif i=='L':
            if s[s.index(i)-1] == 'X':
                numbers.append(40)
                s=s.replace('XL','')
            else:
                # s=s.replace(i,'')
                s = s[:s.index(i)] + s[s.index(i)+1:]
                numbers.append(L)
        elif i=='V':
            if s[s.index(i)-1] == 'I':
                print(s.index(i)-1)
                print(s)
                numbers.append(4)
                s=s.replace('IV','')
            else:
                #s=s.replace(i,'')
                s = s[:s.index(i)] + s[s.index(i)+1:]
                numbers.append(V)
    for i in s:
        if i=='C':
            if s[s.index(i)-1] == 'X':
                numbers.append(90)
                s=s.replace('XC','')
            else:
                # s=s.replace(i,'')
                s = s[:s.index(i)] + s[s.index(i)+1:]
                numbers.append(C)
                
    for i in s:
        if i=='X':
            if s[s.index(i)-1] == 'I':
                numbers.append(9)
                s=s.replace('IX','')
            else:
                # s=s.replace(i,'')
                s = s[:s.index(i)] + s[s.index(i)+1:]
                numbers.append(X)
            
    for i in s:
        if i=='I':
            # s=s.replace(i,'')
            numbers.append(I)
        
    return sum(numbers)
            

def main():
    s='"DCXXI"'
    get_result(s)
    
if __name__ == "__main__":
    main()