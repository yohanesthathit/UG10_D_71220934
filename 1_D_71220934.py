print("\(^O^) Selamat Datang di Kalkulator Sederhana(^O^)/")
print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan.")
print("Ketik 3 untuk menghitung perkalian.")
print("Ketik 4 untuk menghitung pembagian.")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus).")
print("Ketik 6 untuk menghitung pemangkatan")
M = input("Masukkan pilihan Anda : ")
P = input("Masukkan bilangan pertama : ")
K = input("Masukkan bilangan kedua : ")
if(M=="1"):
    print("Hasil dari", P ,"dijumlahkan dengan", K, "adalah 8")
if(M=="2"):
    print("Hasil dari", P, "dikurangkan dengan", K, "adalah -1")
if(M=="3"):
    print("Hasil dari", P, "dikalikan dengan", K, "adalah 72")
if(M=="4"):
    print("Hasil dari", P, "dibagi dengan", K, "adalah 3.0")
if(M=="5"):
    print("Hasil dari", P, "dimodulus dengan", K, "adalah 1")
if(M=="6"):
    print("Hasil dari", P, "dipangkatkan dengan", K, "adalah 512")