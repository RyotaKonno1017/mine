#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import select
host = '10.0.3.7'
port = 3400

if __name__ == '__main__':
    backlog = 10
    bufsize = 4096

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockList = set([serverSock])
    addrList = {serverSock: host}
    
    try:
        msg_list=[]    #ここに全メッセージを保存する
        serverSock.bind((host, port))
        serverSock.listen(backlog)
 
        while True:
            readReadySock, writeReadySock, exceptionReadySock = \
                    select.select(sockList, [], [])

            for sock in readReadySock:
                if sock is serverSock:       #そのソケットがサーバー自身の場合
                    connection, address = serverSock.accept()
                    sockList.add(connection)
                    addrList[connection] = address

                else:   #そのソケットがクライアントの場合
  
                    msg = sock.recv(bufsize)  #3.サーバーで受信
                    msg_list.append(msg)      #受信メッセージをリストに追加
                    if len(msg) == 0:         #メッセージの文字数が0なら
                        sock.close()          #サーバー側でソケットを閉じて
                        sockList.remove(sock) #リストから削除
                    else:   #メッセージがある場合
                        print("[{}]".format(addrList[connection])), #誰が通信した分かるやつ[●●.●.●.●].●●●●●みたいな                     
                        msg = msg.decode("utf-8") #サーバー側も見にくかったので受信したbyte型からstr型に変換
                        print(msg)
                        msg=b"\n".join(msg_list)
                        sock.send(msg) #4.サーバーが返信
    finally:
        for sock in sockList:
            sock.close()
