import random

roomsize = 2
pos = (0,0)
cleanroom = set()

def posi(pos,roomsize):
    options = [(0,1),(1,0),(0,-1),(-1,0)]
    x,y = random.choice(options)
    new_x, new_y = (pos[0] + x, pos[1] + y)
    if (0 <= new_x < roomsize) and (0 <= new_y < roomsize):
        return (new_x,new_y)
    return pos

def clean(position,cleanroom):
    if position not in cleanroom:
        cleanroom.add(position)
        print(f'Cleaned at {position}')

def run(roomsize,pos,cleanroom):
    while len(cleanroom) < roomsize ** 2:
        pos = posi(pos,roomsize)
        clean(pos,cleanroom)
        print(f'Curr pos : {pos} , CleanRoom : {len(cleanroom)}')

run(roomsize,pos,cleanroom)
