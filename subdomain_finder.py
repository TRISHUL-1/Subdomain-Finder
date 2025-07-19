import dns.resolver
from concurrent.futures import ThreadPoolExecutor
from domain_info_gather import subdomain_enumeration

        
if __name__ == "__main__":
    
    print("🔍 This is a Subdomain Enumeration Tool")

    enumerator = subdomain_enumeration()

    while(True):

        print("What do you want to do ?")
        print("1. Check the available Subdomain for a particular domain")
        print("2. Find out more info on a particular subdomain")
        choice = int(input(">> "))

        if choice == 1:
            try:
                print("Enter the target domain below")
                print("eg: Exmaple.com")
                print("Or you can type 'exit' to exit out")
                domain = input(">> ")

                if domain.lower() == "exit":
                    exit()

                wordlist = "subdomains1.txt"

                found = [enumerator.find_subdomain(domain, wordlist)]

                print(f"{len(found)} Subdomains found!!")

            except KeyboardInterrupt:
                print("\n[!] Script interrupted.")
                exit()


        elif choice == 2:

                print("Enter the subdomain below")
                subdomain = input(">> ")

                print(f"Subdomain Name: {subdomain}")

                enumerator.check_HTTP(subdomain=subdomain)
                enumerator.check_CNAME(subdomain=subdomain)
                enumerator.check_MX(subdomain=subdomain)
                enumerator.check_TXTrecord(subdomain=subdomain)
            


        else:
            print("Wrong Input!!")
            exit()