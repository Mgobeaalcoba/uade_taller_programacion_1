import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define los conjuntos A y B
A = set([1, 2, 3, 4, 5])
B = set([4, 5, 6, 7, 8])

# Crear esquema de Venn para la unión e intersección de A y B
plt.figure(figsize=(12, 6))

# Unión de los conjuntos A y B
plt.subplot(1, 2, 1)
venn2([A, B], ('A', 'B'))
plt.title('Unión de A y B')

# Intersección de los conjuntos A y B
plt.subplot(1, 2, 2)
venn2([A, B], ('A', 'B'))
plt.title('Intersección de A y B')

plt.show()
