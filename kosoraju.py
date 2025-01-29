class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, e):
        self.stack.append(e)
    
    def pop(self):
        return self.stack.pop(0)
    
    def length(self):
        return len(self.stack)


def dfs(v, G, used, S):
    used.add(v)
    for n in G[v]:
        if n not in used:
            dfs(n, G, used, S)
    S.push(v)


def dfs1(v, G, used):
    used.add(v)
    for n in G[v]:
        if n not in used:
            dfs1(n, G, used)


def invertation(G):
    res = {}
    for key, word in G.items():
        for i in word:
            if i not in res:
                res[i] = {key}
            else:
                res[i].add(key)
    return res


s = Stack()
n, m = [int(i) for i in input().split()]
a = [input().split() for _ in range(m)]
g = {}
for i in a:
    if i[0] in g:
        g[i[0]].add(i[1])
    else:
        g[i[0]] = {i[1]}
    if i[1] not in g:
        g[i[1]] = set()

used = set()
k = 0
for i in g:
    if i not in used:
        dfs(i, g, used, s)
        k += 1

sg = invertation(g)
used1 = set()
k = 0
for i in range(s.length()):
    p = s.pop()
    if p not in used1:
        k += 1
        dfs1(p, g, used1)
print(k)
    
