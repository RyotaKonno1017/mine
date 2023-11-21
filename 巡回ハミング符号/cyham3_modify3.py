# 「符号理論」第8回(11/17) (7,4)巡回ハミング符号のプログラム
##　【プログラミング課題】
# (1) 教科書p.138 演習問題6.1をこのプログラムで確認せよ。
# (2) 次数をm=4,5としたときの巡回ハミング符号に拡張して、動作確認した結果をまとめる。
import random
m = 3 # 原始多項式の次数 m = 3
gx = 0b1011 # m=3の原始多項式 G(x) = x^3 + x + 1 の2進表現
n = (1<<m)-1 # 位数　n = 2^m - 1 
alpha = [1] # α^0 = １の定義したガロア体リストの作成
loga = [-n] # α^i の指数部分iを格納　log[alpha^i] = i
for i in range(0,n):
    loga.append(0)
def gfield(): # 有限体GF(2^n)の生成 1, α, α^2, .... , α^{n-2}
    a = 1 # loga[] 有限体α^i の指数部分iを格納する　log(α^i) = i
    for i in range(1,n):
        a <<= 1
        if a > n: a ^= gx
        alpha.append(a)
        for i in range(1,n):
            loga[alpha[i]] = i
            return
def rol(x,l,n): # nビットデータxのlビット左巡回シフト
    return ( ( (x << l) | (x>>(n-l)) ) & ((1<<n)-1) )
def polymod(z,n,y,m): #多項式の剰余計算【多項式z(x)の次数n, 多項式y(x)の次数m】
    for i in range(n-m+1):
        z = z ^ ( y << (n-m-i)) if ( z >> (n-i) ) else z
        return z
def encoding(a): # 巡回符号の符号化
    return ((a << m)|polymod(a<<m,n-1,gx,m)) # 情報記号aにx^mを掛けてg(x)で割った余りを付加【組織符号化】
def hamming_decoding(v): #　誤り訂正ハミング符号の復号
    s = 0 # s: シンドローム
    for i in range(n):
        if (( v >> i ) & 1) : s ^= alpha[i]
        print("s=",loga[s],format(s,'03b')) # シンドローム表示s=α^iの指数部を出力(sの2進表記も併記)
        if s : v ^= ( 1 << loga[s] ) # シンドロームが0でなければs=α^iとなる位置iを反転
        return v
gfield() # ガロア体の生成
a = random.randint(0,(1<<(n-m))-1) #(n-m)ビットの情報記号aをランダムに生成（0～2^{n-m}-1）
w = encoding(a) # (n-m)ビット情報記号列aを巡回符号に符号化
print(format(w,'07b')) # mビットの検査記号が加わり、nビットの符号語となる
v = w ^ ( 1 << 4 ) # 通信路の処理（符号語wの4ビット目に誤り発生）
print(format(v,'07b')) #　誤りが発生していることを確認する
v = hamming_decoding(v) # 誤りを含む受信語に復号処理を実行
print(format(v,'07b')) # 復号処理により単一誤りが訂正されていることを確認