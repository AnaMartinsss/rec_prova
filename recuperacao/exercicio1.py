"""
1) Separar múltiplos de 3 e 5

Objetivo:
Crie uma função chamada listar_multiplos(n) que receba um número inteiro n e:
- Liste todos os números de 1 até n que sejam múltiplos de 3 e 5.
- Indique claramente se cada número é múltiplo de 3, de 5 ou de 3 e 5 (quando for divisível por 15).
- Ao final, retorne a contagem total desses números.

Observação:
- Utilize estruturas de repetição para percorrer o intervalo de 1 a n.
- Faça uso de condicionais (if/elif/else) para verificar a divisibilidade.

Exemplo de Chamada:
    resultado = listar_multiplos(15)
    print(resultado)
    # Exemplo de saída (em texto):
    # 3 → Múltiplo de 3
    # 5 → Múltiplo de 5
    # 6 → Múltiplo de 3
    # ...
    # 15 → Múltiplo de 3 e 5
    # Total de números listados: 7

Requisitos:
- Use ao menos uma estrutura de repetição (for ou while).
- Faça uso de condicionais para classificar cada número.
- Retorne (ou exiba) a contagem total ao final.
"""
# Solution:

def listar_multiplos(n):
 contador = 0
 for i in range(1, n+1):
  if n % 15 == 0:
     print(f"{i} -> Múltiplo de 3 e 5 ")
     contador += 1
  elif n % 5 ==0:
    print(f"{i} -> Múltiplo de 5")
    contador +=1 
  elif n % 3 ==0:
     print(f"{i} -> Múltiplo de 3 ")
     contador +=1
  print(f"Total de números listados: {contador}")
  return contador


listar_multiplos(15) 


    