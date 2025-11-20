# CMPS 2200 Recitation 08

## Answers

**Name:**Hoang Dieu Linh Nguyen
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
+) Work:
The algorithm is a modified Dijkstra’s algorithm (breaking ties by number of edges). Each edge relaxation involves a priority-queue operation (push/pop), which costs O(log V), and each edge is relaxed at most once.
=> Work = O(E log V)

+) Span:
Since the algorithm is fully sequential and each relaxation may depend on the previous one, the longest dependency chain is proportional to the number of edges.
=> Span = O(E)



- **2b)**
+) Work of bfs_path:
BFS visits each vertex and edge once.
=> Work = O(V + E)

+) Span of bfs_path:
BFS proceeds level-by-level, and without parallelism the longest level chain is O(V).
=> Span = O(V)

+) Work of get_path:
Reconstructing the path walks up the BFS tree from the destination to the root, at most V steps.
=> Work = O(V)

+) Span of get_path:
Path reconstruction is sequential along the tree.
=> Span = O(V)

