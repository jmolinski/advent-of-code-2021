with open("input.txt") as f:
    nums = [int(a) for a in f.readline().split(",")]
    boards = [
        [
            [int(a.strip()) for a in line.split(" ") if a.strip()]
            for line in chunk.split("\n")
        ]
        for chunk in f.read().strip().split("\n\n")
    ]


def mark_point_on_board(board, value):
    for line in board:
        for i in range(len(line)):
            if line[i] == value:
                line[i] = -1


def check_if_won(board) -> bool:
    if any(all(a == -1 for a in row) for row in board):
        return True

    for i in range(len(board)):
        if all(a == -1 for a in [board[j][i] for j in range(len(board))]):
            return True

    return False


def get_board_score(board, last_num):
    s = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != -1:
                s += board[i][j]

    return s * last_num


def get_scores() -> tuple[int, int]:
    nth_winning_board_score = []
    for num_to_mark in nums:
        for i, board in enumerate(boards):
            if board is not None:
                mark_point_on_board(board, num_to_mark)
                if check_if_won(board):
                    nth_winning_board_score.append(get_board_score(board, num_to_mark))
                    boards[i] = None

    return nth_winning_board_score[0], nth_winning_board_score[-1]


print("Part 1: {}\nPart 2: {}".format(*get_scores()))
