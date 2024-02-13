import matplotlib.pyplot as plt

alltimes = []
allspeeds = []
allangels = []
times = []
angles = []
speeds = []
with open('data.csv', 'r') as csvfile:
    for line in csvfile:
        if line.strip() == 'end':
            alltimes.append(times)
            allangels.append(angles)
            allspeeds.append(speeds)
            times = []
            angles = []
            speeds = []
            continue
        time, angle, speed = map(float, line.strip().split(','))
        times.append(time)
        angles.append(angle)
        speeds.append(speed)
for i in range(len(alltimes)):
    plt.plot(alltimes[i], allspeeds[i])
plt.xlabel('time')
plt.ylabel('speed')
plt.show()
