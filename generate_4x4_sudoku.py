import random
from copy import deepcopy

BASE = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1],
]

def permute_symbols(grid):
    mapping = {i: j for i, j in zip([1, 2, 3, 4], random.sample([1, 2, 3, 4], 4))}
    return [[mapping[v] for v in row] for row in grid]

def shuffle_rows_within_bands(grid):
    g = deepcopy(grid)
    # 4x4は2行ずつが“バンド”
    for band_start in (0, 2):
        band = g[band_start:band_start+2]
        random.shuffle(band)
        g[band_start:band_start+2] = band
    return g

def shuffle_cols_within_stacks(grid):
    g = deepcopy(grid)
    # 4x4は2列ずつが“スタック”
    cols = list(zip(*g))
    for stack_start in (0, 2):
        stack = cols[stack_start:stack_start+2]
        stack = list(stack)
        random.shuffle(stack)
        cols[stack_start:stack_start+2] = stack
    return [list(row) for row in zip(*cols)]

def maybe_swap_bands(grid):
    g = deepcopy(grid)
    if random.random() < 0.5:
        g[0:2], g[2:4] = g[2:4], g[0:2]
    return g

def maybe_swap_stacks(grid):
    g = deepcopy(grid)
    if random.random() < 0.5:
        cols = list(zip(*g))
        cols[0:2], cols[2:4] = cols[2:4], cols[0:2]
        g = [list(row) for row in zip(*cols)]
    return g

def make_solution():
    g = deepcopy(BASE)
    g = shuffle_rows_within_bands(g)
    g = shuffle_cols_within_stacks(g)
    g = maybe_swap_bands(g)
    g = maybe_swap_stacks(g)
    g = permute_symbols(g)
    return g

def punch_holes(solution, holes=4):
    # holes: 空欄の数（めっちゃ簡単なら 2〜6 くらい）
    puzzle = deepcopy(solution)
    cells = [(r, c) for r in range(4) for c in range(4)]
    for r, c in random.sample(cells, holes):
        puzzle[r][c] = 0
    return puzzle

def format_grid(grid):
    lines = []
    for r in range(4):
        row = []
        for c in range(4):
            v = grid[r][c]
            row.append("_" if v == 0 else str(v))
        lines.append(" ".join(row[0:2]) + " | " + " ".join(row[2:4]))
        if r == 1:
            lines.append("---------")
    return "\n".join(lines)

def main(n=10, holes=4, out_file="puzzles_4x4.txt"):
    blocks = []
    for i in range(1, n + 1):
        sol = make_solution()
        puz = punch_holes(sol, holes=holes)
        blocks.append(f"## Puzzle {i}\n{format_grid(puz)}\n\nAnswer:\n{format_grid(sol)}\n")
    text = "\n\n".join(blocks)

    print(text)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    # ここを変えるだけで量と難易度を調整できます
    main(n=10, holes=4)
