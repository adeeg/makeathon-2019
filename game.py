class Player():
    def __init__(self):
        self.items = []
        self.score = 0
        self.current_room = 0
    
    def choosePath(self, choiceNum):
        path = rooms[self.current_room].paths[choiceNum]
        print(path.desc)
        self.current_room = path.room_to
        self.score += path.point_change
        if path.point_change > 0:
            print('You gained {} points'.format(path.point_change))
        elif path.point_change < 0:
            print('You lost {} points'.format(path.point_change))
        self.items += path.items_earned
    
    def listPaths(self):
        for p in rooms[self.current_room].paths:
            print(p.name)

class Event():
    def __init__(self, id, name, desc, point_change=0, links_to=[], items_earned=[]):
        self.id = id
        self.name = name
        self.desc = desc
        self.point_change = point_change
        #self.room_to = room_to
        self.links_to = links_to
        self.items_earned = items_earned

class Room():
    def __init__(self, id, name, desc):
        self.id = id
        self.name = name
        self.desc = desc
        self.paths = []
        self.rand_enc = []
        
        self.addPathStay(Event('Describe room', self.desc, 0))
    
    def addPathStay(self, path):
        path.room_to = self.id
        self.paths.append(path)

# id -> room
rooms = {}

mvb11 = Room(0, 'MVB1.11', 'A dark, scary place.')
rooms[0] = mvb11

mvb11.addPathStay(Event('Look at table', 'You look at the table.', 0))
mvb11.addPathStay(Event('Look at floor', 'You look at the floor. Why?', -1))

p = Player()

p.listPaths()
p.choosePath(1)
p.choosePath(2)