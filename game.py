import json

class Player():
    def __init__(self):
        self.items = []
        self.score = 0
        self.current_room = 0
        self.nextLinked = None
    
    def choosePath(self, choiceNum):
        path = rooms[self.current_room].paths[choiceNum]
        print(path.desc)
        self.current_room = path.room_to
        self.score += path.point_change

        self.nextLinked = path.links_to
        if path.point_change > 0:
            print('You gained {} points'.format(path.point_change))
        elif path.point_change < 0:
            print('You lost {} points'.format(path.point_change))
        self.items += path.items_earned
    
    def listPaths(self):
        for p in self.getPaths():
            print(p.id, p.name)
    
    def getPaths(self):
        if self.nextLinked:
            return map(lambda x: rooms[self.current_room].paths[x], self.nextLinked)
        else:
            return filter(lambda x: x.links_from == [], rooms[self.current_room].paths)

class Event():
    def __init__(self, id, name, desc, point_change=0, room_to=-1, links_to=[], links_from=[], items_earned=[]):
        self.id = id
        self.name = name
        self.desc = desc
        self.point_change = point_change
        self.room_to = room_to
        self.links_to = links_to
        self.links_from = links_from
        self.items_earned = items_earned
    
    def __str__(self):
        return '{}-> |{}| -> {}'.format(self.links_from, self.name, self.links_to)

class Room():
    def __init__(self, id, name, desc):
        self.id = id
        self.name = name
        self.desc = desc
        self.paths = []
        self.rand_enc = []
        
        self.addPathStay(Event(0, 'Describe room', self.desc))
    
    def addPathStay(self, path):
        path.room_to = self.id
        self.paths.append(path)
    
    def __str__(self):
        return self.name + str(list(map(lambda x: x.name + '\n', self.paths)))

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

        room = Room(id, name, desc)

        for p in paths:
            path_id = p['id']
            path_name = p['name']
            path_desc = p['desc']

            room_to = saferDictGet(p, 'room_to', room.id)
            point_change = saferDictGet(p, 'point_change', 0)
            links_from = saferDictGet(p, 'links_from', [])
            links_to = saferDictGet(p, 'links_to', [])

            path = Event(path_id, path_name, path_desc, point_change, room_to, links_to, links_from)
            #print(path)
            room.paths.append(path)

        rooms[room.id] = room

# mvb11 = Room(0, 'MVB1.11', 'A dark, scary place.')
# rooms[0] = mvb11
# 
# mvb11.addPathStay(Event('Look at table', 'You look at the table.', 0))
# mvb11.addPathStay(Event('Look at floor', 'You look at the floor. Why?', -1))

p = Player()

while True:
    p.listPaths()
    p.choosePath(int(input()))