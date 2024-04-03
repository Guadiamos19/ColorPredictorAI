import pygame
import math;


class Mouse:

 @staticmethod
 def getDistance(circleX, circleY, mouseX , mouseY):

  x = math.fabs(circleX - mouseX)
  y = math.fabs(circleY - mouseY)


  return math.sqrt(((x * x) + (y * y)))



 def hitsPreferedCircle(self):

   mousex, mousey = pygame.mouse.get_pos()


   if Mouse.getDistance(self.CircleOneX , self.CircleOneY, mousex, mousey) < self.CircleRadius:

    return 0

   elif Mouse.getDistance(self.CircleTwoX, self.CircleTwoY, mousex, mousey) < self.CircleRadius:

    return 1

   else:

    return 2


 def __init__(self, CircleOneX, CircleOneY, CircleTwoX, CircleTwoY, CircleRadius):


   self.CircleOneX = CircleOneX
   self.CircleOneY = CircleOneY
   self.CircleTwoX = CircleTwoX
   self.CircleTwoY = CircleTwoY
   self.CircleRadius = CircleRadius
