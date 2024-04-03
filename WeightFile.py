import numpy as np
import os


class WeightFile:


 @staticmethod
 def loadWeights(firstLayerWeights, secondLayerWeights):


  firstLayerWeights.shape = [9,]
  secondLayerWeights.shape = [6,]

  if os.path.exists("weights.txt"):

   file = open("weights.txt" , 'r')

   firstWeightData = []
   secondWeightData = []


   f = file.readline()


   for i in f:

    if f.startswith("Weights1: "):

        f = f.replace("Weights1: ", "")

        firstWeightData = f.split()

    elif f.startswith("Weights2: "):
        f = f.replace("Weights2: ", "")
        secondWeightData = f.split()

    f = file.readline()

   for weightIndex1 , weightValue1 in enumerate(firstWeightData):

       firstLayerWeights[weightIndex1] = float(weightValue1)



   for weightIndex2 , weightValue2 in enumerate(secondWeightData):

       secondLayerWeights[weightIndex2] = float(weightValue2)


   firstLayerWeights.shape = (3,3)
   secondLayerWeights.shape = (3,2)





 @staticmethod
 def writeToFile(firstLayerWeights, secondLayerWeights):

  file = open(r"weights.txt","w")
  file.seek(0)  # <- This is the missing piece
  file.truncate()

  file.write("Weights1: ")

  for x in np.nditer(firstLayerWeights, op_flags=['readwrite']):

     file.write(str(x) + " ")


  file.write('\n')

  file.write("Weights2: ")

  for y in np.nditer(secondLayerWeights, op_flags=['readwrite']):

     file.write(str(y) + " ")


 def __init__(self):
    pass