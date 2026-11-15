import numpy as np


L1 = 5.0    # Coxa
L2 = 1.0    # Femur
L3 = 28.0   # Tibia


sudut_coxa  = 30.0
sudut_femur = 40.0
sudut_tibia = 30.0



def buat_matriks_dh(theta_derajat, d, a, alpha_derajat):
    # Ubah sudut dari derajat ke radian (karena numpy memakai radian)
    t  = np.radians(theta_derajat)
    al = np.radians(alpha_derajat)

    # Susun matriks ukuran 4x4 sesuai rumus standar Denavit-Hartenberg
    matriks = np.array([
        [np.cos(t), -np.sin(t) * np.cos(al),  np.sin(t) * np.sin(al), a * np.cos(t)],
        [np.sin(t),  np.cos(t) * np.cos(al), -np.cos(t) * np.sin(al), a * np.sin(t)],
        [0.0,        np.sin(al),              np.cos(al),             d],
        [0.0,        0.0,                     0.0,                    1.0]
    ])
    return matriks



#FORWARD KINEMATICS (Mencari Koordinat dari Sudut)

# Buat matriks untuk masing-masing sendi
T_coxa  = buat_matriks_dh(sudut_coxa,  d=0, a=L1, alpha_derajat=90)
T_femur = buat_matriks_dh(sudut_femur, d=0, a=L2, alpha_derajat=0)
T_tibia = buat_matriks_dh(sudut_tibia, d=0, a=L3, alpha_derajat=0)

# Kalikan ketiga matriks secara berurutan
T_total = T_coxa @ T_femur @ T_tibia

# Ambil koordinat X, Y, Z ujung kaki (ada di kolom ke-4 matriks T_total)
X = T_total[0, 3]
Y = T_total[1, 3]
Z = T_total[2, 3]

print("=== HASIL FORWARD KINEMATICS (MATRIKS) ===")
print("Matriks T_total:")
print(np.round(T_total, 4)) # Dibulatkan 4 angka di belakang koma agar rapi
print(f"\nKoordinat Ujung Kaki:")
print(f"X = {X:.4f} cm")
print(f"Y = {Y:.4f} cm")
print(f"Z = {Z:.4f} cm")

#Inverse Kinematics (Mencari Sudut dari Koordinat)
#maaf kakak-kakak, saya belum bisa menerjemahkan rumus inverse kinematics ke dalam kode python.