print("\t| 🌀 KGC 🌀 QUANT |")
print("_" * 47)

# Basic
nyawa = 10 # 20 nyawa
while nyawa != 0:
	'''
	20 != 0 = True kondisi
	berhenti loping jika False atau nyawa 0
	'''
	print(f"\tNyawa {nyawa}")
	nyawa -= 1
	'''
	nyawa - 1 setiap looping 10 - 1
	break otomatis karena kondisi False 0
	0 != 0 False
	'''


print("pasword: KGC	Kasempatan login 10x")
pasword = input("🌀\t| Pasword: ").upper()

kesempatan = 1
while pasword != "KGC" and kesempatan != 10:
	print("🌀\t| Kesempatan Login:", kesempatan)
	pasword = input("🌀\t| Pasword: ").upper()
	
	kesempatan += 1

print('-' * 20, 'NOTE', '-' * 20)

print(f"\tLogin berhasil {kesempatan - 1}x salah!! 🌀") if pasword == "KGC" else print('''\tKesempatan Login Sudah Habis
	Login Gagal!! 🌀''')


print('_' * 15, '🏦', '_' * 15)
print("↓ DEPOSIT IN 🌀 KGC 🌀 BANK ↓")
print('''Limit Deposit = 100k IDR
Min Deposit = 20k IDR''')
print('_' * 30)

deposit = int(input("Deposit Rp."))

while deposit > 100000 or deposit < 20000:
	print("\t| Deposit Log Rp." + str(deposit), "Gagal ❌ |")
	deposit = int(input("Deposit Rp."))

print("\tBUKTI DEPOSIT")
print("\tDeposit sukses Rp.{} !! 🌀".format(deposit))


print("Exit or No")
user_input = input("menu: ").capitalize()

while "Exit" not in user_input:
	print("Apa yang mau kamu lakukan: ")
	user_input = input("Text: ").capitalize()

	print("\t↓ ⛓️ USER LOG ⛓️ ↓")
	print(f"\t 🌀 [ {user_input} ] 🌀")
	print("⚠️ EXIT OR NO ⚠️")

	print("🌀 Oke 🌀") if 'Exit' in user_input else print("{} 👀".format(user_input))

print("\t[ 🌀 PROGRAM SELESAI 🌀 ]")