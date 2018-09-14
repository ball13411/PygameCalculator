# # Calculator By Apisit Khomcharoen 6001012630187
# # blog me ---> https://apisit13411.blogspot.com/


# Calculator 
# Credit Regedit1 by Github "https://github.com/CodeAndMoreCode/pycalculator/blob/master/calculator.py" 
# Credit Tech With Tim  by youtube "https://www.youtube.com/watch?v=4_9twnEduFA&t=212s"

import pygame

pygame.init()
pygame.display.set_caption("13411 Calculator")                     # Set name pygame
Display = pygame.display.set_mode((400,700))                       # Set Display
sound_click = pygame.mixer.music.load("Button-click-sound.mp3")    # Set Sound
Equal = ''
font = pygame.font.SysFont("Bookman Old Style",50)                       # Set Font
clock = pygame.time.Clock()

# hex color
red = (255,0,0)    
white = (255,255,255)
blue_button = (68,32,155)
blue_button1 = (68,32,170)
list_xy = []
Display.fill(white)                                 # Set Color Display
list_str_cal = ['(',')','c','«','7','8','9','÷','4','5','6','x','1','2','3','-','.','0','=','+']  #list button
list_btm_class = []
in_list = 0

class Draw():                                       # Class Pygame Draw Button
    
    def __init__ (self,color,x,y,widht,height):     # Set Variable
        self.color = color
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
        
    def set_color (self,color):                     # Set Color
        self.color = color
        return self.Rect()
    
    def Rect (self):                                # Draw Rect
        return pygame.draw.rect(Display,self.color,(self.x,self.y,self.widht,self.height))
    
    def Circle(self):                               # Draw Circle
        return pygame.draw.circle(Display,self.color,(self.x+self.widht)/2,(self.y+self.height)/2,)
    
    def isPosition(self,pos):                       # Check Position Mouse
        if pos[0] > self.x and pos[0] < self.x + self.widht :
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

i=0
for y in range(200,700,100):              
    for x in range(0,400,100):
        list_btm_class.append(Draw(blue_button,x,y,100,100))                         # Append Class to List
        Draw(blue_button,x,y,100,100).Rect()                                         # Create Button from Class
        Display.blit(font.render(list_str_cal[i],True,(white)),(x+30,y+30))          # White Text on Display
        i = i+1
        
run = True
while run:     
    
  # Event in pygame
    for event in pygame.event.get():                                                     # Even in Display
        pos = pygame.mouse.get_pos() 
        if event.type == pygame.MOUSEBUTTONDOWN:                                         # Even about MouseDown
            Process_btm = pygame.draw.rect(Display,white,(0,0,400,200))
            
   # Check Position Mouse with Button  (Press Button)
            if list_btm_class[3].isPosition(pos) :                                   
                Equal = Equal[:-1]
            elif list_btm_class[2].isPosition(pos) :
                Equal = ''
            elif len(Equal) == 11 :
                pass
            elif list_btm_class[0].isPosition(pos) :                            
                Equal += '('
            elif list_btm_class[1].isPosition(pos) :
                Equal += ')'
            elif list_btm_class[4].isPosition(pos) :
                Equal += '7'
            elif list_btm_class[5].isPosition(pos) :
                Equal += '8'
            elif list_btm_class[6].isPosition(pos) :
                Equal += '9'
            elif list_btm_class[7].isPosition(pos) :
                Equal += '/'
            elif list_btm_class[8].isPosition(pos) :
                Equal += '4'
            elif list_btm_class[9].isPosition(pos) :
                Equal += '5'
            elif list_btm_class[10].isPosition(pos) :
                Equal += '6'
            elif list_btm_class[11].isPosition(pos) :
                Equal += '*'
            elif list_btm_class[12].isPosition(pos) :
                Equal += '1'
            elif list_btm_class[13].isPosition(pos) :
                Equal += '2'
            elif list_btm_class[14].isPosition(pos) :
                Equal += '3'
            elif list_btm_class[15].isPosition(pos) :
                Equal += '-'
            elif list_btm_class[16].isPosition(pos) :
                Equal += '.'
            elif list_btm_class[17].isPosition(pos) :
                Equal += '0'
            elif list_btm_class[19].isPosition(pos) :
                Equal += '+'
            text = font.render(str(Equal), True,red)                            # Render Text ---> Equal
            Display.blit(text, (25,50))                                         # Show Text (x,y)
            if list_btm_class[18].isPosition(pos) : 
                Process_btm = pygame.draw.rect(Display,white,(0,0,400,200))
                pygame.display.update()                                         
                if Equal == '13411':                                            # if Condition
                    Equal = "Apisit.K"
                    text = font.render(str(Equal), True,red)
                    Display.blit(text, (25,50)) 
                elif len(Equal) == 0 :
                    Equal = "0"
                    text = font.render(str(Equal), True,red)
                    Display.blit(text, (25,50)) 
                elif '/0' in Equal or '*/' in Equal or '/*' in Equal or Equal[0] == '*' or Equal[0] == '/' or Equal[-1] =='*' or Equal[-1] == '/' or Equal[0]== '.':
                    Equal = "Error"                                              # for Error Case
                    text = font.render(str(Equal), True,red)
                    Display.blit(text, (25,50)) 
                elif '/' in Equal or '*' in Equal or '+' in Equal or '-' in Equal:
                    answer = str("%0.2f" %(eval(Equal)))
                    if '.00' in answer:
                        answer = str(int(float(answer)))
                        text = font.render(str(answer), True,red)
                        Display.blit(text, (25,50))
                        Equal = answer
                    else :
                        text = font.render(str(answer), True,red)
                        Display.blit(text, (25,50))
                        Equal = answer
                else:
                    text = font.render(str(Equal), True,red)
                    Display.blit(text, (25,50))  
            pygame.mixer.music.play()                                        # Sound Button
            pygame.mixer.music.play()
        
   # if mouse on buttom change color            
        elif event.type == pygame.MOUSEMOTION:                               
            for i in list_btm_class:
                if i.isPosition(pos):
                    i.set_color(blue_button1)
                else :
                    i.set_color(blue_button)
            i=0
            for y in range(200,700,100):              
                for x in range(0,400,100):
                    Display.blit(font.render(list_str_cal[i],True,(white)),(x+30,y+30))  # White Text on Display
                    i = i+1
   # Quit Program           
        elif event.type == pygame.QUIT:                                    
            run= False
    pygame.display.update()   
    
pygame.quit()
quit()


"""
Test Calculator

45 + 8 - 5 * 3 = 38
70 * 5 / 2 = 175
-6+3 = -3
41 / 0 = Error
7 * (5+6) - 2 = 75
9 / 0 + (5-2) = Error
13411 = Apisit.K
50*  = Error
7/3 = 2.33 
50*/2 = Error

"""

