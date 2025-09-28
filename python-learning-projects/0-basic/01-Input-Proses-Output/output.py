print('___String___')

teks = input("teks: ")

print(teks) # Variabel output

print(type(teks))
print('______________________')


print('___int___')

bulat = int(input("input bulat: "))

print("Output Bilangan Bulat:", bulat) # Multiple output

print(type(bulat))
print('______________________')


print('___float___')

desimal = float(input("Input desimal: "))

print("Output Bilangan Desimal: {}".format(desimal)) # format() output

print(type(desimal))
print('______________________')


print('___complex (real and imag)___')
print("Input: = 10 output real (float)")
print("Input: 10j = output imag (float)")

complexs = complex(input("Input complex: "))

print(f"Output complexs.real: {complexs.real}") # f-string output

print("Output complexs.imag: " + str(complexs.imag)) # concatenation

print(type(complexs))
print('______________________')


print('___type list (input(' ').split(",") )___')

split_input = input("Split input dengan coma (,): ").split(",")

name, age = split_input
age = int(age.strip())

print("Name:\t", name)  # Escape character
print("Age:\t", age) # tab 
print('______________________')


print('___type list (variabel = variabel.split(",") )___')

Split_input = input("Split input dengan coma (,): ")

Name, Age = Split_input.split(",")
Age = int(Age.strip())

print("Name:\t","_".join(Name)) # join list
print("Age:\t", Age)
print("Name:\t","".join(Name))
print('______________________')