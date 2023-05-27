import pygame, sys
from pygame.locals import *

class StateMachine:
    
    def __init__(self):
        self.end = False
        self.next = None
        self.quit = False
        self.previous = None
  
class Texts:
    
    white = (255,255,255)
    black = (0,0,0) 
    
    def __init__(self):
        pygame.init()          
        self.basic_font = pygame.font.SysFont('arcade',40)     
        self.small_font = pygame.font.Font('freesansbold.ttf',20)  

    def menu_txt(self, displaysurf, game_name):
        logoSurf = self.basic_font.render(game_name,True,self.white)
        enterSurf = self.basic_font.render('Press ENTER',True,self.white)
        logoRect = logoSurf.get_rect()
        enterRect = enterSurf.get_rect()
        logoRect.center = (400,250)
        enterRect.center = (400,300)      
        displaysurf.blit(logoSurf,logoRect)
        displaysurf.blit(enterSurf,enterRect)     
        
class MainMenu(StateMachine): 
    
    blue = (182, 208, 226)   

    def __init__(self):
        StateMachine.__init__(self)
    
    def startup(self):
        pass

    def cleanup(self):
        pass

    def handle_events(self, event):
        pass

    def update(self, displaysurf):
        t = Texts()

        displaysurf.fill(self.blue)
        t.menu_txt(displaysurf,'Snow Muncher') 

class MainGame(StateMachine):
    def __init__(self):
        StateMachine.__init__(self)
        Texts.__init__(self)

    def startup(self):      
        pass

    def cleanup(self):
        pass
    
    def handle_events(self, event):
        pass
    
    def actors_update(self):
        pass
    
    def actors_draw(self, displaysurf):
        pass
        
    def update(self, displaysurf):  
        pass 
    
class StageI(MainGame):
    
    def __init__(self):
        super().__init__()
    
    def startup(self):
        pass

    def update(self, displaysurf):
        pass 

class SnowMuncherGame:
    
    state_dictionary = None
    state_name = None
    state = None

    def __init__(self, **settings):      
        self.__dict__.update(settings)
        self.end = False  
        pygame.display.set_caption("Snow Muncher")   
        self.displaysurf = pygame.display.set_mode(self.size)
        self.fpsclock = pygame.time.Clock()            

    def setup_states(self, state_dictionary, start_state):
        self.state_dictionary = state_dictionary
        self.state_name = start_state
        self.state = self.state_dictionary[self.state_name]
        self.state.startup()

    def flip_state(self):
        self.state.end = False
        previous,self.state_name = self.state_name,self.state.next
        self.state.cleanup()
        self.state = self.state_dictionary[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self):
        if self.state.quit:
            self.end = True
        elif self.state.end:
            self.flip_state()

        self.state.update(self.displaysurf)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.end = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.end = True
            self.state.handle_events(event)

    def loop(self):
        while not self.end:
            self.event_loop()
            self.update()
            pygame.display.flip()
            pygame.display.update()
            self.fpsclock.tick(self.fps)

def main():
    
    settings = {
        'size' : (800,650),
        'fps' : 10           
    }

    game_images = {
        
    }

    state_dictionary = {
        'menu' : MainMenu(),
        'stage1': StageI(),
    }

    main_game = SnowMuncherGame(**settings)
    main_game.setup_states(state_dictionary,'menu')
    main_game.loop()  

## MAIN ##
if __name__ == '__main__':
    main()
