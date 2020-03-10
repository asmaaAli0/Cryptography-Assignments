import sys
#needed functions
def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 

def mul_inverse(a,m):
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None  
    else: 
        return x % m

def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
    
    #------------------------------------#
def shift(op,text,key):
    out ="" 
    if op[0]=='e' :
        for cha in text:
              if cha == ' ' :
                  out+=' '
              else :
                  
                  chai = ord(cha) - ord('A')
                  chai = (chai + key) % 26
                  out += chr(chai + ord('A'))
    elif op[0]=='d' :
        for cha in text:
            if cha == ' ' :
                      out+=' '
            else :
                chai = ord(cha) - ord('A')
                chai = (chai - key) % 26
                out += chr(chai + ord('A'))
          
    return out


def Affine(op,text,a,b):
    out=""
    if op[0]=='e' :
       for cha in text:
            if cha == ' ' :
                  out+=' '
            else :
                chai = ord(cha) - ord('A')
                chai = (a * chai + b) % 26
                chai = chr(chai + ord('A')) 
                out += chai
    elif op[0]=='d' :
        
        for cha in text:
              if cha == ' ' :
                  out+=' '
              else :
                chai = ord(cha) - ord('A')
                if mul_inverse(a, 26) == None:
                    print("invalid key!!!!")
                    return ""
                chai = ((chai - b + 26) * mul_inverse(a, 26)) % 26
                chai = chr(chai + ord('A')) 
                out += chai
  
    return out



def Vigenere(op,text,key):
    out=""
    if op[0]=='e':
        key=generateKey(text,key)
        for i in range(len(key)):
            if text[i] == ' ' :
                  out+=' '
            else :
                chai = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A')) % 26
                out += chr(chai + ord('A')) 
    elif op[0]=='d' :
        

        key = generateKey(text, key)
        for i in range(len(key)):
            if text[i] == ' ' :
                  out+=' '
            else :
                chai = (ord(text[i]) - ord('A') - ord(key[i]) - ord('A') + 26) % 26
                out += chr(chai + ord('A')) 
      
    return out



if __name__ == '__main__':
    
    args = sys.argv
    alg, oper, inf, outf = args[1:5]
    
    inf = open(inf, 'r')
    text = inf.read()
    inf.close()
    

    if alg == 'shift':
        sol = ""
        a = int(args[-1])
        sol = shift(oper,text,a)
        
        
    elif alg == 'affine':
        sol = ""
        a, b = int(args[-2]), int(args[-1])
        sol = Affine(oper,text,a,b)
        
    elif alg == 'vigenere':
        sol=""
        k = args[-1]
        sol = Vigenere(oper,text,k)

    outf = open(outf, 'w')
    outf.write(str(sol))
    outf.close()






