## Seleção Simultânea do Maior e do Menor Elementos 
   
## Descrição do projeto
Implementação do algoritmo de seleção simultânea do maior e do menor elemento de um array utilizando a estratégia de divisão e conquista. A solução recursiva reduz o número de comparações em relação ao método ingênuo de procurar primeiro o mínimo e depois o máximo separadamente.

## Como executar o projeto
   
   1. **Pré-requisitos**:
      - Ter o Python 3 instalado.
   
   2. **Passos para Execução**:
       - **Clonar o repositório**:      
        ```bash
          git clone https://github.com/larisilvapedrosa/Selecao_Simultanea_Maior_Menor.git
        ```
   
        - **Navegar até o diretório do projeto**:      
        ```bash
          cd Selecao_Simultanea_Maior_Menor
        ```
   
        - **Executar o programa**:      
        ```bash
          python main.py
        ```
   
        - **Interação**:      
        Apos rodar o projeto sera exibido o exemplo de array e qual é o menor e o maior valor.

## Implementação
   1. De início é verificado se a lista tiver apenas 1 elemento, este elemento é tanto o min quanto o max.
   
   ```python
     if len(arr) == 1:
        return arr[0], arr[0]
   ```

  2. Em seguida verifica se a lista tiver apenas 2 elementos, apenas uma comparação é necessária para definir min e max:
   ```python
      if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]
   ```

  3. Em seguida o array sera dividido em 2 metades.
   ```python
      meio = len(arr) // 2
   ```

  4. Em seguida sera feita obtemos:<br/>Recursivamente obtemos min_esq, max_esq da sublista esquerda e <br/>
     Recursivamente obtemos min_dir, max_dir da sublista direita
   ```python
      min_esq, max_esq = maxmin_select(arr[:meio])
      min_dir, max_dir = maxmin_select(arr[meio:])
   ```

  5. Obtemos o menor valor geral que será o menor entre min_esq e min_dir e <br/>
     Obtemos o maior valor geral que será o maior entre max_esq e max_dir
   ```python
      menor_valor = min(min_esq, min_dir)
      maior_valor = max(max_esq, max_dir)
   ```

  6. Após isso sera retornado o par (menor_valor, maior_valor) encontrado
   ```python
      return menor_valor, maior_valor
   ```

  ### Exemplo Saída execução
   ![SaidaExec](Images/SaidaExec.png)

  ## Relatório Técnico
  ### Análise da Complexidade Ciclomática
  Para o array com mais de dois elementos é realizada: <br/>
    1. 2 chamadas recursivas, cada uma em uma lista (n/2). <br/>
    2. 2 comparações adicionais (uma para o menor e outra para o maior) após receber os resultados das subchamadas.

  Com isso temos o total de operações:

$$
2⋅n/2
$$

então:

$$
O(n) = n
$$

### Análise pelo Teorema Mestre
- No caso do MaxMin Select, temos a recorrência:
  
$$
(n)=2⋅T( n/2)+O(1)
$$

Comparando: <br/>
- a = 2
- b = 2
- f(n) = O(1)

Calculamos: <br/>
- log_b(a) = log_2(2) = 1

Então 
- f(n) = O(1)

Pelo Teorema Mestre estamos no caso 1 onde: f(n) < O(n^log_b(a))

Então 
- T(n) = O(n)

Com isso podemos concluir que tanto pela contagem de operações quanto pelo Teorema Mestre, o custo do algoritmo MaxMin Select é linear, 
𝑂(𝑛).
  
