Em python, um dicionário é uma das principais estruturas de dados, é uma sequencia de pares chave-valor separados por virgula e cercados por chaves

**{key:value, key:value}**

Um dicionário, então, é criado abrindo uma chave e colocando um par de valores-chave separados por virgula

```python
dicionario = {
    "1": {
        "id": 1,
        "nome": "teste",
        "email": "teste@gmail.com",
        "senha": "1234"
    },
    "2": {
        "id": 1,
        "nome": "teste",
        "email": "teste1@gmail.com",
        "senha": "12341"
    }
}
```
Os valores podem ser de qualquer tipo de dados e podem ser duplicados, contudo as chaves são únicas, como o caso do 1 e 2 ali.
Dentro das chaves estão repetindo as chaves "nome", "email", etc, porque estão dentro de outra chave.


Para manipular dicionários em python, existem 10 métodos.
 - para acessar o valor de uma chave espeficica, usamos o _get()_

```python
dicionario = {
    "1": {
        "id": 1,
        "nome": "teste",
        "email": "teste@gmail.com",
        "senha": "1234"
    },
    "2": {
        "id": 1,
        "nome": "teste",
        "email": "teste1@gmail.com",
        "senha": "12341"
    }
}
# aqui você ta acessando a chave 1
dicionario.get("1")

# para acessar a chave id da chave 1, se faz assim:
dicionario.get("1").get("id")

# ou

dicionario["1"]["id"]
```

Observe que foi usado o get para acessar a key 1 e obter o seu valor, o get vai retornar o valor da chave se ela existir, caso ela não exista vai retornar _None_ como default, ou se for o caso, você pode especificar um valor de fallback: get("1", "valor de retorno").

No exemplo acima, se não existir a chave 1 ele vai retornar a string "valor de retorno".