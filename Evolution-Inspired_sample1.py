import random

num_particles = 5
particles = [random.uniform(-10,10) for _ in range(num_particles)]
velocities = [0]*num_particles

def fitness(x):
    return -(x**2) + 10

pbest = particles[:]
gbest = max(particles, key=fitness)

for iteration in range(10):

    for i in range(num_particles):

        velocities[i] = velocities[i] + random.random()*(pbest[i]-particles[i]) + random.random()*(gbest-particles[i])
        particles[i] = particles[i] + velocities[i]

        if fitness(particles[i]) > fitness(pbest[i]):
            pbest[i] = particles[i]

    gbest = max(particles, key=fitness)

    print("Iteration", iteration, "Best Value:", gbest)