
import socket
import time


host = "localhost"
port = 7777
internet_soketi = socket.socket()
internet_soketi.connect((host, port))


print("Bağlantı sağlandı... ★ Welcome Explorer :){}:{}".format(host, port))
print("""░""")


mesaj = input("---::")
print("User1 bekleniyor...")

while mesaj != "cikis":
    internet_soketi.send(mesaj.encode())
    gelen_veri = internet_soketi.recv(1024).decode()

    print("Server: "+gelen_veri)

    mesaj = input("---::")
    print("User1 Bekleniyor...")
internet_soketi.close()