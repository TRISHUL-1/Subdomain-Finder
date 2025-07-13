import dns.resolver
from concurrent.futures import ThreadPoolExecutor

def check_subdomain(subdomain, domain): #checks whether the subdomain exits or not
    
    full_domain = f"{subdomain}.{domain}"   #combines the prefix and sufix to form a working domain

    try:
        answers = dns.resolver.resolve(full_domain, 'A')    #call the resolve method to get the ip address using the A record
        ips = [answer.to_text() for answer in answers]
        print(f"[+] Found: {full_domain} -> {', '.join(ips)}")  #which returns the ip of the domain if it exists or else it gives an error
        return((full_domain,ips))

    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout, dns.resolver.NoNameservers):
        return None

def find_subdomain(domain, wordlist, max_threads=100):

    with open(wordlist, 'r') as file:
        subdomains = [line.strip() for line in file if line.strip()]

        results = []

        try:

            with ThreadPoolExecutor(max_workers=max_threads) as executor:
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
