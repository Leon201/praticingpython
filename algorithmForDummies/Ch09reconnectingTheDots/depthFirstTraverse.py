graph = {
    'A': ['B', 'C']
    , 'B': ['A', 'C', 'D']
    , 'C': ['A', 'B', 'D', 'E']
    , 'D': ['B', 'C', 'E', 'F']
    , 'E': ['C', 'D', 'F']
    , 'F': ['D', 'E']
}

def dfs(graph, start):
    stack = [start]
    parents = {start: start}
    path = list()
    while stack:
        print ('Stack is : %s' % stack)
        vertex = stack.pop(-1)
        print ('Processing %s' % vertex)
        for candidate in graph[vertex]:
            if candidate not in parents:
                parents[candidate] = vertex
                stack.append(candidate)
                print ('Adding %s to the stack'
                       % candidate)
        path.append(parents[vertex] + '>' + vertex)
    return path[1:]

steps = dfs(graph, 'A')
print('\nDFS:', steps)