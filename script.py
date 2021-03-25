#!/usr/bin/python3
import sys

def prints(mat):

    for i in range(3):
        for j in range(3):
                if (mat[i][j] == 1):
                    print('', end = '|')
                elif (mat[i][j] == 2):
                    print('', end = '_')
                else:
                    print('', end = ' ')
 
        print()
 

sys.argv.pop(0)
for x in range(len(sys.argv)):
    num = int(sys.argv[x])

    if (num == 0):
        mat = [ [ 0, 2, 0 ],
                [ 1, 0, 1 ],
                [ 1, 2, 1 ] ]             
        prints(mat)    
    elif (num == 1):
        mat = [ [ 0, 0, 0],
                [ 0, 0, 1],
                [ 0, 0, 1] ]            
        prints(mat)    
    elif (num == 2):
        mat = [ [ 0, 2, 0],
                [ 0, 2, 1],
                [ 1, 2, 0] ]             
        prints(mat)    
    elif (num == 3):
        mat = [ [ 0, 2, 0],
                [ 0, 2, 1],
                [ 0, 2, 1] ]          
        prints(mat)    
    elif (num == 4):
        mat = [ [ 0, 0, 0],
                [ 1, 2, 1],
                [ 0, 0, 1] ]            
        prints(mat)    
    elif (num == 5):
        mat = [ [ 0, 2, 0],
                [ 1, 2, 0],
                [ 0, 2, 1] ]     
        prints(mat)    
    elif (num == 6):
        mat = [ [ 0, 2, 0],
                [ 1, 2, 0],
                [ 1, 2, 1] ]       
        prints(mat)    
    elif (num == 7):
        mat = [ [ 0, 2, 0],
                [ 0, 0, 1],
                [ 0, 0, 1] ]      
        prints(mat)    
    elif (num == 8):
        mat = [ [ 0, 2, 0],
                [ 1, 2, 1],
                [ 1, 2, 1] ]
        prints(mat)
    elif (num == 9):
        mat = [ [ 0, 2, 0],
                [ 1, 2, 1],
                [ 0, 2, 1] ]
        prints(mat)
    x += 1