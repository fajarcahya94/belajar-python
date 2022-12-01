class people:
    name = []
    laguage = []


def inInggris(name):
    print("=====Inggris=====")
    print("Hallo!", name)
    print("Good Morning", name)
    print("Good Afternoon", name)
    print("Good Evening", name)
    print()


def inIndonesia(name):
    print("=====Indonesia=====")
    print("Halo!", name)
    print("Selamat Pagi", name)
    print("Selamat Siang", name)
    print("Selamat Malam", name)
    print()


def inGerman(name):
    print("=====German=====")
    print("Hallo!", name)
    print("Guten Morgen", name)
    print("Guten Tag", name)
    print("Guten Abend", name)
    print()


def getName(leng):
    print("=====Nama=====")
    getInputName = input(str("Nama Anda : "))
    people.name.append(getInputName)
    getLeng = input(str("Bahasa Anda : "))
    people.laguage.append(getLeng)
    print()

    if getLeng == "indonesia":
        hasil = inIndonesia(''.join(map(str, people.name)))
        print(hasil)
    elif getLeng == "german":
        hasil = inGerman(''.join(map(str, people.name)))
        print(hasil)
    elif getLeng == "inggris":
        hasil = inInggris(''.join(map(str, people.name)))
        print(hasil)
    else:
        print("Bahasa tidak tersedia!")
    return tampil(leng)


def tampil(leng):
    getInput = input("Apakah ingin mengulang? y/n: ")
    print()
    if getInput == "y":
        getName(people.name)
    else:
        print("Terimakasih")
        exit()
    return leng


tampil(getName(people.name))
