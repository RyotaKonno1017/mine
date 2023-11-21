"""
第8回 フィッティング

多項式の2次近似を行うプログラム
"""
import numpy as np
import matplotlib.pyplot as plt

"""データの読み込みと確認"""
# 読み込むデータのファイル名
filename = "LSDataEx2.txt" #修正箇所（ファイル）指定の為必須

# データファイルの読み込み
x_data, y_data = np.loadtxt(filename, unpack=True)  # 2次元配列のデータ
n_of_data = len(x_data) # データの個数

# 計測データを散布図でプロット
fig = plt.figure()
ax = plt.subplot(111)
# 散布図 (四角形(s)の青色(blue)のマーカーで, マーカーのサイズ25)
ax.scatter(x_data, y_data, marker="s", color="blue", s=25) 
ax.set_xlabel("Input [V]")
ax.set_ylabel("Output [V]")
plt.grid()
plt.show()


"""最小二乗法"""
# 1. Aの準備
# Aの中の0次の列 を準備
# [[1.]
#  [1.]
#  [1.]
#  [1.]
#  [1.]
#  [1.]
#  [1.]
#  [1.]
#  [1.]
#  [1.]]
A = np.ones((n_of_data, 1))

# テキストから読みだしたx_1, x_2, の向き
#[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# を縦向きに変更してtmp_rowに一時的に格納する
# [[ 1.]
#  [ 2.]
#  [ 3.]
#  [ 4.]
#  [ 5.]
#  [ 6.]
#  [ 7.]
#  [ 8.]
#  [ 9.]
#  [10.]]
tmp_row = x_data.reshape(n_of_data, 1)
tmp_row_2=tmp_row**2 #xデータを２乗したリストがほしいから追記

# tmp_rowとAを横向きに結合してAを作る
# [[ 1.  1.]
#  [ 2.  1.]
#  [ 3.  1.]
#  [ 4.  1.]
#  [ 5.  1.]
#  [ 6.  1.]
#  [ 7.  1.]
#  [ 8.  1.]
#  [ 9.  1.]
#  [10.  1.]]
A = np.hstack((tmp_row_2,tmp_row, A)) #行の追加


# 最小二乗法の係数Xを計算する
y = y_data # y行列の作成
AT = A.T   # Aの転置行列
PATA = AT @ A  # Aの転置行列とAの積
inv_PATA = np.linalg.inv(PATA)  # Aの転置行列とAの積の逆行列 
P_inv_PATAAT = inv_PATA @ AT
X = P_inv_PATAAT @ y  # 多項式の係数
print(X)
# 求めた多項式の係数を使って多項式曲線あてはめしたデータを計算
y_fitted = X[0] * x_data**2 + X[1] * x_data +X[2] * x_data**0 #あてはめが異なるため変更

# プロットして結果を確認
fig = plt.figure()
ax = plt.subplot(111)
# 実験データを散布図でプロット
ax.scatter(x_data, y_data, marker="s", color="blue", s=25) 
# 当てはめのデータをプロット
ax.plot(x_data, y_fitted, color="red", lw="3")
ax.set_xlabel("Input [V]")
ax.set_ylabel("Output [V]")
plt.grid()
plt.show()