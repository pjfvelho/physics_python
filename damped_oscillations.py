import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a oscilação amortecida
def oscillation(t, m, c, k):
    omega_n = np.sqrt(k / m)  # Frequência natural não amortecida
    if c == 2 * m * omega_n:   # Critically Damped
        return (1 + omega_n * t) * np.exp(-omega_n * t)
    elif c < 2 * m * omega_n:  # Underdamped (Subamortecido)
        omega_d = np.sqrt(omega_n**2 - (c / (2 * m))**2)  # Frequência amortecida
        A = 1  # Amplitude
        phi = np.arctan2(omega_d, (c / (2 * m)))  # Fase
        return A * np.exp(-(c / (2 * m)) * t) * np.cos(omega_d * t + phi)
    else:  # Overdamped (Superamortecido)
        omega_d1 = (-c / (2 * m)) + np.sqrt((c / (2 * m))**2 - omega_n**2)
        omega_d2 = (-c / (2 * m)) - np.sqrt((c / (2 * m))**2 - omega_n**2)
        A1 = 1 / (2 * np.sqrt((c / (2 * m))**2 - omega_n**2))
        A2 = 1 / (2 * np.sqrt((c / (2 * m))**2 - omega_n**2))
        return A1 * np.exp(omega_d1 * t) + A2 * np.exp(omega_d2 * t)

# Parâmetros
m = 10.0  # Massa
k = 1.0  # Constante da mola
c_critico = 2.0 * np.sqrt(m * k)  # Coeficiente de amortecimento crítico
c_subamortecido = 0.8 * c_critico  # Coeficiente de amortecimento subamortecido
c_superamortecido = 1.2 * c_critico  # Coeficiente de amortecimento superamortecido

# Tempo
t = np.linspace(0, 10, 1000)

# Calcule as oscilações para os três casos
oscillation_critico = oscillation(t, m, c_critico, k)
oscillation_subamortecido = oscillation(t, m, c_subamortecido, k)
oscillation_superamortecido = oscillation(t, m, c_superamortecido, k)

# Crie os gráficos
plt.figure(figsize=(12, 4))

plt.subplot(131)
plt.plot(t, oscillation_critico)
plt.title("Oscilação Crítica")

plt.subplot(132)
plt.plot(t, oscillation_subamortecido)
plt.title("Oscilação Subamortecida")

plt.subplot(133)
plt.plot(t, oscillation_superamortecido)
plt.title("Oscilação Superamortecida")

plt.tight_layout()
plt.show()
