import pygame 


class TaskManager:
    
    def __init__(self):
        
        self.binds = []
        
    def bind(self, key, function, args = []):
        
        self.binds.append((key, function, args))
        
    def run_binds(self, event):
        
        for bind in self.binds:
                        
            if not event.type == pygame.KEYDOWN:
                return 
            if not event.key == bind[0]:
                continue 
                
            bind[1](*bind[2])
                