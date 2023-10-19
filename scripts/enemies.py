import pygame 
from random import choice



class Enemy:
    
    def __init__(self,game, type, speed, damage, health) -> None:
        self.type, self.speed, self.damage, self.health = type, speed, damage, health 
        self.game = game
        
        self.pos = []
        self.goal_pos = []
        self.goal_index = 0
        
        self.images = self.game.assets['enemies'][self.type]
        self.image = self.game.assets['enemies'][self.type][0]
        self.index = 0 
        self.anim_time = 150 
        self.next_anim = pygame.time.get_ticks() + self.anim_time
        
    def set_goal_pos(self, pos):
        
        self.goal_pos = pos 
        
    def rect(self):
        
        return pygame.Rect(*self.pos, *self.images[0].get_size())
    
    def animate(self):
        
        tn = pygame.time.get_ticks()
        if tn > self.next_anim:
            
            if self.index > len(self.images)-1:
                self.index = 0
            
            self.index += 1
            
            self.next_anim = tn + self.anim_time
            
        self.image = self.images[self.index]
        

    
    def copy(self):
        
        return Enemy(self.type, self.speed, self.damage, self.health)
    
enemy_presets = [
    Enemy('normal', 3, 5, 20),
    Enemy('fast', 4 , 3, 15),
    Enemy('buff', 2, 10, 25),
]
    
def create_random_enemy():
    
    return choice(enemy_presets).copy()