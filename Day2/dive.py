def clean():
    forward = 0
    down = 0

    forward2 = 0
    down2 = 0
    aim = 0
    with open('input.txt') as file:
        lines = file.readlines()
        for i in range (0,len(lines)):
            lines [i]= (lines[i]).rstrip("\n")          #macht \n raus aus dem String
            lines[i]= tuple(lines[i].split(" "))        #mach aus jedem tupel

    for i in  range (0,len(lines)):                     #mach noch zu ner funktion later
        if lines[i][0] == 'forward':                      #erste [] klammer -> wo in liste zweite [] wo in tupel
            forward += int(lines[i][1])
        elif lines[i][0] == 'down':
            down += int(lines[i][1])
        else:
            down -= int(lines[i][1])
    
    for i in range (0,len(lines)):                          # kannst in einer funktion beide addieren dann ist simpler :)
        if lines[i][0] == 'forward':
            forward2 += int(lines[i][1])
            down2 += aim*int(lines[i][1])
        elif lines[i][0] == 'down':
            aim += int(lines[i][1])
        else:
            aim -= int(lines[i][1])
    return (forward2*down2)



    #return lines

    #calulate
    #if lines[0]= 'f'
    #if lines[0]=
    #if lines[0]=
    #if lines[0]=
    
print(clean())