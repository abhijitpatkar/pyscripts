#!/usr/bin/env python
class FibonacciSeries(object):
      """
      This class will be use to calculate the fibonacci Series
      """
      def __init__(self,limitNum,firstNum=0,secondNum=1):
          self.firstNum=firstNum
          self.secondNum=secondNum
          self.limitNum=limitNum
          self.numContainer=[]
          
      def calculateSeries(self):
          for num in range(self.limitNum):
              
              self.firstNum,self.secondNum=self.secondNum,self.firstNum+self.secondNum
              self.numContainer.append(self.secondNum)

      def displaySeries(self):
          print(self.numContainer)


if __name__=="__main__":
   FiboObj=FibonacciSeries(5)
   FiboObj.calculateSeries()
   FiboObj.displaySeries() 
                    
