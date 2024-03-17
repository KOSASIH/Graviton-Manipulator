import numpy as np

def create_graviton_manipulator(nim, graviton_strength):
    """
    Creates a Graviton Manipulator to manipulate gravitational forces on a localized scale.
    
    Parameters:
    nim (np.array): A 2D array representing the Neural Interface Matrix.
    graviton_strength (float): The strength of the graviton manipulator.
    
    Returns:
    np.array: A 2D array representing the Graviton Manipulator.
    """
    
    # Create the Graviton Manipulator by multiplying the NIM with the graviton strength
    graviton_manipulator = nim * graviton_strength
    
    return graviton_manipulator

def manipulate_gravitational_forces(graviton_manipulator, target_object):
    """
    Manipulates gravitational forces on a localized scale.
    
    Parameters:
    graviton_manipulator (np.array): A 2D array representing the Graviton Manipulator.
    target_object (np.array): A 1D array representing the target object.
    
    Returns:
    np.array: The manipulated gravitational forces.
    """
    
    # Manipulate the gravitational forces by multiplying the Graviton Manipulator with the target object
    manipulated_gravitational_forces = np.dot(graviton_manipulator, target_object)
    
    return manipulated_gravitational_forces
