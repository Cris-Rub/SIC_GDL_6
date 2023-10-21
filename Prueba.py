from matplotlib import pyplot as plt
from matplotlib import animation
from gpiozero import DHT11
import numpy as np

sensor = DHT11(pin=20)

fig = plt.figure()
ax = plt.axes(xlim=(0, 30), ylim=(15, 45))
max_points = 30
line, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float) * np.nan, lw=1, c='blue', marker='d', ms=2)

def init():
    return line

def get_temperature():
    # Leer datos del sensor DHT11
    humidity = sensor.humidity
    temperature = sensor.temperature

    return temperature

def animate(i):
    temperature = get_temperature()
    y = temperature
    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=2000, blit=False)
plt.show()
