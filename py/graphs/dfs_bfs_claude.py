from collections import deque

# ================================
# 2D ARRAY (GRID) IMPLEMENTATIONS
# ================================


def dfs_2d_recursive(grid, start_row, start_col, visited=None):
    """
    DFS on 2D grid - Recursive version

    Args:
        grid: 2D list representing the grid
        start_row, start_col: starting position
        visited: set to track visited cells
    """
    if visited is None:
        visited = set()

    # Get grid dimensions
    rows, cols = len(grid), len(grid[0])

    # Base cases: out of bounds or already visited
    if (
        start_row < 0
        or start_row >= rows
        or start_col < 0
        or start_col >= cols
        or (start_row, start_col) in visited
    ):
        return

    # Mark current cell as visited
    visited.add((start_row, start_col))
    print(f"Visiting cell ({start_row}, {start_col}): {grid[start_row][start_col]}")

    # Define 4 directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Recursively visit all neighbors
    for dr, dc in directions:
        new_row, new_col = start_row + dr, start_col + dc
        dfs_2d_recursive(grid, new_row, new_col, visited)


def dfs_2d_iterative(grid, start_row, start_col):
    """
    DFS on 2D grid - Iterative version using stack

    Args:
        grid: 2D list representing the grid
        start_row, start_col: starting position
    """
    if not grid or not grid[0]:
        return

    rows, cols = len(grid), len(grid[0])
    visited = set()
    stack = [(start_row, start_col)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while stack:
        row, col = stack.pop()  # Pop from end (LIFO - stack behavior)

        # Skip if out of bounds or already visited
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
            continue

        # Mark as visited and process
        visited.add((row, col))
        print(f"Visiting cell ({row}, {col}): {grid[row][col]}")

        # Add neighbors to stack
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (new_row, new_col) not in visited:
                stack.append((new_row, new_col))


def bfs_2d_iterative(grid, start_row, start_col):
    """
    BFS on 2D grid - Iterative version using queue

    Args:
        grid: 2D list representing the grid
        start_row, start_col: starting position
    """
    if not grid or not grid[0]:
        return

    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_row, start_col)])
    visited.add((start_row, start_col))
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        row, col = queue.popleft()  # Pop from front (FIFO - queue behavior)
        print(f"Visiting cell ({row}, {col}): {grid[row][col]}")

        # Add unvisited neighbors to queue
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds and if not visited
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and (new_row, new_col) not in visited
            ):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

def bfs_2d_recursive(grid, start_row, start_col):
    """
    BFS on 2D grid - Recursive version (less common but possible)
    Uses a queue and recursion to process level by level
    """
    if not grid or not grid[0]:
        return

    rows, cols = len(grid), len(grid[0])
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs_helper(queue):
        if not queue:
            return

        # Process current level
        next_queue = deque()

        while queue:
            row, col = queue.popleft()

            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or (row, col) in visited
            ):
                continue

            visited.add((row, col))
            print(f"Visiting cell ({row}, {col}): {grid[row][col]}")

            # Add neighbors to next level
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (new_row, new_col) not in visited:
                    next_queue.append((new_row, new_col))

        # Recursively process next level
        bfs_helper(next_queue)

    # Start BFS
    initial_queue = deque([(start_row, start_col)])
    bfs_helper(initial_queue)


# ====================================
# ADJACENCY LIST (GRAPH) IMPLEMENTATIONS
# ====================================


def dfs_graph_recursive(graph, start, visited=None):
    """
    DFS on adjacency list graph - Recursive version

    Args:
        graph: dictionary where keys are nodes and values are lists of neighbors
        start: starting node
        visited: set to track visited nodes
    """
    if visited is None:
        visited = set()

    # Mark current node as visited
    visited.add(start)
    print(f"Visiting node: {start}")

    # Recursively visit all unvisited neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_graph_recursive(graph, neighbor, visited)


def dfs_graph_iterative(graph, start):
    """
    DFS on adjacency list graph - Iterative version using stack

    Args:
        graph: dictionary where keys are nodes and values are lists of neighbors
        start: starting node
    """
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # Pop from end (LIFO - stack behavior)

        if node not in visited:
            visited.add(node)
            print(f"Visiting node: {node}")

            # Add neighbors to stack (in reverse order for consistent traversal)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)


def bfs_graph_iterative(graph, start):
    """
    BFS on adjacency list graph - Iterative version using queue

    Args:
        graph: dictionary where keys are nodes and values are lists of neighbors
        start: starting node
    """
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()  # Pop from front (FIFO - queue behavior)
        print(f"Visiting node: {node}")

        # Add unvisited neighbors to queue
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def bfs_graph_recursive(graph, start):
    """
    BFS on adjacency list graph - Recursive version
    Uses a queue and recursion to process level by level
    """
    visited = set()

    def bfs_helper(queue):
        if not queue:
            return

        # Process current level
        next_queue = deque()

        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)
            print(f"Visiting node: {node}")

            # Add unvisited neighbors to next level
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    next_queue.append(neighbor)

        # Recursively process next level
        bfs_helper(next_queue)

    # Start BFS
    initial_queue = deque([start])
    bfs_helper(initial_queue)


# ====================================
# EXAMPLE USAGE AND TEST CASES
# ====================================

if __name__ == "__main__":
    # Test 2D Grid
    print("=" * 50)
    print("TESTING 2D GRID ALGORITHMS")
    print("=" * 50)

    # Sample 3x3 grid
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("\nGrid:")
    for row in grid:
        print(row)

    print("\nDFS 2D Recursive from (0,0):")
    dfs_2d_recursive(grid, 0, 0)

    print("\nDFS 2D Iterative from (0,0):")
    dfs_2d_iterative(grid, 0, 0)

    print("\nBFS 2D Iterative from (0,0):")
    bfs_2d_iterative(grid, 0, 0)

    print("\nBFS 2D Recursive from (0,0):")
    bfs_2d_recursive(grid, 0, 0)

    # Test Graph (Adjacency List)
    print("\n" + "=" * 50)
    print("TESTING GRAPH ALGORITHMS")
    print("=" * 50)

    # Sample graph: A connects to B,C; B connects to D; C connects to E; etc.
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B"],
        "E": ["C", "F"],
        "F": ["E"],
    }

    print("\nGraph structure:")
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")

    print("\nDFS Graph Recursive from 'A':")
    dfs_graph_recursive(graph, "A")

    print("\nDFS Graph Iterative from 'A':")
    dfs_graph_iterative(graph, "A")

    print("\nBFS Graph Iterative from 'A':")
    bfs_graph_iterative(graph, "A")

    print("\nBFS Graph Recursive from 'A':")
    bfs_graph_recursive(graph, "A")
