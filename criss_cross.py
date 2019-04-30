# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:35:50 2019

@author: tafsir
"""

import random




def display_board(board):
    
    print('\n'*100)
    print('    |   |')
    print('  '+board[7]+' | '+board[8]+' | '+board[9])
    print('    |   |')
    print('--------------')
    print('    |   |')
    print('  '+board[4]+' | '+board[5]+' | '+board[6])
    print('    |   |')
    print('--------------')
    print('    |   |')
    print('  '+board[1]+' | ' +board[2]+' | '+board[3])
    print('    |   |')



def player_input():
    
    marker = ''
    
    #keep asking player 1 to choose X or O
    
    while marker != 'X' and marker != 'O':
        
        marker = input('Player 1 choose X or O: ').upper()
        
    player1 = marker
        
    
    #assign player 2 to the opposite marker
    
    if player1 == 'X':
        player2 = 'O'
        
    else:
        player2 = 'X'
        
        
    return (player1,player2)
    
    






def place_marker(board,marker,position):
    
    board[position] = marker
    
    



def win_check(board,mark):
    
    
    return(
    #row  
    
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    
    #column
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark) or
    
    #diagonal
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) 
    
    
    
    
    
    
    )
    




def choose_first():
    flip = random.randint(0,1)
    
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
    


def space_check(board,position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
        
        #Board is full if this return True
    return True   
    


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        
        position = int(input('Choose a position (1-9): '))
        
    return position


def replay():
    
    choice = input('Play again? Enter Yes or No')
    
    return choice == 'Yes'





print('Welcome to TIC TAC TOE')
   
    
#while loop to keep running the game

while True:
    
    
        
        
        ## Set everything up (Board, Whoose First, Choose markers X,O)
        
    the_board = [' ']*10
        
    player1_marker,player2_marker = player_input()
        
    turn = choose_first()
    print(turn +' will go first!')
        
        
    play_game = input('Ready to Play? y or n? ')
    
        
    if play_game == 'y':
        
        game_on = True
    else:
        
        game_on = False
        
        ## Game play
        
        
    while game_on:
        
        ### Player 1 turn
        if turn == 'Player 1':
            
                
                #show the board
            display_board(the_board)
                
                # Choose a position
                
            position = player_choice(the_board)
                
                # Place the marker on the position
                
            place_marker(the_board,player1_marker,position)
                
                # Check if they won
                
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game_on = False
                    
                
                # or Check if there is a tie
                
            else:
                        
                if full_board_check(the_board):
                            
                    display_board(the_board)
                    print('TIE GAME !!!')
                            
                    game_on = False
                    
                                  
                # No tie and No win ? Then next players turn
                else:
                        turn = 'Player 2'
        
        
        ### Player 2 turn
        
                
                
        if turn == 'Player 2':
                    
                
                #show the board
            display_board(the_board)
                
                # Choose a position
                
            position = player_choice(the_board)
                
                # Place the marker on the position
                
            place_marker(the_board,player2_marker,position)
                
                # Check if they won
                
            if win_check(the_board,player2_marker):
                    
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!')
                game_on = False
                    
                
                # or Check if there is a tie
                
            else:
                    
                if full_board_check(the_board):
                        
                    display_board(the_board)
                    print('TIE GAME !!!')
                        
                    game_on = False
                    
                                  
                # No tie and No win ? Then next players turn
                else:
                    turn = 'Player 1'
                
        
        
        
        
        
        
#Break out the while loop for replay()
    if not replay():
        break
       

#



    
    






    
    
    

    



  
    