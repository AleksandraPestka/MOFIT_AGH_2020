from config import *

def v_deriv(coor, r):
    """ Calculate acceleration in the x or y direction. 

    Parameters:

    coor: float
    coordinate x or y

    r: float
    radius
    """
    return -G*M*coor/(r**3)

