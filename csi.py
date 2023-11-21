#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用しているダミーデータについて
今回使用しているデータはUserLocalの個人情報テストデータジェネレーターを利用しています.

https://testdata.userlocal.jp/

初期状態のプログラムは下記の2ステップです. これを改造してください

 1. csvからデータを読み込んで, csv_dataに追加
 2. csv_dataの内容をcsvファイルに書き出し
"""
import csv
import matplotlib.pyplot as plt

# データの入れ物
csv_data = []

# 読み出し用csvファイルを開く
with open("./csi.csv", "r") as f:
    # csvとして読み出せるようにする
    csv_reader = csv.reader(f, delimiter=",")  # delimiterは区切り文字の指定
    # ファイルから1行ずつcsv_reader経由で読み出してデータを追加する
    for line in csv_reader:
        """
        ここに読み出し処理を書く
        lineには,で区切ったデータがリストとして入っている
        """
        csv_data.append(line[25])


ch_data = [[] for i in range(64)]
for data in csv_data[1:]: # 見出し行はスキップ
    data = data.replace("[", "").replace("]", "").rstrip().split()
    for i in range(0, len(data), 2):
        x = float(data[i])  # I成分
        y = float(data[i+1])  # Q成分
        amplitude = (x**2 + y**2)**0.5
        ch_data[round(i/2)].append(amplitude)


fig = plt.figure()
plt.clf()
ax = plt.subplot(1,1,1)
for i, item in enumerate(ch_data):
    x = [i for i in range(len(item))]  # 横軸用の適当な数字(プロットの都合上のダミー)
    ax.plot(x, item, lw=1, marker=".", label="ch."+str(i+1))
ax.grid()
ax.set_xlabel("time index")
ax.set_ylabel("amplitude")
plt.legend(fontsize="xx-small")
plt.grid()
plt.savefig("amplitude.pdf")

