# ===================================================================
# Implementação de um Autômato Finito Determinístico (AFD)
# Autor: Ruam Marcos Maciel dos Santos
# Descrição: Este script define e testa um AFD usando uma
#            função de transição estendida implementada recursivamente.
# ===================================================================

# --- 1. Definição Formal do Autômato ---

# O dicionário a seguir representa a função de transição (delta) do AFD.
# Mapeia (estado_atual, simbolo) -> proximo_estado.
dfa_transitions = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q2', 'b': 'q3'},
    'q2': {'a': 'q4', 'b': 'q5'},
    'q3': {'a': 'q6', 'b': 'q7'},
    'q4': {'a': 'q4', 'b': 'q5'},
    'q5': {'a': 'q6', 'b': 'q7'},
    'q6': {'a': 'q2', 'b': 'q3'},
    'q7': {'a': 'q1', 'b': 'q0'}
}

# Estado que dá início ao processamento.
initial_state = 'q0'

# Conjunto de estados que indicam a aceitação da palavra.
accepting_states = {'q4', 'q5', 'q6', 'q7'}

# --- 2. Função de Transição Estendida (Recursiva) ---

def run_dfa_recursive(current_state, input_word):
    """
    Processa uma palavra no AFD de forma recursiva.

    Args:
        current_state: O estado atual do autômato.
        input_word: A parte restante da palavra a ser processada.

    Returns:
        O estado final após o processamento completo da palavra.
    """
    # Caso base: Se a palavra estiver vazia, retornamos o estado em que paramos.
    if not input_word:
        return current_state
    
    # Passo recursivo:
    # 1. Pega o primeiro símbolo da palavra.
    symbol = input_word[0]
    # 2. Pega o restante da palavra para a próxima chamada.
    remaining_word = input_word[1:]
    
    # 3. Usa a tabela de transições para encontrar o próximo estado.
    next_state = dfa_transitions[current_state][symbol]
    
    # 4. Chama a função novamente com o novo estado e o resto da palavra.
    return run_dfa_recursive(next_state, remaining_word)

# --- 3. Execução e Testes ---

def main():
    """
    Função principal que executa os testes do AFD.
    """
    words_to_test = [
        "babaaab",
        "aabba",
        "aaa",
        "bbb",
        "ababab",
        "ababaaba"
    ]

    print("Iniciando simulação do AFD...")
    print("-" * 40)

    for word in words_to_test:
        # A primeira chamada usa o estado inicial e a palavra completa.
        final_state = run_dfa_recursive(initial_state, word)
        
        # Verifica se o estado final é um estado de aceitação.
        is_accepted = "ACEITA" if final_state in accepting_states else "REJEITA"
        
        print(f"Palavra de entrada: '{word}'")
        print(f"  -> Estado de parada: '{final_state}'")
        print(f"  -> Resultado: Palavra {is_accepted}")
        print("-" * 40)

# Ponto de entrada do script.
if __name__ == "__main__":
    main()