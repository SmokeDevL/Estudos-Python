# Na linguagem de programação python temos duas formas de ordenar um array, a primeira delas é usando o método .sort();

array = [4, 2, 1, 3]
array.sort() # Obs: Se tentarmos fazermos o print irá retornar None.
print(array)

#! Resultado;

' [1, 2, 3, 4] '

# Esse é um maneira não tão utilizada porque ela modifica a lista permanentemente, mas se você não precisar da lista desordenada então é uma boa forma de se fazer.

# Usando a função sorted();

array = [4, 2, 1, 3]
print(sorted(array))

#! Resultado;

' [1, 2, 3, 4] '

# Dessa maneira agora tem como ordenar-las sem necessitar modificar a super array.

# Ambas funções recebem o parâmetro key que serve pra você passar uma outra função como parâmetro para ditar como a ordem será feita.

# Usando parâmetro key;

array = [
    ('Carlos', 'A', 16),
    ('Michel', 'B', 30),
    ('Emanuell', 'A', 15),
    ('Isadora', 'A', 14)
]

print(sorted(array, key = lambda array : array[2])) # Sorteando By Age
print(sorted(array, key = lambda array : array[1])) # Sorteando By Exam

#! Resultado;

" [('Isadora', 'A', 14), ('Emanuell', 'A', 15), ('Carlos', 'A', 16), ('Michel', 'B', 30)] "
" [('Carlos', 'A', 16), ('Emanuell', 'A', 15), ('Isadora', 'A', 14), ('Michel', 'B', 30)] "

# Por padrão essas funções ordenam na ordem crescente, mas se quiser que ela ordene do maior pro menor, use o parâmetro reverse = True.

print(sorted(array, key = lambda array : array[2], reverse = True)) # Sorteando by age reverse

#! Resultado;

" [('Michel', 'B', 30), ('Isadora', 'A', 14), ('Emanuell', 'A', 15), ('Carlos', 'A', 16)] "
