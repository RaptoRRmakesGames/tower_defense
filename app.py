import pygame 
from pygame.time import get_ticks as gt
pygame.init()

from scripts.task_manager import TaskManager

class Game:
    
    def __init__(self) -> None:
        
        # Time stuff
        
        self.clock = pygame.time.Clock()
        self.time = 60
        self.fps_cap = 60
        self.last_time = gt()
        
        # Screen stuff
        
        screen_info = pygame.display.Info()
        self.screen = pygame.display.set_mode((screen_info.current_w//2.5, screen_info.current_h//2.5), pygame.FULLSCREEN | pygame.SCALED)
        
        # key bindings
        
        self.key_manager = TaskManager()
        self.key_manager.bind(pygame.K_ESCAPE, self.__exit)
    
    def __exit(self):
        
        import sys 
        sys.exit()
    
    def update(self):
        pass 
    
    def run(self):
        
        while True:
            self.clock.tick(self.fps_cap)
            
            self.update()
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    
                    self.__exit()
                    
                self.key_manager.run_binds(event)
            
            pygame.display.flip()
    
    def get_dt(self) -> float:
        tn = gt()
        
        dt = tn - self.last_time
        self.last_time = tn 
        
        return dt
        
    def get_fps(self) -> float:
        
        return round(self.clock.get_fps(),2) 


game = Game()

if __name__ == '__main__':
    
    game.run()