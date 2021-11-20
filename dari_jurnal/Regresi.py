import numpy as np
import pandas as pd
from matplotlib import colors, pyplot as plt
from sklearn.linear_model import LinearRegression

#########################################################
# Kelompok  : 5                                         #
# Kelas     : TF3A4                                     #
# Nama      :   1. M.FERDY HASAN (202010225204)         #
#               2. SYACHRUL RAMADHAN (202010225151)     #
#               3. Muchammad Prasetyo (202110717001)    #
#########################################################

df = pd.DataFrame([[1, 2055], [2, 2847], [3, 9519], [4, 11505], [5, 13440], [6, 15211]])

df.columns = ['x', 'y']
x_train = df['x'].values[:, np.newaxis]
y_train = df['y'].values
lm = LinearRegression()

lm.fit(x_train, y_train)  # fase training

print('Coefficient :' + str(lm.coef_))
print('Intercept :' + str(lm.intercept_))
x_test = [[7],[8]]  # data yang akan diprediksi
p = lm.predict(x_test)  # fase prediksi
print('hasil prediksi : '+str(p))  # hasil prediksi

#prepare plot
pb = lm.predict(x_train)
dfc = pd.DataFrame({'x': df['x'], 'y': pb})
plt.scatter(df['x'], df['y'])
plt.plot(dfc['x'], dfc['y'], color='red', linewidth=2)
plt.ylabel('Pendapatan', fontsize=14)
plt.xlabel('Bulan Ke-', fontsize=14)
plt.title('PENDAPATAN REKSA DANA DALAM SETAHUN', fontsize=14)
plt.show()
