#1 masala:

class kitob:
    def __init__(self, nomi, muallif, narxi, nashriyot):
        self.nomi = nomi
        self.muallif = muallif
        self.narxi = narxi
        self.nashriyot = nashriyot

    def chiqarish(self):
        print(f"Nomi: {self.nomi}, Muallif: {self.muallif}, Narx: {self.narxi}, Nashriyot: {self.nashriyot}")

k1 = kitob("Jinoyat va jazo", "Dostoyevskiy", 100, "Asaxiy")
k2 = kitob("1984", "Jorj Oruell", 120, "Hilol")
k3 = kitob("Molxona", "Jorj Oruell", 90, "Ziyo")
k4 = kitob("Ikki eshik orasi", "Otkir Hoshimov", 110, "Asaxiy")
k5 = kitob("Urush va tinchlik", "Lev Tolstoy", 80, "Falaqnashr")

kitoblar = [k1, k2, k3, k4, k5]

for i in kitoblar:
    if 'A' <= i.nashriyot[0].upper() <= 'H':
        i.chiqarish()


# 2 masala:

class komputer:
    def __init__(self, nomi, ram, narx, protsessor):
        self.nomi = nomi
        self.ram = ram
        self.narx = narx
        self.protsessor = protsessor
    def chiqarish(self):
        print("Nomi: ", self.nomi)
        print(f"Ram: {self.ram} GB")
        print(f"Narx: {self.narx}$")
        print("Protsessor: ", self.protsessor)


print("Qaysi malumot bilan ishlashni tanlaysiz")
print("1 - tayor malumot bilan ishlash")
print("2 - input orqali kiritish")
a = input("Tanlang (1) yoki (2) ")
print("\n\n")

kompyuterlar = []

if a  == "1":
    pc1 = komputer("HP", 8, 500, "Intel i5")
    pc2 = komputer("Dell", 4, 450, "Intel i3")
    pc3 = komputer("Asus", 12, 700, "Intel i7")
    pc4= komputer("Lenovo", 16, 800, "Ryzen 5")

    kompyuterlar = [pc1, pc2, pc3, pc4]
elif a == "2":
    for i in range(4):
        print(f"{i+1} - kompyuter: ")
        nomi = input("nomi: ")
        ram = int(input("Ram: "))
        narx = int(input("Narx($): "))
        protsesor = input("protsessor: ")

        pc = komputer(nomi, ram, narx, protsesor)
        kompyuterlar.append(pc)
else: print("Bunday tanlov yoq")

print("natija:\n")
for i in kompyuterlar:
    if 4 < i.ram < 16:
        i.chiqarish()

# 3 masala: 


class User:
    def __init__(self, ism, username, email):
        self.name = ism
        self.username = username
        self.email = email
    def get_info(self):
        return f"Foydalanuvchi: {self.name}, Username: {self.username}, Email: {self.email}"


user1 = User("Ali Valiyev", "ali01", "ali@mail.com")
user2 = User("Sardor Karimov", "sardor02", "sardor@mail.com")
user3 = User("Jasur Tursunov", "jasur03", "jasur@mail.com")
user4 = User("Bekzod Rahimov", "bekzod04", "bekzod@mail.com")
user5 = User("Dilshod Xasanov", "dilshod05", "dilshod@mail.com")

print(user1.get_info())
print(user2.get_info())
print(user3.get_info())
print(user4.get_info())
print(user5.get_info())