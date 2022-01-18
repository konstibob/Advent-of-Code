fishamt = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,"newborn":0}

def rate():
    with open('input.txt') as file:
        lines = [l.rstrip() for l in file.readlines()]      #arrays kopieren geht nicht gut :(
    lines = ','.join(lines)
    lines = lines.split(',')

    for i in range (0,len(lines)):                          #macht zu integern -> geht safe alles schneller
        lines[i] = int(lines[i])
    
    lines2 = lines[:]
                                                #mach so gruppen von tupeln die sagen wie viele 1,2..8 es jeweils gibt
    result = simulate(lines)
    
    result2 = group(lines2)

    return (result,result2)

def simulate(fish):
    for j in range(0,80):
        steps = len(fish)
        for i in range(0,steps):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] = fish[i]-1
    return len(fish)

def group(fish):
    answer = 0
    transfer(fish)
    for j in range(257):                          #irgendwas falsch oder so
        fishamt['newborn'] = fishamt[0]            #ort richtig??
        for k in range (8):                      
            fishamt[k] = fishamt[k+1]
        fishamt[6] += fishamt['newborn']
        fishamt[8] = fishamt['newborn']
    for i in range (0,8):
        answer += fishamt[i]
    return answer
    
                                                    #calculate with new values#
            
def transfer(fish):
    for i in range (0,len(fish)):
        fishamt[fish[i]] += 1
    # fish0 -> fish 6 und fish von 8 genausoviele
    #fish andere gehen 1 runter



#for i in range (0,len(lines)):
#            fishamt["amt0"] += 1 
#        return fishamt["amt0"]
                                                            #while nicht am ende der liste angekommen
                                                            #am anfang länge der liste messen


print (rate())