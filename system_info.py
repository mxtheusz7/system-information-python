import platform
import getpass
import socket
import psutil


def mostrar_sistema():
    print("Nome do computador:", platform.node())
    print("Usuário atual:", getpass.getuser())
    print("Sistema operacional:", platform.system())
    print("Versão do sistema:", platform.version())
    print("Arquitetura:", platform.architecture()[0])

def mostrar_hardware():
    print("\n[ HARDWARE ]")
    print("Processador:", platform.processor())
    print("Uso da CPU:", psutil.cpu_percent(interval=1), "%")

    memoria = psutil.virtual_memory()
    print("Memória RAM total:", round(memoria.total / 1024 ** 3, 2), "GB")
    print("Memória RAM disponível:", round(memoria.available / 1024 ** 3, 2), "GB")

    disco = psutil.disk_usage("/")
    print("Armazenamento total:", round(disco.total / 1024 ** 3, 2), "GB")
    print("Armazenamento disponível:", round(disco.free / 1024 ** 3, 2), "GB")

def mostrar_rede():
    print("\n[ REDE ]")
    print("Endereço IP:", socket.gethostbyname(socket.gethostname()))

print("=" * 40)
print("SYSTEM INFORMATION")
print("=" * 40)

mostrar_sistema()
mostrar_hardware()
mostrar_rede()

print("=" * 40)