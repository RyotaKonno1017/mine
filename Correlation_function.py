import numpy as np
import matplotlib.pyplot as plt

# データの読み込み
filename = "CorrelationDataEx1.txt"
t, amplitude = np.loadtxt(filename, unpack=True)  # 2次元配列のデータ
n_of_data = len(t)  # データの個数

# 確認のため計測データのプロット
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)  # (2行, 1列, の1番目)のグラフ描画領域を作りax1でアクセスする
ax1.plot(t, amplitude, lw=2)  # plotで計測データを描画
ax1.set_xlabel("time[s]")  # 横軸のラベル設定
ax1.set_ylabel("amplitude[V]")  # 縦軸のラベル設定
plt.grid()  # グリッド(補助目盛りの点線)表示
#plt.show()  # グラフ描画 (2段組みでプロットするときはここをコメントアウト)

# A. 自己相関関数の計算(自分で実装)
""" A-1. 振幅の平均値を求めて, 振幅の計測値から引いたデータを用意する"""
average_amplitude = np.mean(amplitude)  # 振幅の平均値の算出(np関数の使用)
amplitude -= average_amplitude  # 各振幅データから振幅平均値の減算

""" A-2. 自己相関関数の計算"""
RR = np.zeros(n_of_data)  # 遅れkに対する自己相関RRを測定点のデータ数分ゼロで初期化

for k in range(n_of_data):  # 遅れkに対する繰り返しループ
    for n in range(n_of_data - k):  # データnに対する繰り返しループ（積和の計算）
        RR[k] += amplitude[n] * amplitude[n + k]  # サンプル nとサンプル n+k（遅れk）の積

    RR[k] /= (n_of_data - k)  # 先の計算で求めた積和をデータ点数で除算（平均） → 遅れkに対する自己相関係数

# B. グラフの下側の領域に自己相関関数をプロット(自分で実装)
""" B-1. グラフの下側に自己相関の計算結果をプロットする"""
box = fig.add_subplot(2, 1, 2)  # フィギュアを2個描画する枠（2行1列）を設定し，2個（2行1列目）目を描画する
box.plot(range(n_of_data), RR, lw=2)  # 自己相関関数の描画(実線)
box.set_xlabel("lag")  # 図の横軸のタイトル
box.set_ylabel("autocorrelation")  # 図の縦軸のタイトル
plt.grid()  # 描画したフィギュアにグリッドを書き込む
fig.tight_layout()  # 2段組みのときに各グラフ間の余白を調整
plt.show()  # 上で指定したフィギュアの描画