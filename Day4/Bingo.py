def bingo():
    with open ('input.txt') as file:
        lines = [l.rstrip() for l in file.readlines()]     
        
    bingonumbers = lines[0:1]
    
    

    bingonumbers = ''.join(bingonumbers)

    

    bingonumbers = bingonumbers.split(',')

    

    fields = lines[1:]
    
    fields=[l.split() for l in fields]

    
    for x in bingonumbers:                      
        for j in range (len(fields)):
            for i in range (len(fields[j])):
                if fields[j][i] == x:
                    fields[j][i] = int(fields[j][i])
                    result = bingocheck(fields)                                   #schauen ob bingo
                    if result is not None:
                        return result*int(x)
    
    
def bingocheck(fields):
    for j in range (len(fields)):
        if fields[j] == []:
            num = j+1
        for i in range (len(fields[j])):
            if isinstance(fields[j][i],int):
                bingo = True
                for k in range (5):                     #Zeile
                    if not isinstance(fields[j][k],int):
                        bingo = False
                if bingo:
                    return bingocount(fields,num)
                bingo = True
                for l in range (num,num+5):             #num
                    if not isinstance(fields[l][i],int):
                        bingo = False
                if bingo:
                    return bingocount(fields,num)

def bingocount(fields,num):
    result = 0
    for j in range (5):
        for i in range (num,num+5):
            if not isinstance(fields[i][j],int):
                result += int(fields[i][j])

    return result

print(bingo())