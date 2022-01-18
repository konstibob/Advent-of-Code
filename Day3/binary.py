def report():
    with open ('input.txt') as f:
        lines = [i.rstrip() for i in f.readlines()]  
    
    result = rate(lines)        
    return result

def rate(arr):
    count = 0
    gamma_rate = []
    epsilon_rate = []
    for j in range (12):              #hardcoded 
        for i in range (len(arr)):        
            if arr[i][j] == '1':
                count += 1
            else:
                count -= 1 
        if count > 0:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)
        count = 0
    result = convert(epsilon_rate,gamma_rate)
    return result

def convert(epsilon_rate,gamma_rate):
    epsilon = 0
    gamma = 0
    for i in range (len(epsilon_rate)):
        if epsilon_rate[i] == 1:
            epsilon *= 2
            epsilon += 1
        else:
            epsilon *= 2

    for i in range (len(gamma_rate)):
        if gamma_rate[i] == 1:
            gamma *= 2
            gamma += 1
        else:
            gamma *= 2
    
    return epsilon*gamma

print(report())