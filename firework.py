import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to simulate fireworks explosion
def generate_firework(x, y, num_particles=100):
    # Randomly distributed particles at different angles
    angles = np.random.uniform(0, 2*np.pi, num_particles)
    speeds = np.random.uniform(1, 5, num_particles)
    
    # Calculate the x and y velocities of each particle
    vx = speeds * np.cos(angles)
    vy = speeds * np.sin(angles)
    
    # Initial positions of particles (centered at (x, y)) - cast to float
    particles_x = np.full(num_particles, float(x))
    particles_y = np.full(num_particles, float(y))
    
    return particles_x, particles_y, vx, vy

# Function to update the firework particles for animation
def update_firework(num, particles_x, particles_y, vx, vy, scat):
    # Update positions based on velocity
    particles_x += vx
    particles_y += vy
    
    # Update the scatter plot data
    scat.set_offsets(np.c_[particles_x, particles_y])
    return scat,

# Set up the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Set the background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Remove axis for a cleaner look
ax.axis('off')

# Generate a firework at the center (x=0, y=0) with 500 particles
particles_x, particles_y, vx, vy = generate_firework(0, 0, num_particles=500)

# Set up the scatter plot to animate the particles with color
scat = ax.scatter(particles_x, particles_y, c=np.random.rand(500), s=10, alpha=0.8)

# Create the animation with 20 seconds duration (20 seconds = 1000 ms per frame * 200 frames)
ani = animation.FuncAnimation(fig, update_firework, fargs=(particles_x, particles_y, vx, vy, scat),
                              frames=40000,  # 400 frames for 20 seconds animation (50 ms per frame)
                              interval=100,  # 50ms per frame for smooth animation
                              blit=True)

plt.show()
