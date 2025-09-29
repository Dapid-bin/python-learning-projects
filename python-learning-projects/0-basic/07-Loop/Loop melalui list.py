print("\t🌀 KGC 🌀 QUANT")

nama = {"Nama": "DAPID"}
for name in nama:
	print(f"{name} kami {nama.get("Nama")} 🤝")


# Basic
data = ["Denisa", "Ayu", "Amelia", "Zaskia"]
for nama_teman in data:
	print("Teman saya:", nama_teman)


nama_nama_hewan = ["Buaya", "Ayam", "Singa", "Harimau"]
nama_nama_hewan.append("Python 🐍")

for no, nama_hewan in enumerate(nama_nama_hewan, start=1):
	print(f"{no}. Nama Hewan: {nama_hewan}")


buah = []
def user_input(buah, apa):
	buah.append(input(apa))

user_input(buah, "Kamu suka buah apa: ")

for user_suka_buah in buah:
	print("Kamu suka buah", user_suka_buah)