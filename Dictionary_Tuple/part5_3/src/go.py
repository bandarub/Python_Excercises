def who_won(game_board: list):
    player_1_count = 0
    player_2_count = 0
    
    for row in game_board:
        for cell in row:
            if cell == 1:
                player_1_count += 1
            elif cell == 2:
                player_2_count += 1
    
    if player_1_count > player_2_count:
        return 1
    elif player_2_count > player_1_count:
        return 2
    else:
        return 0

if __name__ == "__main__":
    who_won([
    [1, 2, 1],
    [0, 1, 2],
    [1, 1, 0]])