import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('/content/drive/My Drive/proyecto_ventas/ventas_productos.csv')

# Calcular el precio total por producto
df['Precio_Total'] = df['Cantidad'] * df['Precio']

# Mostrar los primeros registros
print(df.head())

# Crear un gráfico de barras
plt.bar(df['Producto'], df['Precio_Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')

# Guardar el gráfico como PNG en Google Drive
plt.savefig('/content/drive/My Drive/proyecto_ventas/grafico_precios.png')
plt.show()
