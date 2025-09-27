angka = input("Angka ke satu: ")
operator = input("Operator (+ - * float(/) int(//) % **): ")
Angka = input("Angka ke dua: ")

bilangan = input("Desimal or Bulat: ").upper()

output_desimal_bulat_by_logic = print(f"Output Desimal: {float(eval(angka + operator + Angka))}") if bilangan in "DESIMAL" else print(f"Output Bulat: {eval(angka + operator + Angka)}")