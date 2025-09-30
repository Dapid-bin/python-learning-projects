#Basic 
pw = ''
while pw != "kgc123":
	pw = input("\tMasukan Pasword: ")

	if pw != "kgc123":
		print("\tPasword salah❕ coba lagi.")
print("\n\tLogin berhasil ✅")


print('\n\t↓__________Learning__________↓')
pasword = ''

while pasword != "rahasia123":
	pasword = input("\nPasword: ").lower()

	print("\n\t🌀 Pasword benar!! 🌀") if pasword == "rahasia123" else print("\tPasword salah❕")


counter = 20 # ⚠️
while True:
	print("\n\tLoop ke-{}".format(counter))
	counter -= 1

	if counter <= 0:
		break
	elif counter == 5:
		print('\n\tLoop ke 5 2x √ 👀')
	elif counter == 10:
		print('\n\tLoop ke 10 2x √ 👀')

for i in range(100000000):
	if i == 15:
		break
	print('Stop di 14 👉', i)

print("\n[ Program 🌀 Selesai ]")