import ipaddress


def colorear_ip(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        if ip.is_private:
            clase = "IP privada"
        elif ip.is_multicast:
            clase = "IP multicast (Clase D)"
        elif ip.version == 4:
            if ip.is_reserved:
                clase = "IP reservada"
            elif ip.is_loopback:
                clase = "IP loopback"
            elif ip.is_link_local:
                clase = "IP de enlace local"
            elif ip.is_global:
                if ip.is_private:
                    clase = "IP privada"
                elif ip.is_multicast:
                    clase = "IP multicast (Clase D)"
                elif ip.is_unspecified:
                    clase = "IP no especificada"
                elif ip.is_broadcast:
                    clase = "IP de broadcast"
                elif ip.is_reserved:
                    clase = "IP reservada"
                else:
                    clase = "IP pública"
            else:
                clase = "IP desconocida"
        else:
            clase = "IPv6"

        # Colorear partes de la IP en rojo y verde según su clase
        if clase == "IP pública":
            partes = ip_str.split(".")
            red = ".".join(partes[:3])
            host = partes[3]
            colored_ip = f"\033[91m{red}\033[0m.\033[92m{host}\033[0m"
        else:
            colored_ip = ip_str

        print(f"Clase: {clase}")
        print(f"IP coloreada: {colored_ip}")

    except ValueError:
        print("La dirección IP ingresada no es válida.")


if __name__ == "__main__":
    ip_input = input("Ingresa una dirección IP: ")
    colorear_ip(ip_input)
