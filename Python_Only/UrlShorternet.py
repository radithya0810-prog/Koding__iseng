import pyshorteners

url_panjang = input("Masukkan URL panjang: ")
s = pyshorteners.Shortener()

url_pendek = s.tinyurl.short(url_panjang)
print("URL pendek:", url_pendek)