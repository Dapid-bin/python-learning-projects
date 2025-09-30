#======1.ARITMATIKA======
def aritmatika_1():
	def all_in():
		while True:
			def bulat():
				print("====> [BULAT]")
				print(f'{a} + {b} = {tambah}')
				print(f'{a} - {b} = {kurang}')
				print(f'{a} * {b} = {kali}')
				print(f'{a} // {b} = {bagi_bulat}')
				print(f'{a} % {b} = {modulus}')
				print(f'{a} ** {b} = {pangkat}')

			def desimal():
				print("====> [DESIMAL]")
				print(f'{float(a)} + {float(b)} = {float(tambah)}')
				print(f'{float(a)} - {float(b)} = {float(kurang)}')
				print(f'{float(a)} * {float(b)} = {float(kali)}')
				print(f'{float(a)} / {float(b)} = {float(bagi_desimal)}')
				print(f'{float(a)} % {float(b)} = {float(modulus)}')
				print(f'{float(a)} ** {float(b)} = {float(pangkat)}')

			def all():
				print("====> [BULAT]")
				print(f'{a} + {b} = {tambah}')
				print(f'{a} - {b} = {kurang}')
				print(f'{a} * {b} = {kali}')
				print(f'{a} // {b} = {bagi_bulat}')
				print(f'{a} % {b} = {modulus}')
				print(f'{a} ** {b} = {pangkat}')
	
				print("====> [DESIMAL]")
				print(f'{float(a)} + {float(b)} = {float(tambah)}')
				print(f'{float(a)} - {float(b)} = {float(kurang)}')
				print(f'{float(a)} * {float(b)} = {float(kali)}')
				print(f'{float(a)} / {float(b)} = {float(bagi_desimal)}')
				print(f'{float(a)} % {float(b)} = {float(modulus)}')
				print(f'{float(a)} ** {float(b)} = {float(pangkat)}')

			print("↓===👾 ALL IN FITUR 👾===↓")

			print("!! <( Warning Input Zero = 1 )> !!")
			a = int(input("Angka ke 1: ")) or 1
			b = int(input("Angka ke 2: ")) or 1

			tambah = a + b
			kurang = a - b
			kali = a * b
			bagi_desimal = a / b
			bagi_bulat = a // b
			modulus = a % b
			pangkat = a ** b
			
			print('👾 Opsi Hasil:')
			print('> Desimal')
			print('> Bulat')
			print('> Bulat And Desimal')
			option = input("Opsi: ").upper()
			
			bilangan = {
				"BULAT": bulat,
				"DESIMAL": desimal,
				"BULAT AND DESIMAL": all
			}

			if option in bilangan:
				print("==< VIEW >==")
				bilangan[option]()
			else:
				print(f"Opsi hasil ({option}) tidak ada")
			
			print("> EXIT")
			print("> NO")
			user = input("input: ").upper()
			
			match user:
				case "EXIT":
					print("Oke Bro", name, "✌")
					break

	def manual():
		while True:
			bilangan = []
			def main(bilangan, user):
				bilangan.append(input(user).upper())
	
			print('↓====👾 MANUAL FITUR 👾====↓')
	
			print("👾 Opsi Operator:")
			print('''> Tambah: +
> Kurang: -
> Kali: *
> Bagi: Bulat(//) Desimal(/)
> Modulus: %
> Pangkat: **''')
			c = input("Opsi you: ")

			print("!! <( Warning Input Zero = 1 )> !!")
			a = input("Angka ke-1: ") or 1
			b = input("Angka ke-2: ") or 1
	
			print("👾 Opsi Hasil:")
			print('> Desimal')
			print('> Bulat')
			main(bilangan, "Opsi you: ")
	
			match bilangan[0]:
				case "BULAT":
					print("==< VIEW >==")
					print(a, c, b, "=", int(eval(a + c + b)))
				case "DESIMAL":
					print("==< VIEW >==")
					print(float(a), c, float(b), "=", float(eval(a + c + b)))
				case _:
					print("👾 Problem input")
	
			print("> EXIT")
			print("> NO")
			main(bilangan, "Input: ")
	
			match bilangan[1]:
				case "EXIT":
					print("Oke Bro", name, "✌")
					break

#=====MAPING
	while True:
		print("↓===👾 ARITMATIKA 👾===↓")
		print("> Manual")
		print("> All in")
		print("> Exit")
		main = input("Pilih Menu: ").upper()
	
		menu = {
		"MANUAL": manual,
		"ALL IN": all_in
		}
	
		if main in menu:
			menu[main]()
		elif "EXIT" in main:
			print("Oke Bro", name, "✌")
			break
		else:
			print(f"Menu ({main}) Tidak ada")

#======2.PERBANDINGAN======
def perbandingan_2():
	pack = ['==', '!=', '>=', '<=', '>', '<']

	def manual():
		while True:
			print(f"Opsi perbandingan mana bro {name}")
			print('''> Sama dengan: ==
> Tidak sama dengan: !=
> Lebih besar atau sama: >=
> Lebih kecil atau sama: <=
> Lebih besar: >
> Lebih kecil: <

> Exit: Exit''')

			c = input("Pilih menu: ").upper()
			match c:
				case "EXIT":
					print("Oke Bro", name, "✌")
					break

			hasil = "ada" if c in pack else "no"

			match hasil:
				case "ada":
					a = input("Yang mau dibandingin: ")
					b = input("sama: ")
					hasil = eval(a + c + b)

					print("↓===Oke ini Hasilnya===↓")
					match str(hasil):
						case "True":
							print(a, c, b, "= Bener True 🤙")
						case "False":
							print(a, c, b, "= Salah False 👀")
				case _:
					print('Menu', c, 'tidak ada')

	def all_in():
		while True:	
			a = input("Yang mau dibandingin: ")
			b = input("sama: ")
			print("↓== Oke ini Hasilnya ==↓")

			sama_dengan = str(eval(a + pack[0] + b))

			match sama_dengan:
				case "True":
					print(a, pack[0], b, "= Bener True 🤙")
				case "False":
					print(a, pack[0], b, "= Salah False 👀")

			tidak_sama_dengan = str(eval(a + pack[1] + b))

			match tidak_sama_dengan:
				case "True":
					print(a, pack[1], b, "= Bener True 🤙")
				case "False":
					print(a, pack[1], b, "= Salah False 👀")

			besar_sama = str(eval(a + pack[2] + b))

			match besar_sama:
				case "True":
					print(a, pack[2], b, "= Bener True 🤙")
				case "False":
					print(a, pack[2], b, "= Salah False 👀")

			kecil_sama = str(eval(a + pack[3] + b))

			match kecil_sama:
				case "True":
					print(a, pack[3], b, "= Bener True 🤙")
				case "False":
					print(a, pack[3], b, "= Salah False 👀")

			besar = str(eval(a + pack[4] + b))

			match besar:
				case "True":
					print(a, pack[4], b, "= Bener True 🤙")
				case "False":
					print(a, pack[4], b, "= Salah False 👀")

			kecil = str(eval(a + pack[5] + b))

			match kecil:
				case "True":
					print(a, pack[5], b, "= Bener True 🤙")
				case "False":
					print(a, pack[5], b, "= Salah False 👀")

			c = input("-> Exit or -> NO: ").upper()
			match c:
				case "EXIT":
					print("Oke Bro", name, "✌")
					break

#=====MAP=====
	while True:
		print('\t↓==👾 Perbandingan 👾==↓')

		print(f'\tMau opsi mana bro {name}')
		print('\t> Manual')
		print('\t> All In')
		print('\t> Exit: Exit')
		menu = input("\tOpsi: ").upper()

		match menu:
			case "MANUAL":
				manual()
			case "ALL IN":
				all_in()
			case "EXIT":
				print("\tOke Bro", name, "✌")
				break
			case _:
				print(f"\tMenu ({menu}) tidak ada")

#=====3.KONVERSI FIAT======
def konversi_fiat_3():
	while True:
		print('1. USD TO IDR')
		print('2. IDR TO USD')
		print('3. Exit')

		USD_IDR = input("Konversi opsi: ").upper()

		match USD_IDR:
			case "USD TO IDR":
				nominal = int(input("Nominal USD: "))
				USD = nominal
				nominal *= 16000
				print("{} USD Senilai {} Rupiah".format(USD, nominal))

			case "IDR TO USD":
				nominal = int(input("Nominal Rp."))
				IDR = nominal
				nominal /= 16000
				print(f"Rp.{IDR} Senilai {nominal} USD Bro")

			case "EXIT":
				print("Oke Bro", name, "✌")
				break

			case _:
				print(f'Opsi Konversi ({USD_IDR}) Tidak Ada')

#======4.KONVERSI UMUR======
def konversi_umur_4():
	while True:
		umur = int(input("Umur you?: "))

		status = umur
		umur *= 365

		status_detect = status >= 20

		match str(status_detect):
			case "True":
				print(umur, "Hari Bro " + name + " Hidup 🧐👨👀")
			case "False":
				print(umur, "Hari Bro " + name + " Hidup 🧐 🧒 👀")

		stop = input("Exit -> Y | No Exit -> N: ").upper()
		match stop:
			case "Y":
				print("Oke Bro", name, "✌")
				break

#======5.BISA IKUT PEMILU?======
def pemilu_5():
	while True:
		print("↓== Syarat Bisa Pemilu ==↓")
		print("PUNYA KTP dan MIN UMUR 18 Tahun.")

		umur = int(input("Umur: "))
		punya_ktp = input("Punya Ktp? (punya/gak): ").upper()

		if (umur >= 18) and ("PUNYA" in punya_ktp):
			print("\tPreview: ✍️")
			print("\tBisa ✌")
		else:
			print("\tPreview: ✍️")
			print("\tTidak Bisa !!")

		match str(umur >= 18):
			case "False":
				print("\t❎ Dibawah Umur!!") 
				print("\tBisanya Kapan?", (umur * 365) - (18 * 365), "Hari Lagi Bro")
			case _:
				print("\t✅ Diatas 17 Tahun")
		
		match punya_ktp:
			case "PUNYA":
				print("\t✅ Punya KTP !!")
			case _:
				print("\t❎ Gak Punya KTP !!")

		stop = input("Exit -> Y | No Exit -> N: ").upper()
		match stop:
			case "Y":
				print("Oke Bro", name, "✌")
				break

#======6.BIODATA======
def biodata_6():
	def create():
		save = ["Kosong"]

		umur = int(input("Umur: "))
		tinggi = float(input("Tinggi: "))
		hobi = input("Hobi: ").capitalize()
	
		biodata = f'''NAMA: {nama} UMUR: {umur} Year TINGGI: {tinggi} Cm HOBI: {hobi}'''
	
		while True:
			print("=> Tampilkan")
			print("=> Exit")
			menu = input("Menu: ").upper()
	
			match menu:
				case "TAMPILKAN":
					print(biodata)
				case "EXIT":
					break
				case _:
					print(f"✍️ Problem input ({menu})")
					continue
	
	while True:
		check = "ya" if "ANONYMUS" in opsi else "no"

		match check:
			case "ya":
				print("Lanjut dengan nama anonimus? > Lanjut")
				print("Ganti nama asli? > ganti")
				user = input("Pilih: ").upper()
			case "no":
				user = 'LANJUT'

		match user:
			case "LANJUT":
				nama = name
			case "GANTI":
				nama = input("Name you: ").capitalize()
			case _:
				print(f"Problem input ({user})")
				continue

		print("==👾 BIODATA 👾==")
		print("=> Add Biodata")
		print("=> Exit")
		menu = input("Menu: ").upper()
	
		fitur = {
			"ADD BIODATA": create
		}
	
		if menu in fitur:
			fitur[menu]()
		elif "EXIT" in menu:
			break
		else:
			print(f"Menu ({menu}) tidak ada")

#======5.BISA IKUT PEMILU?======
def ganjil_genap_7():
	def ganjil():
		while True:
			a = int(input("Bilangan Ganjil: "))
				
			print(f"{a} Bener Bilangan Ganjil 📸")  if a % 2 == 1 else print(f"{a} Bukan Bilangan Ganjil 👀")
		
			print("=> Lanjut")
			print("=> Exit")
			user = input("Input you: ").upper()
		
			match user:
				case "LANJUT":
					print("Oke 🤟")
				case "EXIT":
					print("Oke Bro " + name + " ✌")
					break
				case _:
					print(f"Problem input ({user})")
					break

	def genap():
		while True:
			a = int(input("Bilangan Genap: "))
				
			print(f"{a} Bener Bilangan Genap 📸")  if a % 2 == 0 else print(f"{a} Bukan Bilangan Genap 👀")
	
			print("=> Lanjut")
			print("=> Exit")
			user = input("Input you: ").upper()
	
			match user:
				case "LANJUT":
					print("Oke 🤟")
				case "EXIT":
					print("Oke Bro " + name + " ✌")
					break
				case _:
					print(f"Problem input ({user})")
					break

	while True:
		print("==👾 Bilangan Ganjil & Genap 👾==")
		print("=> Bilangan Ganjil")
		print("=> Bilangan Genap")
		print("=> Exit")
		menu = input("Menu: ").upper()
		
		user = {
			"BILANGAN GANJIL": ganjil,
			"BILANGAN GENAP": genap
		}
		
		if menu in user:
			user[menu]()
		elif "EXIT" in menu:
			print("Oke Bro " + name + " ✌")
			break
		else:
			print(f"Menu ({menu}) tidak ada")

#======8.STATUS UMUR======
def status_8():
	def multiple_status():
		while True:
			print("Contoh (Umur ke-1 20) (Umur ke-2 30) = 20,30")
			umur = input("Masukan Dua Umur: ").split(",")
			usia, usia_dua = umur
			
			usia = {"Status ke-1": usia.strip(), "Status ke-2": usia_dua.strip()}
			
			status = {check: ("Dewasa" if (int(Age) >= 20) else "Anak - anak")
				for check, Age in usia.items()}
			print(status)
		
			print("=> Lanjut")
			print("=> Exit")
			user_input = input("Menu: ").upper()
		
			match user_input:
				case "EXIT":
					break
	
	def single_status():
		while True:
			umur = int(input("Masukan Umur: "))
			
			usia = {"Status": umur}
			
			status = {check: ("Dewasa" if (Age >= 20) else "Anak - anak")
				for check, Age in usia.items()}
			print(status)
	
			print("=> Lanjut")
			print("=> Exit")
			user_input = input("Menu: ").upper()
		
			match user_input:
				case "EXIT":
					break
	
	menu = {
		"dua status": multiple_status,
		"satu status": single_status
	}
	
	while True:
		print("==👾 Check Status 👾==")
		print("=> Satu Status")
		print("=> Dua Status")
		print("=> Exit")
		user = input("Menu: ").lower()
		
		if user in menu:
			menu[user]()
		elif "exit" in user:
			break
		else:
			print(f"Menu ({user}) Tidak Ada!!")

#======9.Kalkulator & perbandingan======
def kalkulator_dan_perbandingan():
	while True:
		print("\n==👾 Kalkulator & Perbandingan 👾==")

		print('↓ Operator ↓		↓ perbandingan ↓')
		print('''Tambah = +		Sama dengan = ==
Kurang = -		Tidak sama dengan = !=
Kali = *		Lebih besar = >
Bagi desimal = /	Lebih kecil = <
Bagi bulat = //		Besar atau sama = >=
Modulus = %		Kecil atau sama = <=
Pangkat = **''')
		
		angka_pertama = int(input("\nAngka ke-1: "))
		operasi = input("Operator: ")
		angka_kedua = int(input("Angka ke-2: "))

		while (operasi in "/" or operasi in "//") and (angka_kedua == 0):
			print("\t⚠️ Tidak bisa dibagi dengan nol 👀")
			angka_kedua = int(input("Angka ke-2: "))		

		match operasi:
			case "+":
				print(angka_pertama, operasi, angka_kedua, '=', angka_pertama + angka_kedua)
			
			case "-":
				print(angka_pertama, operasi, angka_kedua, '=', angka_pertama - angka_kedua)
		
			case "*":
				print(angka_pertama, operasi, angka_kedua, '=', angka_pertama * angka_kedua)
		
			case "/":
				print(angka_pertama, operasi, angka_kedua, '=', angka_pertama / angka_kedua)
		
			case "//":
				print(angka_pertama, operasi, angka_kedua, '=', angka_pertama // angka_kedua)
		
			case "%":
				print(angka_pertama, operasi, angka_kedua, '=', angka_pertama % angka_kedua)
		
			case "**":
				print(angka_pertama, operasi, angka_kedua, '=', angka_pertama ** angka_kedua)

			case _:
				global op
				op = True

		if operasi == "==":
			print(angka_pertama, operasi, angka_kedua, '=', angka_pertama == angka_kedua)

		elif operasi == "!=":
			print(angka_pertama, operasi, angka_kedua, '=', angka_pertama != angka_kedua)

		elif operasi == ">":
			print(angka_pertama, operasi, angka_kedua, '=', angka_pertama > angka_kedua)

		elif operasi == "<":
			print(angka_pertama, operasi, angka_kedua, '=', angka_pertama < angka_kedua)

		elif operasi == ">=":
			print(angka_pertama, operasi, angka_kedua, '=', angka_pertama >= angka_kedua)

		elif operasi == "<=":
			print(angka_pertama, operasi, angka_kedua, '=', angka_pertama <= angka_kedua)

		else:
			global pb
			pb = True


		print("\n\t🌀KGC🌀QUANT") if pb or op else print("\n\tOperator&Perbandingan tadak ada !!")

		print('\tLanjut\n\tExit')
		user = input('Input: ').lower()
	
		match user:
			case 'exit':
				break

#=====PILIHAN FITUR (USER)
while True:
	print("↓= WELCOME =↓")
	print("=> Nama asli")
	print("=> Anonymus 🎭")
	opsi = input("Opsi you: ").lower()
	
	match opsi:
		case "nama asli":
			name = input('Name?: ').capitalize()
			break
		case "anonymus":
			name = 'KGC_Anonymus_user'
			break
		case _:
			print(f"Problem input ({opsi})")
			continue

print(f'\t👾 [ 🌀KGC🌀QUANT ] 👾')

while True:	
	print('|\t==KGC SINGLE SHOOT TOLS=|')

	print('|\tFitur Options:		|')
	print('''------------------------------------------------
|\t1. ARITMATIKA					|
|\t2. PERBANDINGAN					|
|\t3. KONVERSI FIAT					|
|\t4. KONVERSI UMUR					|
|\t5. BISA IKUT PEMILU					|
|\t6. BIODATA					|
|\t7. GANJIL GENAP					|
|\t8. STATUS UMUR					|
|\t9. KALKULATOR & PERBANDINGAN					|
|\t>. EXIT					|
-----------------------------------------------''')

	menu = {
	    "ARITMATIKA": aritmatika_1,
	    "PERBANDINGAN": perbandingan_2,
	    "KONVERSI FIAT": konversi_fiat_3,
	    "KONVERSI UMUR": konversi_umur_4,
	    "BISA IKUT PEMILU": pemilu_5,
	    "BIODATA": biodata_6,
	    "GANJIL GENAP": ganjil_genap_7,
	    "STATUS UMUR": status_8,
	    'KALKULATOR & PERBANDINGAN': kalkulator_dan_perbandingan
	}
	
	choice = input("👾 Pilih menu: ").upper()
	if choice in menu:
		menu[choice]()
	elif 'EXIT' in choice:
		print('Bye', name, '✌')
		print("[ PROGRAM SELSESAI ]")
		break
	else:
		print('\t[ Fitur tidak ada bro ]')