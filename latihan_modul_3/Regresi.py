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

df= pd.DataFrame([[0.1,0.003],[0.3,0.067],[0.5,0.148],[0.7,0.248],[0.9,0.370],[1.1,0.518],[1.3,0.697]])

df.columns = ['x', 'y']
x_train = df['x'].values[:,np.newaxis]
y_train = df['y'].values
lm = LinearRegression()

lm.fit(x_train,y_train) #fase training 

print('Coefficient :' + str(lm.coef_))
print('Intercept :' + str(lm.intercept_))
x_test = [[0.85]] #data yang akan diprediksi
p = lm.predict(x_test) #fase prediksi
print('hasil prediksi : '+str(p)) #hasil prediksi

#prepare plot
pb = lm.predict(x_train)
dfc = pd.DataFrame({'x':df['x'], 'y':pb})
plt.scatter(df['x'],df['y'])
plt.plot(dfc['x'],dfc['y'],color='red', linewidth=2)
plt.xlabel('x', fontsize=14)
plt.ylabel('f(x)', fontsize=14)
plt.title('Latihan Modul 3', fontsize=14)
plt.show()