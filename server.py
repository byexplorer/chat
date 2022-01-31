from os import access
import socket
import time


host = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.bind((host, port))

internet_soketi.listen(1)

baglanti, adres = internet_soketi.accept()
print(str(adres)+"bağlantı sağlandı...  ★ Welcome Explorer :) ")
time.sleep(1)
print("""░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█""")


while True:	
	while True:
		try: 
			gelen_veri = str(baglanti.recv(1024).decode())
			print(" Client şunu yolladı :"+gelen_veri)
			break
		except ConnectionResetError:
			time.sleep(2)
		baglanti, adres = internet_soketi.accept()
		print(str(adres)+"Bağlantı Sağlandı.")
		
	if gelen_veri == "cikis":
		break
	else:
		mesaj = input("---::")
		print("clint bekleniyor...")
		baglanti.send(mesaj.encode())

baglanti.close()