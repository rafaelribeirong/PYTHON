## Projeto: Teste de Conectividade em Portas (Ping TCP)

### Descrição do Projeto
Este projeto é um programa em Python que permite testar a conectividade em dispositivos alvo através do protocolo TCP. O programa verifica se um determinado endereço IP responde em portas específicas ou em um intervalo de portas definido pelo usuário. O teste é realizado utilizando a função `socket.connect()` para estabelecer uma conexão TCP com o dispositivo alvo em cada porta testada.

### Funcionalidades do Projeto
1. Verificação de conectividade usando protocolo TCP em portas específicas ou em um intervalo de portas.
2. Relatório detalhado exibindo as portas que estão abertas ou fechadas.
3. Tratamento de exceções para evitar falhas no programa.
4. Suporte para resolver o nome do dispositivo alvo a partir do endereço IP.
5. Interface de linha de comando interativa para interação com o usuário.
6. Opção para testar conectividade em múltiplos dispositivos alvo.
7. Histórico dos testes realizados em execuções anteriores.
8. Opção para salvar o histórico de testes em um arquivo para referência futura.

### Instruções de Uso
1. Certifique-se de ter o Python 3 instalado em seu computador.
2. Clone ou faça o download do projeto para o seu computador.
3. Execute o arquivo `teste_conectividade.py` em um terminal ou prompt de comando.
4. Digite o endereço IP do dispositivo alvo quando solicitado.
5. Escolha entre testar um conjunto de portas fixas, um intervalo de portas ou carregar o histórico de testes.
6. O programa exibirá os resultados dos testes para cada porta ou intervalo de portas.

### Comandos Disponíveis
- `ip`: Digite o endereço IP do dispositivo alvo.
- `portas_fixas`: Testa as portas 80, 443, 22, 21 e 3389.
- `intervalo_portas`: Testa um intervalo de portas definido pelo usuário.
- `resolver_nome`: Habilita a resolução do nome do dispositivo a partir do IP.
- `testar_multiplos_dispositivos`: Habilita o teste em múltiplos dispositivos alvo.
- `historico`: Exibe o histórico dos testes realizados em execuções anteriores.
- `salvar_historico`: Salva o histórico atual de testes em um arquivo.

### Exemplo de Uso
1. Digite o endereço IP do dispositivo alvo quando solicitado: `192.168.1.1`
2. Opções disponíveis:
   - Digite `1` para testar as portas fixas (80, 443, 22, 21, 3389).
   - Digite `2` para testar um intervalo de portas definido pelo usuário.
   - Digite `3` para resolver o nome do dispositivo a partir do IP.
   - Digite `4` para testar a conectividade em múltiplos dispositivos alvo.
   - Digite `5` para exibir o histórico dos testes realizados.
3. Opção escolhida: `2`
4. Digite o número da porta inicial: `1000`
5. Digite o número da porta final: `1020`
6. Deseja resolver o nome do dispositivo alvo a partir do IP? (sim/nao): `sim`
7. Deseja testar em múltiplos dispositivos? (sim/nao): `sim`
8. Digite o número de dispositivos a serem testados: `3`
   - Digite o endereço IP do dispositivo 1: `192.168.1.2`
   - Digite o endereço IP do dispositivo 2: `192.168.1.3`
   - Digite o endereço IP do dispositivo 3: `192.168.1.4`
9. Resultado dos testes de conectividade:
   ```
   192.168.1.1 (Dispositivo1):
   - Porta 1000: Fechada
   - Porta 1001: Aberta
   - Porta 1002: Fechada
   ...
   192.168.1.4 (Dispositivo3):
   - Porta 1000: Aberta
   - Porta 1001: Aberta
   - Porta 1002: Fechada
   ...
   ```
10. Deseja salvar o histórico desses testes? (sim/nao): `sim`
    - Histórico salvo com sucesso em "historico_testes.txt".

### Observações
- Esse é um projeto de exemplo com funcionalidades básicas de cibersegurança em Python.
- O programa pode ser expandido e aprimorado conforme necessário.
- A segurança é fundamental; nunca utilize esse programa para fins maliciosos ou sem autorização adequada.