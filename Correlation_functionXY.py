import numpy as np
import matplotlib.pyplot as plt

# データの読み込み
filenameX = "CorrelationDataEx2X.txt"
tX, amplitudeX = np.loadtxt(filenameX, unpack=True) # 2次元配列のデータ
n_of_dataX = len(tX) # データの個数

# 確認のため計測データのプロット
fig= plt.figure()
ax1 = fig.add_subplot(3, 1, 1)  # (3行, 1列, の1番目)のグラフ描画領域を作りax1でアクセスする
ax1.plot(tX, amplitudeX, lw=2)  # plotで計測データを描画
ax1.set_xlabel("time[s]")  # 横軸のラベル設定
ax1.set_ylabel("amplitude[V]")  # 縦軸のラベル設定
plt.grid()  # グリッド(補助目盛りの点線)表示
#plt.show()  # グラフ描画 (2段組みでプロットするときはここをコメントアウト)

# データの読み込み
filenameY = "CorrelationDataEx2Y.txt"
tY, amplitudeY = np.loadtxt(filenameY, unpack=True)  # 2次元配列のデータ
n_of_dataY = len(tY) # データの個数


box = fig.add_subplot(3, 1, 2)  # (3行, 1列, の2番目)のグラフ描画領域を作りboxでアクセスする
box.plot(tY, amplitudeY, lw=2)  # plotで計測データを描画
box.set_xlabel("time[s]")  # 横軸のラベル設定
box.set_ylabel("amplitude[V]")  # 縦軸のラベル設定
plt.grid()  # グリッド(補助目盛りの点線)表示
#plt.show()  # グラフ描画 (2段組みでプロットするときはここをコメントアウト)


# A. 自己相関関数の計算(自分で実装)
""" A-1. 振幅の平均値を求めて, 振幅の計測値から引いたデータを用意する"""
average_amplitudeX = np.mean(amplitudeX)  # 振幅の平均値の算出(np関数の使用)
amplitudeX=amplitudeX-average_amplitudeX  # 各振幅データから振幅平均値の減算


average_amplitudeY = np.mean(amplitudeY)  # 振幅の平均値の算出(np関数の使用)
amplitudeY=amplitudeY-average_amplitudeY  # 各振幅データから振幅平均値の減算

""" A-2. 自己相関関数の計算"""
RR = np.zeros(n_of_dataX)   # 遅れkに対する自己相関RRを測定点のデータ数分ゼロで初期化

for k in range(n_of_dataX):   # 遅れkに対する繰り返しループ
    for n in range(n_of_dataX-k):   # データnに対する繰り返しループ（積和の計算）
        RR[k]+= amplitudeX[n]*amplitudeY[n+k]      # サンプル nとサンプル n+k（遅れk）の積
        
    RR[k]=RR[k]/(n_of_dataX-k)  # 先の計算で求めた積和をデータ点数で除算（平均） → 遅れkに対する自己相関係数


# B. グラフの下側の領域に自己相関関数をプロット(自分で実装)
""" B-1. グラフの下側に自己相関の計算結果をプロットする"""
compose = fig.add_subplot(3, 1, 3) # フィギュアを3個描画する枠（3行1列）を設定し，3個（3行1列目）目を描画する
compose.plot(range(n_of_dataX),RR, lw=2)      # 自己相関関数の描画(実線)
compose.set_xlabel("lag")      # 図の横軸のタイトル
compose.set_ylabel("autocorrelation")      # 図の縦軸のタイトル
plt.grid()      # 描画したフィギュアにグリッドを書き込む
fig.tight_layout()    # 2段組みのときに各グラフ間の余白を調整
plt.show()      # 上で指定したフィギュアの描画
