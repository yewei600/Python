'''
algorithm to place the bombs
placing bombs: card shuffling algorithm?
how to count number of boms neighboring a cell?
when click on a blank cell, algorithm to expand other blank cells

'''
import random

class board:
    dim=7
    numBombs=3
    bombList=[None]*numBombs
    def __init__(self):
        print "let's play Minesweeper!"
        for i in range (0,self.dim):
            for j in range(0,self.dim):
                print "?",
            print
        #determine the location of bombs
        for i in range (0,self.numBombs):
            self.bombList[i]=random.randrange(0,self.dim*self.dim+1)   
            print self.bombList[i]
        
    
    def is_bomb(self,num):
        
   # def makePlay(self,row,column):
     #   if not isBomb()
   
   
   
        
        
    
        
        
            
         
        