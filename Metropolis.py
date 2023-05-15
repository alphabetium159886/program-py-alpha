import numpy as np
import matplotlib.pyplot as plt

def initialize_spins(N):
    spins = np.random.choice([-1, 1], size=(N, N))
    return spins

def calculate_energy(spins):
    energy = np.sum(-J * (spins * np.roll(spins, 1, axis=0) + spins * np.roll(spins, -1, axis=0)
                  + spins * np.roll(spins, 1, axis=1) + spins * np.roll(spins, -1, axis=1)))
    return energy

def metropolis_step(spins, T):
    i = np.random.randint(N)
    j = np.random.randint(N)
    delta_E = 2 * J * spins[i, j] * (spins[(i+1)%N, j] + spins[(i-1)%N, j]
                                  + spins[i, (j+1)%N] + spins[i, (j-1)%N])
    if delta_E < 0 or np.random.rand() < np.exp(-delta_E / (k * T)):
        spins[i, j] *= -1

def calculate_magnetization(spins):
    return np.mean(spins)

def simulate_ising_model(N, J, k, T_values, num_steps, num_equilibration):
    magnetizations = []

    for T in T_values:
        spins = initialize_spins(N)
        
        # Equilibration
        for _ in range(num_equilibration):
            metropolis_step(spins, T)
        
        # Monte Carlo steps
        for _ in range(num_steps):
            metropolis_step(spins, T)

        magnetization = calculate_magnetization(spins)
        magnetizations.append(magnetization)

    return magnetizations

# Parameters
N = 100  # Grid size
J = 1.0  # Exchange constant
k = 1.0  # Boltzmann constant
T_values = np.linspace(0.5, 5.0, 20)  # Temperature values
num_steps = 10000  # Number of Monte Carlo steps per temperature
num_equilibration = 1000  # Number of equilibration steps per temperature

# Simulate Ising model
magnetizations = simulate_ising_model(N, J, k, T_values, num_steps, num_equilibration)

# Plot results
plt.plot(T_values, magnetizations)
plt.xlabel('Temperature (T)')
plt.ylabel('Magnetization')
plt.title('Monte Carlo Ising Model')
plt.show()
