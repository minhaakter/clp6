def solve_case(case_num, R, C, grid, Target):
    found_path = []

    def dfs(r, c, current_sum, visited, path):
        nonlocal found_path
        
        if (r, c) in visited or r < 0 or r >= R or c < 0 or c >= C:
            return False
            
        new_sum = current_sum + grid[r][c]
        if new_sum > Target:
            return False
            
        visited.add((r, c))
        path.append((r, c))
        
        if new_sum == Target:
            found_path = path.copy()
            return True
            
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        for dr, dc in directions:
            if dfs(r + dr, c + dc, new_sum, visited, path):
                return True
                
        path.pop()
        visited.remove((r, c))
        return False

    if case_num == 1:
        dfs(0, 1, 0, set(), [])
    else:
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0, set(), []):
                    break

    print(f"Case#{case_num}Output:")
    if found_path:
        print("Path found")
        print(f"DFS Traversal Order: {found_path}")
    else:
        print("Path not found")
    print()


def read_case(case_num):
    print(f"Case#{case_num}Input:")
    R, C = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(map(int, input().split())))
    target_line = input().strip()
    Target = int(target_line.split(":")[1]) if ":" in target_line else int(target_line)
    solve_case(case_num, R, C, grid, Target)


def main():
    read_case(1)
    read_case(2)


if __name__ == "__main__":
    main()