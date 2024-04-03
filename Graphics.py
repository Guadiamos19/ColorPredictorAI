import pygame


class GraphicsRenderer:


 def init(self):

  self.Display = pygame.display.set_mode((1280, 720))


  pygame.display.set_caption("Color Predictor")

  self.clock = pygame.time.Clock()
  pygame.font.init()
  self.circleFont = pygame.font.SysFont("comicsansms", 36)
  self.circleOneText = self.circleFont.render("Text", True, (0, 0, 0))
  self.circleTwoText = self.circleFont.render("Text", True, (255, 255, 255))
  self.QuestionText = self.circleFont.render("Does White or Black look better over this color?", True, (255, 255, 255))

  self.Display.fill((0,0,0))

  surface = pygame.display.get_surface()
  self.circleOneX = surface.get_width() / 3
  self.circleOneY = surface.get_height() / 2
  self.circleTwoX = 2 * surface.get_width() / 3
  self.circleTwoY = surface.get_height() / 2
  self.circleRadius = 100
  self.QuestionX = surface.get_width() / 2
  self.QuestionY = 36



 def scene(self):

  #surface = pygame.display.get_surface()

  pygame.draw.circle(self.Display, (self.r, self.g, self.b), [int(self.circleOneX ), int(self.circleOneY )], self.circleRadius)
  pygame.draw.circle(self.Display, (self.r, self.g, self.b), [int(self.circleTwoX ), int(self.circleTwoY )], self.circleRadius)


  self.Display.blit(self.circleOneText,( self.circleOneX - self.circleOneText.get_width() / 2, self.circleOneY - self.circleOneText.get_height() / 2))
  self.Display.blit(self.circleTwoText, (self.circleTwoX - self.circleTwoText.get_width() / 2, self.circleTwoY - self.circleTwoText.get_height() / 2))
  self.Display.blit(self.QuestionText , (self.QuestionX - self.QuestionText.get_width() / 2, self.QuestionY))

 def __init__(self, r ,g ,b):

  self.r = r
  self.g = g
  self.b = b




