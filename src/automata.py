def load_automata(filename):
    """
    Lê os dados de um autômato finito a partir de um arquivo.
    A estsrutura do arquivo deve ser:
    <lista de símbolos do alfabeto, separados por espaço (' ')>
    <lista de nomes de estados>
    <lista de nomes de estados finais>
    <nome do estado inicial>
    <lista de regras de transição, com "origem símbolo destino">
    Um exemplo de arquivo válido é:
    ```
    a b
    q0 q1 q2 q3
    q0 q3
    q0
    q0 a q1
    q0 b q2
    q1 a q0
    q1 b q3
    q2 a q3
    q2 b q0
    q3 a q1
    q3 b q2
    ```
    Caso o arquivo seja inválido uma exceção Exception é gerada.
    """
    with open(filename, "rt") as arquivo:
        # Lê linhas do arquivo e processa os dados
        lines = arquivo.readlines()
        
        alphabet = tuple(lines[0].strip().split())
        states = tuple(lines[1].strip().split())
        final_states = tuple(lines[2].strip().split())
        initial_state = lines[3].strip()
        
        transitions = []
        for line in lines[4:]:
            transitions.append(tuple(line.strip().split()))
    
    # Verifica se os estados inicial e finais são válidos
    if initial_state not in states:
        raise ValueError("Estado inicial inválido")
    
    for state in final_states:
        if state not in states:
            raise ValueError(f"Estado final inválido: {state}")
    
    # Verifica se todas as transições são válidas
    for trans in transitions:
        if trans[0] not in states or trans[2] not in states or trans[1] not in alphabet:
            raise ValueError(f"Transição inválida: {trans}")
    
    return states, alphabet, transitions, initial_state, final_states

def process(automata, words):
    """
    Processa uma lista de palavras em um autômato finito e imprime se cada palavra é ACEITA ou REJEITADA.
    """
    states, alphabet, transitions, initial_state, final_states = automata
    
    for word in words:
        current_state = initial_state
        for symbol in word:
            if symbol not in alphabet:
                print("INVÁLIDA")
                break
            transition_found = False
            for trans in transitions:
                if trans[0] == current_state and trans[1] == symbol:
                    current_state = trans[2]
                    transition_found = True
                    break
            if not transition_found:
                print("INVÁLIDA")
                break
        
        if current_state in final_states:
            print("ACEITA")
        else:
            print("REJEITA")
