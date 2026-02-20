import csv
import random

# 6x6 の完成盤
solution = [
    [1, 2, 3, 4, 5, 6],
    [4, 5, 6, 1, 2, 3],
    [2, 3, 4, 5, 6, 1],
    [5, 6, 1, 2, 3, 4],
    [3, 4, 5, 6, 1, 2],
    [6, 1, 2, 3, 4, 5],
]

def make_puzzle(solution, remove_count=12):
    """完成盤からランダムにマスを消して問題を作る"""
    puzzle = [row[:] for row in solution]
    cells = [(r, c) for r in range(6) for c in range(6)]
    random.shuffle(cells)

    for i in range(remove_count):
        r, c = cells[i]
        puzzle[r][c] = 0  # 空欄は 0

    return puzzle

def write_csv(board, filename="puzzle6x6.csv"):
    """6x6 の盤を CSV に書き出す"""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(board)

def main():
    puzzle = make_puzzle(solution, remove_count=12)
    write_csv(puzzle)
    print("CSV に書き出しました:", "puzzle6x6.csv")

if __name__ == "__main__":
    main()
