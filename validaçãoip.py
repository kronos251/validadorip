import re

print("validaçãoip")

def is_valid_ip(ip):
    pattern = re.compile(
        r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\."
        r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$"
    )
    return pattern.match(ip) is not None


def main():
    ips_validos = []
    ips_invalidos = []
    with open('ips.txt','r') as archive:
        ips = archive.readlines()

    for ip in ips:
        ip = ip.strip()
        if is_valid_ip(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

    print(f"validos : {ips_validos}")
    print(f"invalidos : {ips_invalidos}")




if __name__ == '__main__':
   main()





            
    

