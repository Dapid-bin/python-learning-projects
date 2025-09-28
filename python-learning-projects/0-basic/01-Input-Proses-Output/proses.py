print("Proses")

# If else
nilai_Dapid = int(input("Nilai Dapid: "))
nilai_Amelia = int(input("Nilai Amelia: "))
nilai_Icak =  input('Nilai Icak: ')
nilai_Budi = input('Nilai Budi: ')

if nilai_Dapid >= 80:
	status_Dapid = 'Lulus'
else:
	status_Dapid = "Tidak lulus"

if nilai_Amelia >= 80:
	status_Amelia = 'Lulus'
else:
	status_Amelia = "Tidak lulus"

if int(nilai_Icak) >= 80:
	status_Icak = 'Lulus'
else:
	status_Icak = "Tidak lulus"

if int(nilai_Budi) >= 80:
	status_Budi = 'Lulus'
else:
	status_Budi = "Tidak lulus"

print("Nilai Dapid:", nilai_Dapid, 'Status', status_Dapid)

print(f'''Nilai Amelia: {nilai_Amelia} Status {status_Amelia}
Nilai Icak: {int(nilai_Icak)} Status {status_Icak}''')

print("Nilai Budi: {} Status {}".format(int(nilai_Budi), status_Budi))

# match case
nIlai_Dapid = int(input("Nilai Dapid: "))
nIlai_Amelia = int(input("Nilai Amelia: "))
nIlai_Icak =  int(input('Nilai Icak: '))
nIlai_Budi = int(input('Nilai Budi: '))

match str(nIlai_Dapid >= 80):
	case "True":
		print("Nilai Dapid: {} Status Lulus".format(nIlai_Dapid))
	case _:
		print("Nilai Dapid: {} Status Tidak lulus".format(nIlai_Dapid))

match str(nIlai_Amelia >= 80):
	case "True":
		print("Nilai Amelia: {} Status Lulus".format(nIlai_Amelia))
	case _:
		print("Nilai Amelia: {} Status Tidak lulus".format(nIlai_Amelia))

match str(nIlai_Icak >= 80):
	case "True":
		print(f"Nilai Icak: {nIlai_Icak} Status Lulus")
	case _:
		print(f"Nilai Icak: {nIlai_Icak} Status Tidak lulus")

match str(nIlai_Budi >= 80):
	case 'True':
		print(f"Nilai Budi: {nIlai_Budi} Status Lulus")
	case _:
		print(f"Nilai Budi: {nIlai_Budi} Status Tidak lulus")

# dict
Nilai_Dapid = int(input("Nilai Dapid: "))
Nilai_Amelia = int(input("Nilai Amelia: "))
Nilai_Icak =  input('Nilai Icak: ')

nilai = {
	"Dapid": Nilai_Dapid,
	"Amelia": Nilai_Amelia,
	"Icak": int(Nilai_Icak)
}
nilai["Budi"] = int(input("Nilai Budi: "))

Status = {name: ("Lulus" if score >= 80 else 'Tidak lulus')
	for name, score in nilai.items()}

print("____View____")
print("Nilai Dapid:", nilai.get('Dapid'))
print("Nilai Amelia:", nilai.get('Amelia'))
print("Nilai Icak: {}".format(nilai.get('Icak')))
print("Nilai Budi: " + str(nilai.get("Budi")))

print(f"Status: {Status}")