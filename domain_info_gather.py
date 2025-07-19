import dns.resolver
import requests
import tldextract
from concurrent.futures import ThreadPoolExecutor


class subdomain_enumeration:

    def __init__(self):
        pass


    def get_root_domain(self, subdomain):
        
        extract = tldextract.extract(subdomain)
        return f"{extract.domain}.{extract.suffix}"


    def check_subdomain(self, subdomain, domain): #checks whether the subdomain exits or not
    
        full_domain = f"{subdomain}.{domain}"   #combines the prefix and sufix to form a working domain

        try:
            answers = dns.resolver.resolve(full_domain, 'A')    #call the resolve method to get the ip address using the A record
            ips = [answer.to_text() for answer in answers]
            print(f"[+] Found: {full_domain} -> {', '.join(ips)}")  #which returns the ip of the domain if it exists or else it gives an error
            return((full_domain,ips))

        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.LifetimeTimeout, dns.resolver.NoNameservers):
            return None

    def find_subdomain(self, domain, wordlist, max_threads=100):

        with open(wordlist, 'r') as file:
            subdomains = [line.strip() for line in file if line.strip()]

            results = []

            try:

                with ThreadPoolExecutor(max_workers=max_threads) as executor:
                    futures = [executor.submit(self.check_subdomain, subdomain, domain) for subdomain in subdomains]

                    for future in futures:
                        result = future.result()

                        if result:
                            results.append(result)

            except KeyboardInterrupt:
                print("\nInterrupted by the user. Stopping...")
                executor.shutdown(wait=False, cancel_futures=True)
            
        return results


    def check_HTTP(self, subdomain):

        url = f"https://{subdomain}"
        headers = {'User-Agent': 'Mozilla/5.0'}

        try:
            response = requests.get(url, headers=headers, timeout=5)
            print(f"[{response.status_code}] {subdomain} - {response.reason}")
        except requests.exceptions.RequestException as e:
            print(f"[-] HTTP request failed for {subdomain}: {e}")


    def check_CNAME(self, subdomain):

        try:
            answers = dns.resolver.resolve(subdomain, "CNAME")
            for rdata in answers:
                print(f"CNAME points to: {rdata.target}")
        except dns.resolver.NoAnswer:
            print(f"[!] No CNAME record found for {subdomain}")
        except dns.resolver.NXDOMAIN:
            print(f"[!] {subdomain} does not exist")
        except dns.resolver.Timeout:
            print(f"[!] Timeout while resolving {subdomain}")
        except dns.resolver.NoNameservers:
            print(f"[!] No nameservers available for {subdomain}")
        except Exception as e:
            print(f"[!] Unexpected error: {e}")


    def check_MX(self, subdomain):
        
        root_domain = self.get_root_domain(subdomain=subdomain)

        answers = dns.resolver.resolve(root_domain, "MX")
        for rdata in answers:
            print(f"Mail Server: {rdata.exchange}")

    def check_TXTrecord(self, subdomain):

        root_domain = self.get_root_domain(subdomain=subdomain)
        answers = dns.resolver.resolve(root_domain, "TXT")
        for rdata in answers:
            print(f"TXT: {rdata.to_text()}")
