import event
class Room():
    def __init__(self, id, name, desc):
        self.id = id
        self.name = name
        self.desc = desc
        self.paths = []
        self.rand_enc = []
        
        self.addPathStay(event.Event(0, 'Describe room', self.desc))
    
    def addPathStay(self, path):
        path.room_to = self.id
        self.paths.append(path)
    
    def __str__(self):
        return self.name + str(list(map(lambda x: x.name + '\n', self.paths)))


