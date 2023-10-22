import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
amplitude = 1.0  # Amplitude da onda
frequencia = 1.0  # Frequência da onda
comprimento_onda = 2.0  # Comprimento de onda
velocidade = 1.0  # Velocidade da onda

# Gerar dados para o eixo x (espaço)
x = np.linspace(0, 4, 400)

# Gerar dados para o eixo y (amplitude da onda estacionária)
y = amplitude * np.sin(2 * np.pi * x / comprimento_onda) * np.cos(2 * np.pi * x * frequencia / velocidade)

# Plotar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Onda Estacionária', color='blue')

# Configurar os rótulos dos eixos
plt.title('Gráfico de Onda Estacionária')
plt.xlabel('Espaço')
plt.ylabel('Amplitude')

# Adicionar uma legenda
plt.legend()

# Exibir o gráfico
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)  # Linha horizontal do eixo y
plt.axvline(0, color='black', linewidth=0.5)  # Linha vertical do eixo x
plt.show
