import numpy as np
import matplotlib.pyplot as plt

def plot_sine(frequency=1.0, amplitude=1.0, phase=0.0):
    t = np.linspace(0, 2 * np.pi, 500)
    y = amplitude * np.sin(frequency * t + phase)

    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title(f"Sine Wave: {amplitude}·sin({frequency}·t + {phase})")
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
