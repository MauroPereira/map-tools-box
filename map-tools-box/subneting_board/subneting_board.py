import ipaddress


def generar_tabla_subredes(ip_inicial, num_ips_por_subred, num_subredes):
    try:
        # Convertimos la dirección de red inicial en un objeto ipaddress
        direccion_red = ipaddress.IPv4Address(ip_inicial)
    except ipaddress.AddressValueError:
        print("La dirección IP de red inicial es inválida.")
        return

    tabla = []
    ip_broadcast = None

    for i in range(num_subredes):
        # Calcular la dirección de broadcast
        ip_broadcast = direccion_red + num_ips_por_subred - 1

        # Agregar información a la tabla
        fila = [
            i + 1,  # Número de subred
            str(direccion_red),  # Dirección IP de Red
            str(direccion_red + 1),  # IP Inicial de Host
            str(ip_broadcast - 1),  # IP Final de Host
            str(ip_broadcast),  # Dirección IP de Broadcast
        ]
        tabla.append(fila)

        # Actualizar la dirección de red para la siguiente subred
        direccion_red = ip_broadcast + 1

    # Imprimir la tabla
    print(
        "{:<15} {:<15} {:<20} {:<20} {:<15}".format(
            "Subred",
            "IP de Red",
            "IP Inicial de Host",
            "IP Final de Host",
            "IP de Broadcast",
        )
    )
    for fila in tabla:
        print("{:<15} {:<15} {:<20} {:<20} {:<15}".format(*fila))


if __name__ == "__main__":
    ip_inicial = input("Ingrese la dirección IP de red inicial: ")
    num_ips_por_subred = int(input("Ingrese la cantidad de IPs por subred: "))
    num_subredes = int(input("Ingrese el número de subredes: "))

    generar_tabla_subredes(ip_inicial, num_ips_por_subred, num_subredes)
