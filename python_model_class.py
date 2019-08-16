# A dictionary/object access

subscribers = [
    {'id': 1, 'name': 'Monkey', 'age': 20},
    {'id': 2, 'name': 'Dog', 'age': 31},
    {'id': 3, 'name': 'Sheep', 'age': 10},
    {'id': 4, 'name': 'Leopard', 'age': 34},
    {'id': 5, 'name': 'Lion', 'age': 4},
]

class Subscriber(dict):
    def __init__(self, record):
        pass

    def __getattr__(self, name):
        if name in self:
            return self[name]
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if name in self:
            self[name] = value
        else:
            raise AttributeError(name)

    def update(self):
        print('updated!')
        print('new values:', self.id, self.name, self.age)

    def delete(self):
        print('deleted!')

    @classmethod
    def create(cls, record):
        return cls(record)

    @classmethod
    def get_all(cls):
        print('get_all!')
        output = []
        for item in subscribers:
            output.append(cls(item))
        return output

# init sample
subscriber = Subscriber({'id': 6, 'name': 'Zebra', 'age': 65})
print(subscriber.id, subscriber['name'], subscriber.age)

# get_all
# for item in Subscriber.get_all():
#     print(item.id, item['name'], item.age)

# Update
# subscriber = Subscriber({'id': 6, 'name': 'Zebra', 'age': 65})
# print(subscriber.id, subscriber.name, subscriber.age)
# subscriber.name = 'Eddie'
# subscriber['age'] = '99'
# subscriber.update()

# Delete
# subscriber = Subscriber({'id': 6, 'name': 'Zebra', 'age': 65})
# subscriber.delete()

# Create
# subscriber = Subscriber.create({'id': 6, 'name': 'Zebra', 'age': 65})
# print(subscriber.id, subscriber.name, subscriber.age)
