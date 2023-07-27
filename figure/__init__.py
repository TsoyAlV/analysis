import pandas as pd
import matplotlib.pyplot as plt


def plot(dfi, colsi=None, start=None, stop=None, title=None):
    """
    Выводит plot. start и stop - опционально
    """
    figure, ax = plt.subplots()
    figure.set_size_inches((12, 4))
    if start != None and stop != None:
        if colsi != None:
            ax.plot(dfi[start:stop][colsi])
        else:
            ax.plot(dfi[start:stop])
    elif start != None and stop == None:
        if colsi != None:
            ax.plot(dfi[start:][colsi])
        else:
            ax.plot(dfi[start:])
    elif start == None and stop != None:
        if colsi != None:
            ax.plot(dfi[:stop][colsi])
        else:
            ax.plot(dfi[:stop])
    else:
        if colsi != None:
            ax.plot(dfi[:][colsi])
        else:
            ax.plot(dfi[:])

    if title == None:
        pass
    else:
        ax.set_title(title)
    ax.grid()
    figure.show()
