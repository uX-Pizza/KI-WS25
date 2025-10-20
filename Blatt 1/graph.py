class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.connections = []
        self.children = []
        self.h = heuristic
        self.g = 0

    def add_connection(self, connection):
        self.connections.append(connection)
        if connection.a != self and connection.a not in self.children:
            self.children.append(connection.a)
        elif connection.b not in self.connections:
            self.children.append(connection.b)

    def remove_connection(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)



class Edge:
    def __init__(self, name, cost, a, b):
        self.name = name
        self.cost = cost
        self.a = a
        self.b = b