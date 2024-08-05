# Tabla de verdad para AND, OR, NOT y XOR

# Valores posibles de entrada
p = True
q = False

# AND (y)
and_tt = p and p  # True AND True
and_tf = p and q  # True AND False
and_ft = q and p  # False AND True
and_ff = q and q  # False AND False

# OR (o)
or_tt = p or p  # True OR True
or_tf = p or q  # True OR False
or_ft = q or p  # False OR True
or_ff = q or q  # False OR False

# NOT (no)
not_t = not p  # NOT True
not_f = not q  # NOT False

# XOR (o exclusivo)
xor_tt = p != p  # True XOR True (equivalente a (p or q) and not (p and q))
xor_tf = p != q  # True XOR False
xor_ft = q != p  # False XOR True
xor_ff = q != q  # False XOR False

# Imprimir la tabla de verdad
print("AND")
print("P\t\tQ\t\tP AND Q")
print(f"{p}\t{p}\t{and_tt}")
print(f"{p}\t{q}\t{and_tf}")
print(f"{q}\t{p}\t{and_ft}")
print(f"{q}\t{q}\t{and_ff}")

print("\nOR")
print("P\t\tQ\t\tP OR Q")
print(f"{p}\t{p}\t{or_tt}")
print(f"{p}\t{q}\t{or_tf}")
print(f"{q}\t{p}\t{or_ft}")
print(f"{q}\t{q}\t{or_ff}")

print("\nNOT")
print("P\t\tNOT P")
print(f"{p}\t{not_t}")
print(f"{q}\t{not_f}")

print("\nXOR")
print("P\t\tQ\t\tP XOR Q")
print(f"{p}\t{p}\t{xor_tt}")
print(f"{p}\t{q}\t{xor_tf}")
print(f"{q}\t{p}\t{xor_ft}")
print(f"{q}\t{q}\t{xor_ff}")
