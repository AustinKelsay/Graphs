from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "/home/aus/Desktop/Lambda/Projects/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


opposites = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
traversal_graph = {}
def traverse_graph():
    moves = []
    traversal_graph[player.current_room.id] = {}
    for cur_direction in player.current_room.get_exits():
        prev = player.current_room.id
        player.travel(cur_direction)
        traversal_graph[prev][cur_direction] = player.current_room.id
        if player.current_room in visited_rooms:
            player.travel(opposites[cur_direction])
        else:
            visited_rooms.add(player.current_room)
            moves.append(cur_direction)
            moves.extend(traverse_graph())
            player.travel(opposites[cur_direction])
            moves.append(opposites[cur_direction])
    return moves


traversal_path = traverse_graph()






if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
