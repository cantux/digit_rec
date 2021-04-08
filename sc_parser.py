#!/usr/bin/env python

import normalize

game_frame = (20, 280, 1250, 1250)
digit_square = (110, 110)
small_inc_x = 130
small_inc_y = 130
extra_x = 25
extra_y = 33

def fnc():
    img = normalize.open_img("sudoku_app_sc.png")
    
    game_frame = normalize.crop(img, 30, 300, 1250, 1250)
    normalize.save_img("game_frame.jpeg", game_frame)

    curr_y, curr_x = -33, -20
    
    for row in range(9):
        if row % 3 == 0:
            curr_y += extra_y

        for col in range(9):
            if col % 3 == 0:
                curr_x += extra_x
            curr_dig_img = normalize.crop(game_frame, curr_x + 10, curr_y + 10, digit_square[0] - 10, digit_square[1] - 10)
            normalize.save_img("out/" + str(row) + "_" + str(col) + ".jpeg", curr_dig_img)
            curr_x += small_inc_x
        curr_x = -20
        curr_y += small_inc_y
        
    return None

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

