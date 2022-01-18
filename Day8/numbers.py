from collections import defaultdict


def numbers():
    with open ('input.txt') as file:
        decoded = [l.rstrip() for l in file.readlines()]

    task1 = decoded[:]

    task2 = decoded[:]
    task2 = [s.split(' ') for s in task2]

    for i in range(len(task2)):
        for j in range (len(task2[i])):
            task2[i][j] = set(task2[i][j])                  #macht aus strings sets
                
    
    result = countone(task1)                                #counts number of 1, 4, 7 and 8 on right side

    result2 = addall(task2)

    return result2


def findNumbers(encodingArray):
    # returns {encoding_set: number}
    return 

def countone(coding):
    count = 0
    for i in range (0,len(coding)):
        for j in range (0,len(coding[i])):
            if coding[i][j] == '|':
                words = (coding[i])[j+2:len(coding[i])].split(' ')
                words = list(map(len,words))
                for k in range(0,len(words)):
                    if words[k] in [2,3,4,7]:
                        count += 1
    return count

def addall(coding):
    result = 0
    for i in range(len(coding)):
        numbers = defaultdict(lambda:0)
        wires = {}
        for j in range(len(coding[i])):
            if len(coding[i][j]) == 2:             #finds the top Element 
                numbers[1] = coding[i][j]
            if len(coding[i][j]) == 3:
                numbers[7] = coding[i][j]
            if(len(coding[i][j]) == 4):
                numbers[4] = coding[i][j]
            if(len(coding[i][j]) == 7):
                numbers[8] = coding[i][j]

            if numbers[7] != 0 and numbers[1] != 0:
                wires['toptop'] = numbers[7] - numbers[1]  #wires['top'] -> top in number 
        
        for j in range (len(coding[i])):
            if len(coding[i][j]) == 6 and len(coding[i][j] - numbers[1]) == 5:      #find 6 in row
                wires['topright'] = numbers[1] - coding[i][j]                       #
                wires['downright'] = numbers[1] - wires['topright']                 #
            
        for j in range (len(coding[i])):
            if len(coding[i][j]) == 6 and len(coding[i][j]-numbers[4]) == 2:        #find 9 in row
                wires['downdown'] = coding[i][j] - (numbers[4] | numbers[7])        #sets 4 and 7 comined
                
        for j in range (len(coding[i])):                                            #du brauchst den if dings garnicht
            if len(coding[i][j]) == 7:
                wires['downleft'] = coding[i][j] - (numbers[4] |wires['toptop']|wires['downdown'])
                
        for j in range (len(coding[i])):
            if len(coding[i][j]) == 6 and len(coding[i][j]-((wires['topright'])|wires['downleft'])) == 4:
                wires['topleft'] = coding[i][j]-(numbers[7] | wires['downdown'] | wires['downleft'])

        for j in range (len(coding[i])):
            wires['mid'] = numbers[4] - (numbers[1] | wires['topleft']) 

        
        arrofnums = findnums(wires,findsymbol(coding[i]))
        result += transform(arrofnums)
    return result
        

def findsymbol(list):
    i = 0
    startofnum = set('|')
    while(list[i] != startofnum):
        del list[0]
    del list[0]
    return list

def findnums(wires,symbols):            #check if numbers are right
    for j in range (len(symbols)):
        if symbols[j] == (wires['toptop'] | wires['topleft'] |wires['topright'] | wires['downleft'] | wires['downdown'] | wires['downright']):
            symbols[j] = 0
        elif symbols[j] == (wires['topright'] |(wires['downright'])):
            symbols[j] = 1
        elif symbols[j] == (wires['toptop'] |wires['mid'] | wires['downleft'] | wires['downdown'] | wires['topright']):
            symbols[j] = 2
        elif symbols[j] == (wires['toptop'] |wires['mid'] | wires['downright'] | wires['downdown'] | wires['topright']):
            symbols[j] = 3
        elif symbols[j] == (wires['topleft'] |(wires['downright']) | wires['mid'] | wires['topright']):
            symbols[j] = 4
        elif symbols[j] == (wires['toptop'] | wires['topleft'] |wires['mid'] | wires['downdown'] | wires['downright']):
            symbols[j] = 5
        elif symbols[j] == (wires['toptop'] | wires['topleft'] |wires['mid'] | wires['downleft'] | wires['downdown'] | wires['downright']):
            symbols[j] = 6
        elif symbols[j] == (wires['topright'] | (wires['downright']) | wires['toptop']):
            symbols[j] = 7
        elif symbols[j] == (wires['toptop'] | wires['topleft'] |wires['mid'] | wires['downdown'] | wires['downright'] | wires['topright']):
            symbols[j] = 9
        else:
            symbols[j] = 8
    print(symbols)
    return symbols

def transform(arr):
    num = 0
    while arr != []:
        num *= 10
        num += arr[0]
        del arr [0]
    return num

print(numbers())