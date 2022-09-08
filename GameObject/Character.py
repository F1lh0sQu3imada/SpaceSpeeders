from GameObject.GameObject import GameObject
from GameObject.Shot import Shot
import pygame

class Character(GameObject):
    Shots = []
    CharacterWidth = 80
    CharacterHeight = 80
    Health = 3

    def __init__(self, position):
        super().__init__(
            self.CharacterWidth,
            self.CharacterHeight,
            position,
            5,
            pygame.image.load("assets/spaceship.png")
        )       

    def moveUp(self):
        self.movement += pygame.Vector2(0, -1)

    def moveDown(self):
        self.movement += pygame.Vector2(0, 1)

    def moveLeft(self):
        self.movement += pygame.Vector2(-1, 0)

    def moveRight(self):
        self.movement += pygame.Vector2(1, 0)

    def move(self):
        if self.movement == pygame.Vector2(0, 0):
            return

        VectorMovement = self.movement.normalize() * self.acceleration

        VectorMovementX = (VectorMovement[0], 0)
        VectorMovementY = (0, VectorMovement[1])

        self.position += pygame.Vector2(VectorMovementX)
        if self.isOutOfBounds():
            self. position -= pygame.Vector2(VectorMovementX)

        self.position += pygame.Vector2(VectorMovementY)
        if self.isOutOfBounds():
            self. position -= pygame.Vector2(VectorMovementY)
        
        # Stop  movement
        self.movement = pygame.Vector2(0, 0)

    def fire(self, pos):
        shot = Shot(pygame.Vector2(self.getCenter()))
        shot.movement = pos - pygame.Vector2(self.getCenter())
        self.Shots.append(shot)

    def takeDamage(self):
        self.Health -= 1

    def getHealth(self):
        return self.Health