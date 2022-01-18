def search():
    with open('input.txt') as f:
        lines = f.readlines()
        for i in range (0,len(lines)):
            lines [i]= (lines[i]).rstrip("\n")          #macht \n raus aus dem String
            lines [i]= int(lines[i])                    #macht '' raus aus dem String

    result = sum(lines)
    result2 = trisum(lines)
    return (result,result2)

def sum(lines):
    count = 0
    for i in range (0,len(lines)-1):
        if (lines [i]<lines [i+1]):
            count += 1
    return count

def trisum(lines):
    count = 0
    for i in range (0,len(lines)-3): 
        if((lines[i]+lines[i+1]+lines[i+2])<(lines[i+1]+lines[i+2]+lines[i+3])):
            count += 1
    return count

print(search())