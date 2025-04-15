## Funcionalidades

- **Exibição do Tabuleiro:**  
  A função `mostrar_tabuleiro` exibe o estado atual do tabuleiro no console.

- **Busca de Caminho:**  
  A função `proximo_movimento` utiliza recursão para buscar o próximo movimento válido a partir da posição atual e retorna a posição e a profundidade (número de movimentos) do melhor caminho.

- **Validação de Movimento:**  
  A função `movimento_valido` verifica se o movimento está dentro dos limites do tabuleiro e se a célula está livre (representada por um espaço em branco).

- **Verificação de Destino:**  
  A função `chegou_destino` determina se a posição atual é a posição destino (0,3).

- **Execução Interativa:**  
  A função `main` inicializa o tabuleiro, define a posição inicial, marca os movimentos realizados e atualiza o estado do tabuleiro até que o destino seja alcançado ou se determine que não existe um caminho viável.

## Estrutura do Código

- **`mostrar_tabuleiro(tabuleiro)`**  
  Exibe o tabuleiro, formatando os elementos com bordas para facilitar a visualização.

- **`proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade)`**  
  Determina recursivamente o próximo movimento a ser realizado, considerando os movimentos para cima, baixo, esquerda e direita. Retorna uma tupla com a posição e a profundidade.

- **`movimento_valido(tabuleiro, linha, coluna)`**  
  Verifica se a posição desejada está dentro dos limites do tabuleiro e se ela não contém um obstáculo ou já foi visitada.

- **`chegou_destino(linha_atual, coluna_atual)`**  
  Checa se a posição atual corresponde ao destino definido, que é a célula (0,3).

- **`main()`**  
  Função principal que configura o tabuleiro, marca a posição inicial com `*` e executa o loop para mover o "caminhante" até que o destino seja encontrado ou que não exista caminho válido.

  ## Observações

- **Representação dos Elementos:**
  - `' '` (espaço): posição vazia.
  - `'X'`: obstáculo.
  - `'*'`: caminho percorrido.

- **Destino:**  
  Está fixo na posição (0,3), conforme definido na função `chegou_destino`.

- **Algoritmo Recursivo:**  
  Explora os movimentos possíveis (cima, baixo, esquerda e direita) para encontrar o caminho com a menor profundidade até o destino.


