import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent


cpu_percent()



get_ipython().run_line_magic('matplotlib', 'notebook')
frame_len = 200
y = []
fig = plt.figure(figsize=(6,3))
def animate(i):
    y.append(cpu_percent())

    if len(y) <= frame_len:
        plt.cla()
        plt.plot(y, 'r', label = 'Real-Time CPU Uses')
   
    else:
        plt.cla()
        plt.plot(y[-frame_len:], 'r', label = 'Real-Time CPU Uses')

    plt.ylim(0, 100)
    plt.xlabel('Time (s)')
    plt.ylabel('CPU Uses (%)')
    plt.legend(loc = 'upper right')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)




