import socket

HOST = '127.0.0.1'  
PORT = 12345        

# ソケット作成（AF_INET = IPv4, SOCK_STREAM = TCP）
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))       
    s.listen()                 
    print("接続待ち中...")

    conn, addr = s.accept()   
    with conn:
        print(f"接続されました: {addr}")
        while True:
            data = conn.recv(1024)  
            if not data:
                break
            print("受信:", data.decode())
            conn.sendall("受け取りました")  
