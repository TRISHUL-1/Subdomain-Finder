import socket
from concurrent.futures import ThreadPoolExecutor

def check_subdomain(subdomain, domain): #checks whether the subdomain exits or not
    
    full_domain = f"{subdomain}.{domain}"   #combines the prefix and sufix to form a working domain

    try:
        ip = socket.gethostbyname(full_domain)  #calls the gethostbyname method for the socket module
        print(f"[+] Found: {full_domain} -> {ip}")  #which returns the ip of the domain if it exists or else it gives an error
        return((full_domain,ip))

    except socket.gaierror:
        return None

def find_subdomain(domain, wordlist):

    with open(wordlist, 'r') as file:
        subdomains = [line.strip() for line in file]

        results = []

        try:

            with ThreadPoolExecutor(max_workers=30) as executor:
                futures = [executor.submit(check_subdomain, subdomain, domain) for subdomain in subdomains]

                for future in futures:
                    result = future.result()

                    if result:
                        results.append(result)

        except KeyboardInterrupt:
            print("\nInterrupted by the user. Stopping...")
            executor.shutdown(wait=False, cancel_futures=True)
        
    return results

        
if __name__ == "__main__":
    
    try:
        print("Enter the target domain below")
        print("eg: Exmaple.com")
        domain = input(">> ")

        wordlist = "subdomains-top1million-110000.txt"

        found = [find_subdomain(domain, wordlist)]

        print(f"{len(found)} Subdomains found!!")

    except KeyboardInterrupt:
        print("\n[!] Script interrupted.")
