import random


item_gacha = {
    "common": ["Wooden Armor", "Wooden shield", "Wooden Sword"],
    "rare": ["Iron Armor", "Iron Shield", "Iron Sword"],
    "epic": ["Diamond Armor", "Diamond Shield", "Diamond Sword", "Health Potion"],
    "legendary": ["Excalibur", "Dragon Slayer", "Phoenix Feather", "Ice and Fire Staff"],
    "Impossible": ["Infinity Gauntlet", "Eternal Blade", "Time Turner", "Reality Stone"]
}

chance = {
    "common": 50,
    "rare": 30,
    "epic": 10,
    "legendary": 9,
    "Impossible": 1
}

while True:
    
 print("\n=== Gacha Game ===")
 print("1. Gacha 1x")
 print("2. Gacha 10x")
 print("3. keluar")
 
 pilihan = input("Masukkan pilihan Anda (1/2/3): ")
 
 if pilihan == "1":
     jumlah = 1
 elif pilihan == "2":
     jumlah = 10
 elif pilihan == "3":
     break
 else:
     print("Pilihan gak valid")
     continue
 
 for i in range(jumlah):
    rarity = random.choices(list(chance.keys()), weights=list(chance.values()))[0]

    item = random.choice(item_gacha[rarity])
    
    if rarity == "common":
        print("Selamat anda mendapatkan item:", item)
    elif rarity == "rare":
        print("Selamat anda mendapatkan item:", item)
    elif rarity == "epic":
        print("\n[EPIC!!!]")
        print("Selamat anda mendapatkan item:", item)
    elif rarity == "legendary":
        print("\n ✨ LEGENDARY ✨")
        print("Selamat anda mendapatkan item:", item)
    elif rarity == "Impossible":
        print("\n 🌌🌌 IMPOSSIBLE 🌌🌌")
        print("Selamat anda mendapatkan item:", item)
    
 lanjut = input("Mau lanjut lagi? (Y/N): ")

 if lanjut == "N":
    break