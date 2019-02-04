import random

class Player():
    def __init__(self, rooms):
        self.items = []
        self.score = 0
        self.current_room = 0
        self.nextLinked = None
        self.rooms = rooms
    
    def choosePath(self, choiceNum):
        #if random.randint(0,1):
        path = self.rooms[self.current_room].paths[choiceNum]
        if self.getCurrentRoom().rand_enc and random.random() > 0.7:
            # random enc.
            num = random.randint(0, len(self.getCurrentRoom().rand_enc) - 1)
            path = self.getCurrentRoom().rand_enc[num]
        
        print(path.desc)
        self.current_room = path.room_to
        self.score += path.point_change

        self.nextLinked = path.links_to
        if path.point_change > 0:
            print('You gained {} points'.format(path.point_change))
        elif path.point_change < 0:
            print('You lost {} points'.format(path.point_change))
        self.items += path.items_earned
    
    def getCurrentRoom(self):
        return self.rooms[self.current_room]
    
    def listPaths(self):
        for p in self.getPaths():
            print(p.id, p.name)
    
    def getPaths(self):
        if self.nextLinked:
            return map(lambda x: self.rooms[self.current_room].paths[x], self.nextLinked)
        else:
            return filter(lambda x: x.links_from == [], self.rooms[self.current_room].paths)


