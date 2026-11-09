# Anotações de Estudo — Python

**Data:** 08/11/2026  
**Curso:** Python — freeCodeCamp  
**Status:** Em aprendizado

## 1. Métodos de Strings

### `.find()`
Procura uma substring dentro de uma string e retorna o índice da primeira ocorrência.

- Os índices começam em `0`.
- Se a substring não for encontrada, retorna `-1`.

### `.title()`
Converte a primeira letra de cada palavra em maiúscula e, normalmente, as demais letras em minúsculas.

### `.lower()`
Converte todas as letras da string em minúsculas.

### `.upper()`
Converte todas as letras da string em maiúsculas.

### `.strip()`
Remove espaços em branco e outros caracteres de espaçamento, como quebras de linha, do início e do final de uma string.

- Não remove os espaços entre as palavras.

### `.replace(old, new)`
Substitui as ocorrências de uma substring (`old`) por outra (`new`).

- Por padrão, substitui todas as ocorrências encontradas.

### `.split()`
Divide uma string em uma lista de substrings.

- É possível definir um separador.
- Sem um separador informado, utiliza sequências de espaços em branco para realizar a divisão.

### `' '.join(lista)`
Junta os elementos de uma sequência de strings em uma única string.

- O conteúdo entre as aspas define o separador utilizado.
- `' '.join(lista)` utiliza um espaço entre os elementos.

## 2. Fatiamento de Strings (Slicing)

O *slicing* permite extrair partes de uma string utilizando seus índices.

**Sintaxe:** `string[inicio:fim]`

- `inicio`: índice onde o fatiamento começa (inclusivo).
- `fim`: índice onde o fatiamento termina (exclusivo).
- O caractere correspondente ao índice final não é incluído no resultado.

## 3. Verificação de Substrings — `in`

A palavra-chave `in` permite verificar se uma substring está presente em outra string.

- Retorna `True` quando a substring é encontrada.
- Retorna `False` quando a substring não está presente.
- Diferentemente de `.find()`, não retorna a posição da substring.

## 4. Resumo do Aprendizado

Nesta sessão, estudei diferentes formas de manipular strings em Python.

Aprendi a localizar substrings, extrair partes de textos, verificar a presença de caracteres ou palavras, modificar letras maiúsculas e minúsculas, remover espaços, substituir conteúdos e dividir ou juntar strings.

**Status:** Conteúdo estudado. Ainda preciso praticar para consolidar o aprendizado.
