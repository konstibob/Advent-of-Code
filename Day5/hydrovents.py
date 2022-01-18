def hydros():
    
    with open('input.txt') as file:
        lines = [l.rstrip() for l in file.readlines()]
    
    lines = " -> ".join(lines)                  #lücken damit deckungsgleich
    lines = lines.replace(',',' -> ')
    
    lines = lines.split(' -> ')
    
    
    hydros = [(int(lines[i]),int(lines[i+1])) for i in range (0,len(lines),2)]     #Tupel Nr 1 = x1,y1 Koordinaten
                                                                             #Tupel Nr 2 = x1,y2 wohin die Zahl geht
    
    result = calc(hydros)

    return result

def calc(hydros):                                 
    hydromap = []                                        
    for i in range (0,len(hydros)-1,2):             
        if hydros[i][0] == hydros[i+1][0]:        #wenn die erste Zahl von beiden Tupeln gleich ist
            if hydros[i][1] > hydros[i+1][1]:     
                for j in range ((hydros[i+1][1]),(hydros[i][1])+1):
                    hydromap.append((hydros[i][0],j))
            elif hydros[i][1] < hydros[i+1][1]:
                for j in range ((hydros[i][1]),(hydros[i+1][1])+1):
                    hydromap.append((hydros[i][0],j))

        elif hydros[i][1] == hydros[i+1][1]:        #wenn die zweite Zahl von beiden Tupeln gleich ist
            if hydros[i][0] > hydros[i+1][0]:
                for j in range ((hydros[i+1][0]),(hydros[i][0])+1):
                    hydromap.append((j,hydros[i][1]))
            elif hydros[i][0] < hydros[i+1][0]:
                for j in range ((hydros[i][0]),(hydros[i+1][0])+1):
                    hydromap.append((j,hydros[i][1]))

    number = checkfordoubles(hydromap)
    return number

def checkfordoubles(map):
    overlap = set()
    map.sort()
    for i in range (0,len(map)-1):
        if map[i] == map[i+1]:
            overlap.add(map[i]) 
    return len(overlap)
    
    


print(hydros())