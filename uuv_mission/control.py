import numpy as np

class Controller:
    def __init__(self):
        self.Kp = 0.15
        self.Kd = 0.6
    
    def controller(self, Reference: np.ndarray, Position: np.ndarray, T: int):
        # Reference and Position should be the full arrays, and T should be the time starting from 0

        # Defining Proportional and Differential Gain values
        #Kp = 0.15
        #Kd = 0.6

        # Creating Error array
        Error = np.subtract(Reference, Position)

        # u(t) = Kp * e(t) + Kd * (e(t) - e(t-1))
        System_Input = self.Kp * Error[T] + self.Kd * (Error[T] - Error[T-1])

        return System_Input
    