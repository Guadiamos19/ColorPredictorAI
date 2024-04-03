import math
import numpy as np

class NeuralNetwork:

 @staticmethod
 def sigmoid(weights):


  for x in np.nditer(weights, op_flags=['readwrite']):

    x[...] = 1.0 / (1 + math.exp(-x))

  return weights


 @staticmethod
 def sigmoid_derivative(weights):

     weights = weights * (1.0 - weights)

     return weights







 def feedForward(self):

     self.FirLW.shape = (3, 3)
     self.SecLW.shape = (3, 2)
     self.outputs.shape = (1, 2)
     self.HiddenLayer.shape = (1, 3)
     self.inputs.shape = (1, 3)


     self.HiddenLayer = np.dot(self.inputs, self.FirLW)




     self.HiddenLayer = NeuralNetwork.sigmoid(np.copy(self.HiddenLayer))




     self.outputs = np.dot(self.HiddenLayer, self.SecLW)


     #ox, oy = self.outputs.shape

     self.outputs = NeuralNetwork.sigmoid(np.copy(self.outputs))






#BackProgagation
 def feedBack(self, y):







  OutPutDerivative = NeuralNetwork.sigmoid_derivative(np.copy(self.outputs))
  LayerDerivative = NeuralNetwork.sigmoid_derivative(np.copy(self.HiddenLayer))



  d_weights2 = np.dot(self.HiddenLayer.T, (2 * (y - self.outputs) * OutPutDerivative))




  d_weights1 = np.dot(self.inputs.T, (np.dot(2 * (y - self.outputs) * OutPutDerivative, self.SecLW.T )* LayerDerivative))



  self.SecLW += d_weights2
  self.FirLW += d_weights1





 def __init__(self, inputs):

        self.inputs = inputs
        self.FirLW = np.random.rand(9,1)
        self.SecLW = np.random.rand(6,1)
        self.HiddenLayer = np.array([0,0,0])
        self.outputs = np.array([0,0])


        for i in range(self.inputs.size):
            self.inputs[i] /= 255
        #print(inputs)
        self.FirLW.shape = (3, 3)
        self.SecLW.shape = (3, 2)
        self.outputs.shape = (1, 2)
        self.HiddenLayer.shape = (1, 3)
        self.inputs.shape = (1, 3)
















