import numpy as np


L_femur = 1.0     # Panjang Femur (cm)
L_tibia = 28.0    # Panjang Tibia (cm)

sudut_femur = 40.0  # Derajat
sudut_tibia = 30.0  # Derajat



def buat_matriks_2d(theta_derajat, panjang):
    t = np.radians(theta_derajat)  # Ubah derajat ke radian

    # Matriks rotasi + translasi pada bidang XY
    matriks = np.array([
        [np.cos(t), -np.sin(t), panjang * np.cos(t)],
        [np.sin(t),  np.cos(t), panjang * np.sin(t)],
        [0.0,        0.0,       1.0]
    ])
    return matriks



T_femur = buat_matriks_2d(sudut_femur, L_femur)
T_tibia = buat_matriks_2d(sudut_tibia, L_tibia)


T_total = T_femur @ T_tibia


X = T_total[0, 2]
Y = T_total[1, 2]

print("=== MATRIKS TRANSFORMASI TOTAL (2D XY) ===")
print(np.round(T_total, 4))

print("\n=== KOORDINAT UJUNG KAKI (BIDANG XY) ===")
print(f"X = {X:.4f} cm")
print(f"Y = {Y:.4f} cm")