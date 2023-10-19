import pygame 
from pygame.math import Vector2 as v

from scripts.enemies import create_random_enemy

def get_move_towards_vel(p1, p2):
    
    return v(p1).move_towards(p2, 1) - v(p1)

def distance_to(p1,p2):
    
    return v(p1).distance_to(p2)

class Level:

    def __init__(self,game, enemy_len) -> None:
        
        self.enemies = [create_random_enemy() for i in range(enemy_len)]
        self.points = []
        self.tilemap = {}
        self.castle_hp = 5
        self.game =game
        
    def update_enemies(self, dt):
        
        for enemy in self.enemies:
            enemy.set_goal_pos(self.points[enemy.goal_index])
            
            enemy.pos[0] += get_move_towards_vel(enemy.pos, enemy.goal_pos).x  * dt
            enemy.pos[1] += get_move_towards_vel(enemy.pos, enemy.goal_pos).y * dt
            
            if distance_to(enemy.pos, enemy.goal_pos)<3:
                
                enemy.goal_index += 1
                
                if enemy.goal_index > len(self.points) -1 :
                    
                    self.enemies.remove(enemy)
                    self.castle_hp -= 1
                    continue
                
    def render_enemies(self, display : pygame.Surface):
        
        [enemy.animate() for enemy in self.enemies]
        
        display.fblits(([enemy.image, enemy.pos] for enemy in self.enemies))
                
    def add_point(self, point):
        
        self.points.append(point)
        
    def draw_world(self) -> pygame.Surface:
        
        keys = list(self.tilemap.keys())
        largest_x = 0
        largest_y = 0
        for key in keys:
            x,y = map(int, key.split(';'))
            
            if x > largest_x:
                largest_x = x 
            if y > largest_y:
                largest_y = y
                
        world_surf = pygame.Surface((largest_x * 24 + 24, largest_y * 24 + 24))
        
        for key in self.tilemap:
            
            x,y =  map(int, key.split(';'))
            
            tile = self.tilemap[key][0]
            
            tile_x, tile_y = x*24, y*24 
            
            world_surf.blit(self.game.tile_imgs[tile], (tile_x, tile_y))
            
        return world_surf
