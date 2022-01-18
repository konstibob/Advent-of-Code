def crabs():
    with open('input.txt') as file:
        lines = [l.rstrip() for l in file.readlines()]
    lines =','.join(lines)
    lines = lines.split(',')
    for i in range (0,len(lines)):
        lines[i] = int(lines[i])
    result = addon(lines)

    return result

def addon(lines):                               #anders berechnen -> den median vs avarage -> ungerade Anzahl an werten/ gerade anzahl an werten
    lines.sort()
    solution = 0
    if len(lines) % 2 == 0:                     #defenition des Median
        median = lines[(len(lines))//2]
    else:
        median = round(((lines[(len(lines))//2] + lines[(len(lines))//2 + 1])/2),0)
    for i in range (0,len(lines)):
        solution += abs(median-lines[i])
    return solution

print(crabs())