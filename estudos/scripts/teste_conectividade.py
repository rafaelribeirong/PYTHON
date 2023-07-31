import socket
import os

def ping_icmp(ip):
    response = os.system("ping -n 1 " + ip)

    if response == 0:
        print(f"{ip} está online (ICMP)")
    else:
        print(f"{ip} não está respondendo (ICMP)")

def ping_tcp(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)  # Define um timeout de 3 segundos para a conexão
        s.connect((ip, port))
        s.close()
        return True
    except socket.error:
        return False

def testar_portas_fixas(ip_alvo):
    print(f"\nTestando portas fixas em {ip_alvo}...\n")
    portas_fixas = [80, 443, 22, 21, 3389]
    for porta in portas_fixas:
        if ping_tcp(ip_alvo, porta):
            print(f"A porta {porta} está aberta em {ip_alvo}.")
        else:
            print(f"A porta {porta} não está respondendo em {ip_alvo}.")

def testar_intervalo_portas(ip_alvo, porta_inicial, porta_final):
    print(f"\nTestando intervalo de portas em {ip_alvo}...")
    for porta in range(porta_inicial, porta_final + 1):
        if ping_tcp(ip_alvo, porta):
            print(f"A porta {porta} está aberta em {ip_alvo}.")
        else:
            print(f"A porta {porta} não está respondendo em {ip_alvo}.")

def resolver_nome_do_ip(ip_alvo):
    try:
        nome = socket.gethostbyaddr(ip_alvo)
        print(f"\nNome do dispositivo alvo: {nome[0]}")
    except socket.herror:
        print(f"\nNão foi possível resolver o nome do dispositivo alvo para o IP {ip_alvo}.")

def testar_multiplos_dispositivos():
    num_dispositivos = int(input("\nDigite o número de dispositivos a serem testados: "))
    dispositivos = []
    for i in range(num_dispositivos):
        ip = input(f"Digite o endereço IP do dispositivo {i+1}: ")
        dispositivos.append(ip)

    for dispositivo in dispositivos:
        print(f"\nTestando conectividade em {dispositivo}...")
        ping_icmp(dispositivo)
        testar_portas_fixas(dispositivo)

if __name__ == "__main__":
    ip_alvo = input("Digite o endereço IP do dispositivo alvo: ")

    if not ip_alvo:
        print("O endereço IP deve ser especificado.")
        exit(1)

    ping_icmp(ip_alvo)

    while True:
        print("\nOpções disponíveis:")
        print("1. Testar portas fixas (80, 443, 22, 21, 3389)")
        print("2. Testar intervalo de portas")
        print("3. Resolver nome do dispositivo a partir do IP")
        print("4. Testar em múltiplos dispositivos")
        print("5. Sair")

        opcao = input("\nSelecione uma opção (1, 2, 3, 4 ou 5): ")

        if opcao == "1":
            testar_portas_fixas(ip_alvo)
        elif opcao == "2":
            porta_inicial = int(input("Digite o número da porta inicial: "))
            porta_final = int(input("Digite o número da porta final: "))
            testar_intervalo_portas(ip_alvo, porta_inicial, porta_final)
        elif opcao == "3":
            resolver_nome_do_ip(ip_alvo)
        elif opcao == "4":
            testar_multiplos_dispositivos()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Digite uma opção válida (1, 2, 3, 4 ou 5).")
