import socket
host = '10.0.3.7'    # 接続先サーバの[Alpine Linux3]のIPアドレスを指定
port = 3400           # 接続先サーバのポート番号を指定
bufsize = 4096

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientSock.connect((host, port))

while True:  
    msg = input() # 1.キーボードからメッセージ入力
    if msg == '': # 入力が空の場合はプログラム終了へむけてbreak
        break
    else:  # 入力が空でない場合
        txMsg = msg.encode("utf-8")     # 文字列型はそのまま送れないのでbyte型に変換
        clientSock.send(txMsg)          #サーバーに送信
        rxMsg = clientSock.recv(bufsize)       # 返事を受信
        rxMsg = rxMsg.decode("utf-8")          # byte型で受信した文字列をstr型に変換
        print(rxMsg)                           # 返事を表示

clientSock.close()                     # ソケット破棄
