import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.state = parent
        self.state = action

class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.fronteir[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[:1]
            return node

class Maze():
    def __init__(self, filename):
        with open(filename) as f:
            pass

# paused at 46:50, need an OOP refresher