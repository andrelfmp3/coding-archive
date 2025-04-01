import socket  # nativo

try:
    # Criando o socket TCP. socket.socket(family, type)
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 e tcp
except socket.error as err:
    print(f"Erro durante criação do socket: {err}")
    exit()

host = "127.0.0.1"  # endereço local
port = 8080         # porta que será utilizada, root

try:
    # Tentativa de fazer o bind do socket ao endereço e porta
    tcp_socket.bind((host, port))  # de modo que o servidor escute nesse endereço e porta
    tcp_socket.listen(1)  # permitindo até 1 conexão na fila
    print(f"Servidor iniciado em {host}:{port}")
except socket.error as err:
    print(f"Erro ao tentar fazer o bind na porta {port}: {err}")
    tcp_socket.close()  # Fechar o socket se não conseguir fazer bind
    exit()

while True:  # Loop para aceitar conexões
    try:
        c, addr = tcp_socket.accept()
        print(f"Conexão recebida de {addr[0]}:{addr[1]}")
        c.close()  # Fecha a conexão após o log
    except socket.error as err:
        print(f"Erro ao aceitar conexão: {err}")
        continue  # Continua esperando por novas conexões

tcp_socket.close()  # Fecha o socket principal quando o loop terminar
