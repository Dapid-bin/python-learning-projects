# Looping langsung string
for x in "DAPID":
    print(x)

# Slicing string
nama = "dapid This is"
print("\tSlicing:", nama[6:14])

# Loop huruf pertama -> uppercase repeat
for h in nama[:5]:
    print("\t----->", h.upper() * 10, "<-----")

# Input user dengan enumerasi
name = input("\tMasukkan Nama: ")
print(f"\tNama {name.capitalize()} punya {len(name)} huruf.")

start = int(input("\tMulai dari index ke berapa? "))
for i, huruf in enumerate(name[start:], start=start):
    print(f"{i} | {name.capitalize()} = {huruf.upper()}")

# Loop tiap huruf dengan nomor
Nama = input("\tNama lain: ")
print(f"Nama {Nama} ada {len(Nama)} huruf.")
for no, huruf in enumerate(Nama, start=1):
    print(no, "->", huruf.upper())