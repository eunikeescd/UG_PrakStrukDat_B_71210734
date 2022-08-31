while True:
    print()
    print('Masukkan pilihan yang ada untuk menggunakan kalkulator\n 1.Penjumlahan\n 2.Pengurangan\n 3.Perkalian\n 4.Pembagian\n 5.Q untuk mengakhiri Program')
    Pilihan = (input("Masukkan pilihan anda: "))

    if Pilihan == '1':
        a1 = int(input('masukkan angka1: '))
        a2 = int(input('masukkan angka2: '))
        print("hasilnya",a1+a2)
    elif Pilihan == '2':
        a1 = int(input('masukkan angka1: '))
        a2 = int(input('masukkan angka2: '))
        print("hasilnya",a1-a2)
    elif Pilihan == '3':
        a1 = int(input('masukkan angka1: '))
        a2 = int(input('masukkan angka2: '))
        print("hasilnya",a1*a2)
    elif Pilihan == '4':
        a1 = int(input('masukkan angka1: '))
        a2 = int(input('masukkan angka2: '))
        print("hasilnya",a1/a2)
    elif Pilihan == 'Q':
        print("Program akan dihentikan")
        break
    else :
        print("Pilihan anda tidak tersedia di menu kalkulator ini")

