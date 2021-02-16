
def timeConverter(seconds):
    try: 
        # jumlah_detik = int(input("Masukkan detik :"))
        jumlah_detik = int(seconds)

        if (jumlah_detik > 359999):
            print("Invalid Input, Jumlah Detik diatas batas (Batas Maks 359999)")
        elif (jumlah_detik < 0):
            print("Invalid Input, Jumlah Detik dibawah batas (Tidak boleh input angka negatif)")
        else:
            jam = jumlah_detik // 3600
            menit = (jumlah_detik % 3600) // 60
            detik = ((jumlah_detik % 3600) % 60)
            jam_str = str("{:0>2d}".format(jam))
            menit_str = str("{:0>2d}".format(menit))
            detik_str = str("{:0>2d}".format(detik))
            print("Konversi :", jam_str ,":", menit_str,":", detik_str)
            # print("{:0>2d}".format(jam), ":", "{:0>2d}".format(menit), ":", "{:0>2d}".format(detik))
    except:
        print("Invalid Input, Jumlah detik yang anda masukkan salah (Hanya boleh memasukkan INTEGER)")

jumlah_detik_input = input("Masukkan detik :")
timeConverter(jumlah_detik_input)