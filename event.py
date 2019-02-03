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


