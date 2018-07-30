graph = {
    'A': ['B', 'C']
    , 'B': ['A', 'C', 'D']
    , 'C': ['A', 'B', 'D', 'E']
    , 'D': ['B', 'C', 'E', 'F']
    , 'E': ['C', 'D', 'F']
    , 'F': ['D', 'E']
}


def bfs(graph, start):
    queue = [start]
    queued = list()
    path = list()
    while queue:
        print('Queue is: %s' % queue)
        vertex = queue.pop(0)
        print('Processing %s' % vertex)
        for candidate in graph[vertex]:
            if candidate not in queued:
                queued.append(candidate)
                queue.append(candidate)
                path.append(vertex + '>' + candidate)
                print('Adding %s to the queue'
                      % candidate)
    return path


steps = bfs(graph, 'A')
print('\nBFS:', steps)
