#https://programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10**4)

class Node():
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.left = None
        self.right = None
    
    def listPre(self):
        lPre = [self.n]
        if self.left:
            lPre += self.left.listPre()
        if self.right:
            lPre += self.right.listPre()
        return lPre
    
    def listPost(self):
        lPost = []
        if self.left:
            lPost += self.left.listPost()
        if self.right:
            lPost += self.right.listPost()
        lPost += [self.n]
        return lPost
    
    def addNode(self,node):
        # assume self.y > node.y
        if self.x > node.x:
            if self.left == None:
                self.left = node
            else:
                self.left.addNode(node)
        else:
            if self.right == None:
                self.right = node
            else:
                self.right.addNode(node)

def solution(nodeinfo):
    dnodes = dict()
    
    for i in range(len(nodeinfo)):
        x,y = nodeinfo[i]
        node = Node(i+1,x,y)
        if y in dnodes:
            dnodes[y].append(node)
        else:
            dnodes[y] = [node]
    
    ys = sorted(list(dnodes.keys()), reverse=True)
    
    root = dnodes[ys[0]][0]
    
    for lv, y in enumerate(ys):
        if lv==0: continue
        else:
            for node in dnodes[y]:
                root.addNode(node)
    
    return [root.listPre(), root.listPost()]
