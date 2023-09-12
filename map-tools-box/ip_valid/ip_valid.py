import ipaddress


def validar_ip(ip_str):
    try:
        ipaddress.IPv4Network(ip_str, strict=False)
        return True
    except ipaddress.AddressValueError:
        return False


def determinar_clase(ip_obj):
    if ip_obj.is_private:
        return "IP Privada"
    elif ip_obj.is_loopback:
        return "IP de Loopback"
    elif ip_obj.is_link_local:
        return "IP Link-Local"
    elif ip_obj.is_reserved:
        return "IP Reservada"
    elif ip_obj.is_multicast:
        return "IP Multicast"
    elif ip_obj.is_unspecified:
        return "IP No Especificada"
    else:
        if ip_obj.is_ipv4:
            if ip_obj.is_global:
                if ip_obj.network_address == ip_obj:
                    return "IP de Red"
                elif ip_obj.broadcast_address == ip_obj:
                    return "IP de Broadcast"
                else:
                    return "IP Válida"
            else:
                return "IP No Global"
        else:
            return "IPv6 (No se maneja en este script)"


def es_subneteada(ip_obj, mask_str):
    try:
        mask = ipaddress.IPv4Network(mask_str, strict=False)
        return ip_obj != mask.network_address and ip_obj != mask.broadcast_address
    except ipaddress.AddressValueError:
        return False


while True:
    ip_str = input("Ingresa una dirección IP (formato x.x.x.x): ")
    mask_str = input("Ingresa una máscara de subred (formato x.x.x.x): ")

    if not validar_ip(ip_str):
        print("La dirección IP ingresada no es válida.")
        continue

    ip_obj = ipaddress.IPv4Address(ip_str)
    clase = determinar_clase(ip_obj)
    subneteada = es_subneteada(ip_obj, mask_str)

    print(f"Clase: {clase}")
    if subneteada:
        print("La IP está subneteada.")
    else:
        print("La IP no está subneteada.")

    break
