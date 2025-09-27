teks = input("teks: ") # "Abc012"

bulat = int(input("input bulat: ")) # 1

desimal = float(input("Input desimal: ")) # 1.0

complexs = complex(input("Input complex: ")) # Output (1 real (1j imag))

split_input = input("Split input dengan coma (,): ").split(",") # Input Dapid,19
name, age = split_input
age = int(age.strip()) # <- conversi str -> to int
