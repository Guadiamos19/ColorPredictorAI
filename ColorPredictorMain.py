from NN import *
from Graphics import *
from Mouse import *
import random
from WeightFile import *
import numpy as np







inputs = np.array([float(random.randint(0,255)),float(random.randint(0,255)),float(random.randint(0,255))])
black = np.array([0,1])
white = np.array([1,0])

black.shape = (1,2)
white.shape = (1,2)


graphicsRenderer = GraphicsRenderer(inputs[0],inputs[1] ,inputs[2] )
graphicsRenderer.init()
mouseInput = Mouse(graphicsRenderer.circleOneX, graphicsRenderer.circleOneY , graphicsRenderer.circleTwoX,graphicsRenderer.circleTwoY, graphicsRenderer.circleRadius)


wp = WeightFile()

brain = NeuralNetwork(inputs)


wp.loadWeights(brain.FirLW, brain.SecLW)


brain.feedForward()







running = True

while running:


 graphicsRenderer.scene()

 pygame.display.flip()
 graphicsRenderer.clock.tick(60)

 if(brain.outputs[0][0] < brain.outputs[0][1]):
  pygame.draw.circle(graphicsRenderer.Display, (255, 255, 255),[int(graphicsRenderer.circleOneX), int(graphicsRenderer.circleOneY + 200)], 50)
  pygame.draw.circle(graphicsRenderer.Display, (0, 0, 0), [int(graphicsRenderer.circleTwoX), int(graphicsRenderer.circleTwoY + 200)], 50)
 else:
  pygame.draw.circle(graphicsRenderer.Display, (255, 255, 255),[int(graphicsRenderer.circleTwoX), int(graphicsRenderer.circleTwoY + 200)], 50)
  pygame.draw.circle(graphicsRenderer.Display, (0, 0, 0),[int(graphicsRenderer.circleOneX), int(graphicsRenderer.circleOneY + 200)], 50)



 for event in pygame.event.get():



  if event.type == pygame.QUIT:
     running = False



  if event.type == pygame.MOUSEBUTTONDOWN:

   if event.button == 1:

    #print(brain.outputs)

    if mouseInput.hitsPreferedCircle() == 0:
     brain.feedBack(black)

     wp.writeToFile(brain.FirLW, brain.SecLW)

     inputs = np.array([float(random.randint(0, 255)), float(random.randint(0, 255)), float(random.randint(0, 255))])
     graphicsRenderer.r = inputs[0]
     graphicsRenderer.g = inputs[1]
     graphicsRenderer.b = inputs[2]

     for i in range(inputs.size):

       inputs[i] /= 255

     brain.inputs = inputs
     brain.feedForward()



    elif mouseInput.hitsPreferedCircle() == 1:
     brain.feedBack(white)

     wp.writeToFile(brain.FirLW, brain.SecLW)

     inputs = np.array([float(random.randint(0, 255)), float(random.randint(0, 255)), float(random.randint(0, 255))])
     graphicsRenderer.r = inputs[0]
     graphicsRenderer.g = inputs[1]
     graphicsRenderer.b = inputs[2]

     for i in range(inputs.size):
         inputs[i] /= 255


     brain.inputs = inputs
     brain.feedForward()


   elif event.button == 3:

      #print(brain.outputs)
      inputs = np.array([float(random.randint(0, 255)), float(random.randint(0, 255)), float(random.randint(0, 255))])
      graphicsRenderer.r = inputs[0]
      graphicsRenderer.g = inputs[1]
      graphicsRenderer.b = inputs[2]

      for i in range(inputs.size):
        inputs[i] /= 255

      brain.inputs = inputs
      brain.feedForward()