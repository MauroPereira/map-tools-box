def ipv4_decimal_to_binary(ipv4_decimal):
    # Divide la dirección IPv4 en octetos
    octetos_decimal = ipv4_decimal.split('.')
    
    # Inicializa una lista vacía para almacenar los octetos binarios
    octetos_binarios = []
    
    # Convierte cada octeto decimal a binario y lo agrega a la lista
    for octeto in octetos_decimal:
        octeto_binario = bin(int(octeto))[2:].zfill(8)
        octetos_binarios.append(octeto_binario)
    
    # Une los octetos binarios con puntos y devuelve la dirección IPv4 en binario
    ipv4_binario = '.'.join(octetos_binarios)
    
    return ipv4_binario

# Ingresa la dirección IPv4 en formato decimal
ipv4_decimal = input("Ingresa una dirección IPv4 en formato decimal (por ejemplo, 192.168.1.1): ")

# Convierte y muestra la dirección IPv4 en formato binario
ipv4_binario = ipv4_decimal_to_binary(ipv4_decimal)
print("La dirección IPv4 en formato binario es:", ipv4_binario)
