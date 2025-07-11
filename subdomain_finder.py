import socket

def find_subdomain(domain, wordlist):
    found = []
    with open(wordlist, 'r') as file:
        for line in file:
            subdomain = line.strip() + '.' + domain

            try:
                ip = socket.gethostbyname(subdomain)
                print(f"[+] Found: {subdomain} -> {ip}")
                found.append((subdomain,ip))

            except socket.gaierror:
                pass

    print(f"{len(found)} subdomains discovered")


if __name__ == "__main__":
    print("Enter the target domain below")
    print("eg: Exmaple.com")
    domain = input(">> ")

    wordlist = "subdomains-top1million-110000.txt"

    find_subdomain(domain, wordlist)

