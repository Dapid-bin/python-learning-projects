print("==👾 Kalkulator & Perbandingan 👾==")
print('↓ Operator ↓		↓ perbandingan ↓')
print('''Tambah = +		Sama dengan = ==
Kurang = -		Tidak sama dengan = !=
Kali = *		Lebih besar = >
Bagi desimal = /	Lebih kecil = <
Bagi bulat = //		Besar atau sama = >=
Modulus = %		Kecil atau sama = <=
Pangkat = **''')

angka_pertama = int(input("Angka ke-1: "))

operasi = input("Operator: ").upper()

angka_kedua = int(input("Angka ke-2: "))

match operasi:
	case "+":
		print(angka_pertama, operasi, angka_kedua, '=', angka_pertama + angka_kedua)
	
	case "-":
		print(angka_pertama, operasi, angka_kedua, '=', angka_pertama - angka_kedua)

	case "*":
		print(angka_pertama, operasi, angka_kedua, '=', angka_pertama * angka_kedua)

	case "/":
		print(angka_pertama, operasi, angka_kedua, '=', angka_pertama or 1 / angka_kedua or 1)

	case "//":
		print(angka_pertama, operasi, angka_kedua, '=', angka_pertama or 1 // angka_kedua or 1)

	case "%":
		print(angka_pertama, operasi, angka_kedua, '=', angka_pertama % angka_kedua)

	case "**":
		print(angka_pertama, operasi, angka_kedua, '=', angka_pertama ** angka_kedua)

	case _:
		print("Operator ({}) tidak ada".format(operasi))


perbandingan = {
	'==': '{} {} {} = {}'.format(angka_pertama, operasi, angka_kedua, eval(str(angka_pertama) + operasi + str(angka_kedua))),
	'!=': 'Tidak sama dengan',
	'>': 'Lebih besar',
	'<': 'Lebih kecil',
	'>=': 'Lebih besar atau sama',
	'<=': 'Lebih besar atau sama'
}


if operasi in perbandingan:
	print("Ada di perbandingan")
	print(perbandingan.get('=='))
else:
	pass
