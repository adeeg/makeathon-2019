import json
import random
import player
import event
import room as roomFile
import ser
from threading import Thread

# id -> room
rooms = {}

def saferDictGet(d, key, default=None):
    return default if key not in d else d[key]

# load json
with open('rooms.json', 'r') as f:
    data = json.load(f)
    for r in data:
        # parse room
        id = r['id']
        name = r['name']
        desc = r['desc']
        paths = r['paths']
        rand_enc = saferDictGet(r, 'rand_enc', [])

        room = roomFile.Room(id, name, desc)

        for p in paths:
            path_id = p['id']
            path_name = p['name']
            path_desc = p['desc']

            room_to = saferDictGet(p, 'room_to', room.id)
            point_change = saferDictGet(p, 'point_change', 0)
            links_from = saferDictGet(p, 'links_from', [])
            links_to = saferDictGet(p, 'links_to', [])

            path = event.Event(path_id, path_name, path_desc, point_change, room_to, links_to, links_from)
            #print(path)
            room.paths.append(path)
        
        for p in rand_enc:
            # yes i am aware this is copy pasted sue me
            path_id = p['id']
            path_name = p['name']
            path_desc = p['desc']

            room_to = saferDictGet(p, 'room_to', room.id)
            point_change = saferDictGet(p, 'point_change', 0)
            links_from = saferDictGet(p, 'links_from', [])
            links_to = saferDictGet(p, 'links_to', [])

            path = event.Event(path_id, path_name, path_desc, point_change, room_to, links_to, links_from)
            room.rand_enc.append(path)

        rooms[room.id] = room

# mvb11 = Room(0, 'MVB1.11', 'A dark, scary place.')
# rooms[0] = mvb11
# 
# mvb11.addPathStay(Event('Look at table', 'You look at the table.', 0))
# mvb11.addPathStay(Event('Look at floor', 'You look at the floor. Why?', -1))

p = player.Player(rooms)
serThread = Thread(target=ser.thread1, args=("Ser thead". ))

while True:
    print ("===== {} =====".format(rooms[p.current_room].name))
    p.listPaths()
    p.choosePath(int(input()))
    print()
    print("Test: {}".format(ser.keyDown))
serThread.join()
