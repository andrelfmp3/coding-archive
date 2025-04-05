print(type(404))  
print(type(4.04))  
print(type("True"))  
print(type(True)) 

# Número complexo 
# x = 3 + 4j (com lib)
# print(type(x))  

print(type(None))  

# Lista (ordenada e mutável)
print(type([1, 2, 3]))  
# Tupla (ordenada e imutável)
print(type((1, 2, 3))) 
# Conjunto (não ordenado e mutável)
print(type({1, 2, 3}))  
# Conjunto (não ordenado e imutável)
conjunto_imutavel = frozenset([1, 2, 3])  # Criação de um frozenset
print(type(conjunto_imutavel))  

# Dicionário (pares chave-valor)
print(type({'a': 1}))  

# Bytearray (mutável, array de bytes)
print(type(bytearray(5)))  
# Bytes (imutável, sequência de bytes)
print(type(b"abc")) 
# Memoryview (usado para acesso eficiente a fatias de dados binários)
mv = memoryview(b"abc")
print(type(mv))  

print(type(range(5)))  

print("\n1234"[1])  # (o caractere na posição 1 é '1')
print("\n" + "1234"[0])  # (adiciona uma nova linha antes de '1')
