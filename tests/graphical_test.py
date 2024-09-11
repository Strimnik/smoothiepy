import matplotlib.pyplot as plt
import numpy as np
from smoothiepy.easing_functions import *

def plot_easing_functions():
    t = np.linspace(0, 1, 500)

    easing_functions = {
        'Exponential': Exponential(),
        'Quad': Quad(),
        'Back': Back(),
        'Bounce': Bounce(),
        'Elastic': Elastic(),
        'Sine': Sine(),
        'Circ': Circ(),
        'Cubic': Cubic(),
        'Quart': Quart(),
        'Quint': Quint(),
    }

    plt.figure(figsize=(14, 10))
    for name, func in easing_functions.items():
        plt.plot(t, [func.out(x) for x in t], label=f'{name} Out')
        plt.plot(t, [func.in_(x) for x in t], '--', label=f'{name} In')
        plt.plot(t, [func.in_out(x) for x in t], ':', label=f'{name} In-Out')
        plt.plot(t, [func.out_in(x) for x in t], '-.', label=f'{name} Out-In')

    plt.title('Easing Functions')
    plt.xlabel('t')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_easing_functions()