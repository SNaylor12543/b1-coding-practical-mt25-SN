def controller(Reference, Position):
    # Reference and Position should be two value arrays where Reference = [r(t-1), r(t)] and Position = [y(t-1), y(t)].
    
    # Defining Controller gain parameters:
    Kp = 0.15
    Kd = 0.6
    
    # Creating a new array of the error values
    Error = Reference - Position

    # u(t) = Kp * e(t) + Kd * (e(t) - e(t-1))
    System_Input = Kp * Error[1] + Kd * (Error[1] - Error[0])

    return System_Input