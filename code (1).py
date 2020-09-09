from numpy.random import choice

def simulate(start_state, N, q_1, q_2, boundary):
    states = [start_state]

    for i in range(0, N):
        new_pos = (0,0)
        new_is_on_boundary = False

        if states[-1][1] == False:
            # probabilities for non-boundary [stay, left, right, down, up]
            n = choice([1, 2, 3, 4, 5], p=[1-q_1-q_2, q_1/2, q_1/2, q_2/2, q_2/2])

            if n == 1:
                new_pos = states[-1][0]
            elif n == 2:
                new_pos = (states[-1][0][0] - 1, states[-1][0][1])
            elif n == 3:
                new_pos = (states[-1][0][0] + 1, states[-1][0][1])
            elif n == 4:
                new_pos = (states[-1][0][0], states[-1][0][1] - 1)
            elif n == 5:
                new_pos = (states[-1][0][0], states[-1][0][1] + 1)

        else:
            n_1 = choice([1, 2], p=[1-(q_1/2), q_1/2]) # probabilities for horizontal reflective boundarys
            n_2 = choice([1, 2], p=[1-(q_2/2), q_2/2]) # probabilities for vertical reflective boundarys

            if states[-1][0][0] == -boundary and n_1 == 1:
                new_pos = states[-1][0]

            elif states[-1][0][0] == -boundary and n_1 == 2:
                new_pos = (states[-1][0][0] + 1, states[-1][0][1])

            elif states[-1][0][0] == boundary and n_1 == 1:
                new_pos = states[-1][0]

            elif states[-1][0][0] == boundary and n_1 == 2:
                new_pos = (states[-1][0][0] - 1, states[-1][0][1])

            elif states[-1][0][1] == -boundary and n_2 == 1:
                new_pos = states[-1][0]

            elif states[-1][0][1] == -boundary and n_2 == 2:
                new_pos = (states[-1][0][0], states[-1][0][1] + 1)

            elif states[-1][0][1] == boundary and n_2 == 1:
                new_pos = states[-1][0]

            elif states[-1][0][1] == boundary and n_2 == 2:
                new_pos = (states[-1][0][0], states[-1][0][1] - 1)

        if abs(new_pos[0]) == boundary or abs(new_pos[1]) == boundary:
            new_is_on_boundary = True

        states.append((new_pos, new_is_on_boundary))

    return [i[0] for i in states]

boundary = 5
num_sim = 1000
walk_length = 5

simulation_results = [simulate(((0,0), False), walk_length, 0.4, 0.4, boundary) for i in range(0, num_sim)]

results = [sublist[-1] for sublist in simulation_results]

from matplotlib import pyplot as plt

x = []
y = []

for i in results:
    x.append(i[0])
    y.append(i[1])

bins_1d = [i-0.5 for i in range(-boundary, boundary+1)]

import numpy as np

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(x,y, bins = [bins_1d, bins_1d], normed = True)

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

fig.suptitle('Simulation with q1 = q2 = 0.4', fontsize=20)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('density')

plt.savefig('foo.png')
plt.show()
