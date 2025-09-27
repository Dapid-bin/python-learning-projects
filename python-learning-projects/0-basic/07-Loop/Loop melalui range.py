#Loop melalui range basic
print("Default in range(5)")

for basic in range(5):# range(5) = 5 × d ulang
	print("Perulangan Ke-" + str(basic))# Output str manipulation str() <- conversi int to str

'''
Perulangan 5 kali yang diawali dari 0:
	0 1 2 3 4
	^  ^ ^  ^  ^
= 1 2  3 4  5
'''


print('_________________________')
print("User multiple input in range(input_user_ke_satu) and (input_user_ke_dua)")

multiple = input("Range perulangan: ").split(",") #Split input dengan comma ,

input_user_ke_satu, input_user_ke_dua = multiple #input_user_ke_satu, input_user_ke_dua = multiple.split(",")

for User in range(int(input_user_ke_satu.strip())):
	print("Perulangan (input_user_ke_satu) {}".format(User))

for USer in range(int(input_user_ke_dua.strip())):
	print(f"Perulangan (input_user_ke_dua) {USer}")


print('_________________________')
print("User input in range(user_input)")

user_input = int(input("Range perulangan: ")) # melalui input user conversi int()

for user in range(user_input): #mengulang user_input ×
	print("Perulangan user_input", user)


print('_________________________')
print('Devault value in range(default_value)')

default_value = 5 # mengulang int(5) ×

for default in range(default_value):
	print(default)


print('_________________________')
print("user input in range(user_complex)")
# 5 real + 5j imag (input = 5 real or 5j)
user_complex = complex(input("Range perulangan: "))

for kompleks_user in range(int(user_complex.real)):
	print("user_complex.real Ke-", kompleks_user)

for Kompleks_user in range(int(user_complex.imag)):
	print("user_complex.imag Ke-", Kompleks_user)


print('_________________________')
print("user input in range(default_complex)")

default_complex = 5 + 5j

for kOmpleks in range(int(default_complex.real)):
	print("output = (default_complex.real) Ke-", kOmpleks)

for koMpleks in range(int(default_complex.imag)):
	print("output = (default_complex.imag) Ke-", koMpleks)