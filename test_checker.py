from easyAI import Human_Player, AI_Player, Negamax
from checker import Checker, black_squares
import pytest
import numpy as np


@pytest.fixture
def checker_game():
    ai = Negamax(13) # The AI will think 13 moves in advance
    game = Checker( [ Human_Player(), AI_Player(ai) ] )
    return game

@pytest.fixture
def black_pieces():
    return [
            (0,1), (0,3), (0,5), (0,7),
            (1,0), (1,2), (1,4), (1,6)
        ]

@pytest.fixture
def white_pieces():
    return [
        (6,1), (6,3), (6,5), (6,7),
        (7,0), (7,2), (7,4), (7,6)
        ]

@pytest.fixture
def black_squares():
    even = [0,2,4,6]
    odd = [1,3,5,7]

    even_row = [(i,j) for i in even for j in odd]
    odd_row = [(i,j) for i in odd for j in even]

    black_squares = even_row + odd_row
    return black_squares


@pytest.mark.usefixtures("checker_game")
def test_has_2_player(checker_game):
    assert len(checker_game.players) == 2

# initialize board, pieces, and player's position
@pytest.mark.usefixtures("checker_game")
def test_board_size(checker_game):
    assert checker_game.board.size == 64
    assert checker_game.board.shape == (8,8)

@pytest.mark.usefixtures("checker_game", "black_pieces", "white_pieces")
def test_initial_pieces_position(checker_game, black_pieces, white_pieces):

    for i in black_pieces:
        assert i in checker_game.black_pieces

    for i in white_pieces:
        assert i in checker_game.white_pieces

@pytest.mark.usefixtures("checker_game", "black_pieces", "white_pieces")
def test_initial_player_positions(checker_game, black_pieces, white_pieces):

    # white players
    for i in checker_game.players[0].pos:
        assert i in white_pieces

    # black players
    for i in checker_game.players[1].pos:
        assert i in black_pieces

@pytest.mark.usefixtures("checker_game", "black_pieces", "white_pieces")
def test_initial_pieces_position_on_board(checker_game, black_pieces, white_pieces):
    for (i,j) in white_pieces:
        assert checker_game.board[i,j] == "W"

    for (i,j) in black_pieces:
        assert checker_game.board[i,j] == "B"

@pytest.mark.usefixtures("checker_game")
def test_territory(checker_game):
    white_territory = [(7,0), (7,2), (7,4), (7,6)]
    for i in white_territory:
        assert i in checker_game.white_territory

    black_territory = [(0,1), (0,3), (0,5), (0,7)]
    for i in black_territory:
        assert i in checker_game.black_territory

# test possible move
@pytest.mark.usefixtures("checker_game")
def test_only_black_square_is_valid(checker_game):
    for (i,j) in [(0,1),(0,3),(1,0),(1,2)]:
        assert (i,j) in black_squares

    for (i,j) in black_squares:
        assert (i + j) % 2 == 1

@pytest.mark.usefixtures("checker_game", "black_squares")
def test_possible_moves_of_black_player(checker_game, black_squares):
    checker_game.current_player = 2 # black turn to move
    checker_game.players[checker_game.current_player-1].pos = [[0,1], (1,0), (1,2)]
    table_pos_after_move = [[(0,1),(2,1),(1,2)],
                            [(0,1),(1,0),(2,1)],
                            [(0,1),(1,0),(2,3)],
                            [(2,3),(1,0),(2,1)]
                            ]
    possible_moves = checker_game.possible_moves()
    assert len(possible_moves) == len(table_pos_after_move)
    for pos in possible_moves: # all possible combination of pieces after black moves.
        index_in_pos = np.where(pos == "B")
        assert len(index_in_pos[0]) == len(checker_game.players[checker_game.current_player-1].pos)
        for i,j in zip(index_in_pos[0], index_in_pos[1]):
            assert (i,j) in black_squares

@pytest.mark.usefixtures("checker_game", "black_squares")
def test_possible_moves_of_white_player(checker_game, black_squares):
    checker_game.current_player = 1 # white turn to move
    checker_game.players[checker_game.current_player-1].pos = [[7,0], (6,1), (7,2)]
    table_pos_after_move = [[(7,0),(5,0),(7,2)],
                            [(7,0),(5,2),(7,2)],
                            [(7,0),(6,1),(5,0)],
                            [(5,2),(6,1),(7,2)],
                            [(7,0),(6,1),(6,3)]]
    possible_moves = checker_game.possible_moves()
    print(possible_moves)
    assert len(possible_moves) == len(table_pos_after_move)
    for pos in possible_moves: # all possible combination of pieces after white moves.
        index_in_pos = np.where(pos == "W")
        assert len(index_in_pos[0]) == len(checker_game.players[checker_game.current_player-1].pos)
        for i,j in zip(index_in_pos[0], index_in_pos[1]):
            assert (i,j) in black_squares

# test make_move
@pytest.mark.usefixtures("checker_game")
def test_is_player_position_updated(checker_game):
    checker_game.current_player = 1 # white turn to move
    pos = checker_game.possible_moves()[0]
    index_in_pos = np.where(pos == "W")
    index_in_pos = [(i,j) for i,j in zip(index_in_pos[0], index_in_pos[1])]
    checker_game.make_move(pos)
    assert checker_game.players[checker_game.current_player-1].pos == index_in_pos

# test lose condition
@pytest.mark.usefixtures("checker_game")
def test_is_black_lose(checker_game):
    white_territory = [(7,0), (7,2), (7,4), (7,6)]
    black_territory = [(0,1), (0,3), (0,5), (0,7)]

    white_player = 0
    black_player = 1

    # black loss when its turn started
    checker_game.players[white_player].pos = [black_territory[0]]
    for i,j in checker_game.players[white_player].pos:
        checker_game.board[i,j] = "W"

    checker_game.current_player = 2
    answer = []
    for i,j in black_territory:
        if "W" in checker_game.board[i,j]:
            answer.append(True)
        else:
            answer.append(False)

    assert checker_game.lose() == any(answer)

@pytest.mark.usefixtures("checker_game")
def test_lose_when_no_move_left(checker_game):
    checker_game.board = np.zeros((8,8), dtype=object)
    ind = np.where(checker_game.board == 0)
    for i,j in zip(ind[0],ind[1]):
        checker_game.board[i,j] = 'W'
    assert len(checker_game.possible_moves()) == 0

def test_is_white_lose(checker_game):
    white_territory = [(7,0), (7,2), (7,4), (7,6)]
    black_territory = [(0,1), (0,3), (0,5), (0,7)]

    white_player = 1
    black_player = 2

    # white loss when its turn started
    checker_game.players[black_player-1].pos = [white_territory[0]]
    for i in checker_game.players[black_player-1].pos:
        checker_game.board[i] = "B"

    checker_game.current_player = 1
    answer = []
    for i,j in white_territory:
        if "B" in checker_game.board[i,j]:
            answer.append(True)
        else:
            answer.append(False)

    assert checker_game.lose() == any(answer)


# test scoring
@pytest.mark.usefixtures("checker_game")
def test_scoring(checker_game):
    white_territory = [(7,0), (7,2), (7,4), (7,6)]
    black_territory = [(0,1), (0,3), (0,5), (0,7)]

    white_player = 1
    black_player = 2

    # score when lose a game

    # white loss when its turn started
    checker_game.players[black_player-1].pos = [white_territory[0]]
    for i in checker_game.players[black_player-1].pos:
        checker_game.board[i] = "B"

    checker_game.current_player = 1

    assert checker_game.scoring() == -100

    # score when lose a game
    checker_game.board = np.zeros((8,8))
    assert checker_game.scoring() == 0


@pytest.mark.usefixtures("checker_game")
def test_number_of_piece_the_same_after_move(checker_game):
    pass

    # make a move
    # checker_game.make_move()
    # # count pass zero = 48.

if __name__ == "__main__":
    pass