# Module to generate time varying electric field and save as a series of txt files
import numpy as np

def uniform_field(filename, V):
    Y_lim=[-200,200]
    field = np.zeros((len( range(Y_lim[0],Y_lim[1]))))
    for i, y in enumerate(range(Y_lim[0],Y_lim[1])):
        field[i]=V
    np.savetxt(filename, field)
        
        
    
    
