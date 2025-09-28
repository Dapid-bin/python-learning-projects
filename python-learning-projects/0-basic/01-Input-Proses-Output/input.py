print('___String___')

teks = input("teks: ") # "Abc012"

print('______________________')


print('___int___')

bulat = int(input("input bulat: ")) # 1

print('______________________')


print('___float___')

desimal = float(input("Input desimal: ")) # 1.0

print('______________________')


print('___complex___')

complexs = complex(input("Input complex: ")) # Output (1 real (1j imag))

print('______________________')


print('___type list (input(' ').split(",") )___')

split_input = input("Split input dengan coma (,): ").split(",") # Input Dapid,19

name, age = split_input

age = int(age.strip()) # <- conversi str -> to int
print('______________________')


print('___type list (variabel = variabel.split(",") )___')

Split_input = input("Split input dengan coma (,): ")

Name, Age = Split_input.split(",")

Age = int(Age.strip())
print('______________________')

print(type(teks))
print(type(bulat))
print(type(desimal))
print(type(complexs))
print(type(split_input))