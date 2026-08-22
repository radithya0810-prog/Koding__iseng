while True:
    print()

    nama = input("Masukkan nama Anda: ")

    tanggal_lahir = input("Masukkan tanggal lahir Anda (DDMMYYYY): ")

    while not tanggal_lahir.isdigit() or len(tanggal_lahir) != 8:
        print("Format tanggal lahir tidak valid. Harap masukkan dalam format DDMMYYYY (contoh: 01012000).")
        tanggal_lahir = input("Masukkan tanggal lahir Anda (DDMMYYYY): ")
    tanggal_lahir = tanggal_lahir[:2] + "/" + tanggal_lahir[2:4] + "/" + tanggal_lahir[4:]

    alamat = input("Masukkan alamat Anda: ")
    
    gender = input("Masukkan jenis kelamin Anda (L/P): ")
    while gender not in ['L', 'P']:
        print("Jenis kelamin tidak valid. Harap masukkan 'L' untuk laki-laki atau 'P' untuk perempuan.")
        gender = input("Masukkan jenis kelamin Anda (L/P): ")
    
    print("\nData yang Anda masukkan:")
    print("Nama:", nama)
    print("Tanggal Lahir:", tanggal_lahir)
    print("Alamat:", alamat)
    print("Jenis Kelamin:", gender)