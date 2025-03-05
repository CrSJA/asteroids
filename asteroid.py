from circleshape import *

class asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.time_of_existence=40
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)
    
    def update(self,dt):
        self.position +=self.velocity*dt
        self.time_of_existence-=dt
        if self.time_of_existence < 0:
            self.kill()

