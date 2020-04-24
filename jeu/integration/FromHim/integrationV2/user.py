import json

class User(object):
    """docstring for User."""

    def __init__(self, name):
        self.data = False
        self.name = name
        self.open()
        self.addUser() #add an user if the name is not in the dict

    def save(self):
        with open('user.json', 'w') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def open(self):
        with open('user.json') as f:
            self.data = json.load(f)

    def print(self, user = False):
        if user:
            print(self.data['victor'])
        else:
            print(self.data)

    def addUser(self):
        for k, v in self.data.items():
            if k == self.name:
                return
        self.data.update({self.name : {"apocalypse":0,"normal":0,"propagation":0}})

    def score(self, gameMode, score):
        self.data[self.name][gameMode] = self.data[self.name][gameMode] + score

    def getData(self):
        return self.data[self.name]



u = User('test')
u.score("apocalypse", 10)
data = u.getData()
print(data["apocalypse"])
u.save()
