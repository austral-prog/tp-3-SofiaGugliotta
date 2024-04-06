def check_vowels():

    name = input("Ingresa tu nombre: ")
    
    a = "a" in name.lower()
    e = "e" in name.lower()
    i = "i" in name.lower()
    o = "o" in name.lower()
    u = "u" in name.lower()

    print(f"Contiene a: {a}")
    print(f"Contiene e: {e}")
    print(f"Contiene i: {i}")
    print(f"Contiene o: {o}")
    print(f"Contiene u: {u}")
    
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
