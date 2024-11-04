import random

room_size = 2
position = (0, 0)
cleaned_rooms = set()

def move(room_size, position):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dx, dy = random.choice(directions)
    new_x, new_y = position[0] + dx, position[1] + dy
    if (0 <= new_x < room_size) and (0 <= new_y < room_size):
        return (new_x, new_y)
    return position

def clean(position, cleaned_rooms):
    if position not in cleaned_rooms:
        cleaned_rooms.add(position)
        print(f"Cleaned room at position {position}")

def run(position, room_size, cleaned_rooms):
    while len(cleaned_rooms) < room_size ** 2:
        position = move(room_size, position)
        clean(position, cleaned_rooms)
        print(f"Position: {position}, cleaned_rooms: {len(cleaned_rooms)}")

run(position, room_size, cleaned_rooms)
