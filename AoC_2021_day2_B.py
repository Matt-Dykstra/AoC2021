#In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. 
#The commands also mean something entirely different than you first thought:

#down X increases your aim by X units.
#up X decreases your aim by X units.
#forward X does two things:
#It increases your horizontal position by X units.
#It increases your depth by your aim multiplied by X.
#Your horizontal position and depth both start at 0.
#What do you get if you multiply your final horizontal position by your final depth?

aim = 0
horiz = 0
depth = 0

day2input = open('day2_input.txt', 'r')

for line in day2input.read().splitlines():
    dir, dist = line.split()
    if dir == 'down':
        aim += int(dist)
    elif dir == 'up':
        aim -= int(dist)
    elif dir == 'forward':
        horiz += int(dist)
        depth += aim * int(dist)
    else:
        break
        
print (horiz * depth)
day2input.close()



