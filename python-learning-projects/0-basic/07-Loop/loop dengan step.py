# Step 2 (Genap)
for genap in range(0, 10, 2):
    print(f"Genap: {genap}")

print('______ Default Value (Ganjil) ______')
# Step 2 (Ganjil)
start, stop, step = 1, 10, 2
for ganjil in range(start, stop, step):
    print(f"Ganjil: {ganjil}")

print('_____ Tuple Example _____')
# Step 4 (Tuple Unpack)
start, stop, step = (0, 20, 4)
for i in range(start, stop, step):
    print("Genap:", i)

print('______ User Input ______')
print("Pilih jenis bilangan:\n0 = Genap\n1 = Ganjil")

b = int(input("Option (0/1): "))
r = int(input("Range batas akhir: "))
l = int(input("Loncat (step): "))

for i in range(b, r, l):
    print(f"Bilangan mulai dari {b}:", i)