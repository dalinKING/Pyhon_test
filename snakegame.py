import tkinter
import random   

def __init__(self):  

        self.step = 10  
        self.score_ = -1  
        # the snake position  
        self.snakeX = [255,245]  
        self.snakeY = [255,255]  
          
        #to initialize the moving direction  
        self.snakeDirection = "right"  
        self.snakeMove = [1, 0]  
        # to draw the game frame   
        window = Tk()  
        window.geometry("800x550+180+160")  
        window.maxsize(800,550)  
        window.minsize(800,550)  
        window.title("贪食蛇")  
          
        self.canvas = Canvas(window, bg = "#191919", width = 800, height = 550)  
        self.canvas.create_line(0,500,800,500, fill = 'white')  
        self.scoretext = self.canvas.create_text(100, 520, text = 'Score: 0', font=("Purisa", 20), fill = 'white')      
        self.canvas.grid(row = 0)     
        self.draw_score()  
        self.draw_food()  
        self.draw_snake()    
        self.play()  
        window.mainloop()  

"=== View Part ==="           
def draw_score(self):  
    self.score()  
    self.tkinter.canvas.itemconfig(self.scoretext, text="Score: " + str(self.score_))  
     
def draw_food(self):  
    self.canvas.delete('food')  
    self.foodx,self.foody=self.random_food()  
    self.canvas.create_rectangle(self.foodx - self.step / 2,self.foody - self.step / 2,self.foodx + self.step / 2,self.foody + self.step / 2, fill = 'white', tags='food')  
      
def draw_snake(self):  
    self.canvas.delete("snake")  
    x,y=self.snake()  
    for i in range(len(x)):  
       self.canvas.create_rectangle(x[i] - self.step / 2,y[i] - self.step / 2,x[i] + self.step / 2,y[i] + self.step / 2, fill='orange',tags='snake')  

"=== Model Part ==="  
def random_food(self):   
    # return food position but not in the snake position  
        return(random.randrange(5,795,self.step),random.randrange(5,495,self.step))  
          
def snake(self):  
    #return x array and y array  
    #前一段的位置给下一段  
        for i in range(len(self.snakeX)-1,0,-1):  
            self.snakeX[i] = self.snakeX[i-1]  
            self.snakeY[i] = self.snakeY[i-1]  
              
        self.snakeX[0] += self.snakeMove[0] * self.step  
        self.snakeY[0] += self.snakeMove[1] * self.step  
        return(self.snakeX,self.snakeY)  
      
def score(self):  
        self.score_ += 1  
"=== Control Part ==="       
def iseated(self):  
    # return true or false  
        if self.snakeX[0] == self.foodx and self.snakeY[0] == self.foody:  
            return True  
        else:  
            return False  
      
def isdead(self):  
    # 判断头是否撞墙，或是否咬到自身  
        if self.snakeX[0] < 5 or self.snakeX[0] > 795 or self.snakeY[0] < 5 or self.snakeY[0] > 495:  
            return True  
          
        for i in range(1,len(self.snakeX)):  
            if self.snakeX[0] == self.snakeX[i] and self.snakeY[0] == self.snakeY[i]:  
                return True  
        else:  
            return False  
      
def move(self,event):  
    # 通过键盘控制蛇的运动  
    # left:[-1,0],right:[1,0],up:[0,1],down:[0,-1]    
        if event.keycode == 39 and self.snakeDirection != 'left':  
            self.snakeMove = [1,0]  
            self.snakeDirection = "right"  
              
        elif event.keycode == 38 and self.snakeDirection != 'down':  
            self.snakeMove = [0,-1]  
            self.snakeDirection = "up"  
              
        elif event.keycode == 37 and self.snakeDirection != 'right':  
            self.snakeMove = [-1,0]  
            self.snakeDirection = "left"  
              
        elif event.keycode == 40 and self.snakeDirection != 'up':  
            self.snakeMove = [0,1]  
            self.snakeDirection = "down"  
        #如何加速？    
        #else:  
        #    print event.keycode  
      
def play(self):  
    # main   
        self.canvas.bind('<Key>',self.move)  
        self.canvas.focus_set()  
        self.updatetime = 115  
          
        while True:  
            self.update = self.updatetime - self.score_  
            if self.isdead():  
                self.gameover()  
                break  
                  
            elif self.iseated():  
                self.snakeX[0] += self.snakeMove[0] * self.step  
                self.snakeY[0] += self.snakeMove[1] * self.step     
                self.snakeX.insert(1,self.foodx)  
                self.snakeY.insert(1,self.foody)  
                  
                self.draw_score()  
                self.draw_food()  
                self.draw_snake()  
                self.canvas.after(100)  
                self.canvas.update()  
              
            else:  
                self.draw_snake()   
                self.canvas.after(self.update)  
                self.canvas.update()  
                  
def gameover(self):  
        # self.canvas.delete("food","snake")  
        self.canvas.unbind('<Key>')  
        self.canvas.bind("<Key>",self.restart)  
        self.canvas.create_text(270,180,text="                   Game Over!\n  Press any key to continue",font=("Purisa", 30),tags='text', fill = "white")  
          
def restart(self,event):  
        self.canvas.delete('text')  
        self.canvas.unbind('<Key>')  
          
        self.score_ = -1  
        # the snake position  
        self.snakeX = [255,245]  
        self.snakeY = [255,255]  
          
        #to initialize the moving direction  
        self.snakeDirection = "right"  
        self.snakeMove = [1, 0]  
  
        self.draw_score()   
        self.draw_food()  
        self.draw_snake()  
          
        self.play()  
