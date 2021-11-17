import numpy as np
import matplotlib.pyplot as plt 

def desenho(lista,titulo,cor_controle, cor_TW):
    for j in range(50):   
        plt.plot(lista[j], color=cor_controle)
        plt.plot(lista[j+50], color=cor_TW)

    plt.title(titulo, weight='bold')
    plt.xlabel('R_disco')
    plt.ylabel('f - abe(f)')
    plt.legend(['CONTROLE', 'TW'], loc=0)
    plt.grid('on')
    plt.show()
