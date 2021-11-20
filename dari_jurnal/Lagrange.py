import numpy as np
import matplotlib.pyplot as plt

#########################################################
# Kelompok  : 5                                         #
# Kelas     : TF3A4                                     #
# Nama      :   1. M.FERDY HASAN (202010225204)         #
#               2. SYACHRUL RAMADHAN (202010225151)     #
#               3. Muchammad Prasetyo (202110717001)    #
#########################################################
# membaca jumlah titik data
n = int(input('Masukan jumlah titik data : '))

# membuat array ukuran n x n dan inisiasi
x = np.zeros((n))
y = np.zeros((n))

xx = []
yy = []

# membaca titik data
print('Masukan data x dan y : ')
for i in range(n):
    x[i] = float(input('x['+str(i)+'] = '))
    xx.append(x[i])
    y[i] = float(input('y['+str(i)+'] = '))
    yy.append(y[i])

# membaca interpolasi titik
xp = float(input('Masukan x yang diinginkan : '))

# inisiasi interpolasi
yp = 0

# implementasi interpolasi lagrange
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p*(xp - x[j])/(x[i] - x[j])
        yp = yp + p * y[i]

# display output
print('Nilai interpolasi untuk %.3f adalah %.3f.' % (xp, yp))

plt.plot(xx, yy, 'bo')
plt.ylabel('Pendapatan', fontsize=14)
plt.xlabel('Bulan Ke-', fontsize=14)
plt.title('PENDAPATAN REKSA DANA DALAM SETAHUN', fontsize=14)
plt.show()
