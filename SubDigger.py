import requests
import random
import string

def generate_wordlist(target_website, num_common_subdomains, num_random_words):
    wordlist = []

    # Generate wordlist with common subdomains
    common_subdomains = generate_common_subdomains(num_common_subdomains)
    for subdomain in common_subdomains:
        potential_subdomain = f"{subdomain}.{target_website}"
        url = f"http://{potential_subdomain}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Valid subdomain: {potential_subdomain}")
                wordlist.append(potential_subdomain)
        except requests.ConnectionError:
            print(f"Error connecting to: {potential_subdomain}")

    # Generate wordlist with random strings
    for _ in range(num_random_words):
        random_subdomain = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        potential_subdomain = f"{random_subdomain}.{target_website}"
        wordlist.append(potential_subdomain)

    return wordlist

def generate_common_subdomains(num_common_subdomains):
    common_subdomains = [
        "mail", "blog", "admin", "test", "dev", "shop", "forum",
        "info", "news", "login", "api", "support", "help", "store", "portal",
        "app", "web", "cdn", "static", "secure", "download", "members", "images"
    ]
    # Add additional common subdomains if needed
    additional_subdomains = [
        "email", "forum", "news", "shop", "store", "blog", "forum", "portal",
        "members", "gallery", "events", "calendar", "chat", "stats", "billing"
    ]
    num_additional_subdomains = max(num_common_subdomains - len(common_subdomains), 0)
    common_subdomains.extend(random.sample(additional_subdomains, k=num_additional_subdomains))
    return common_subdomains

def main():
    print("""
    █████████             █████     ██████████    ███                                      
 ███░░░░░███           ░░███     ░░███░░░░███  ░░░                                       
░███    ░░░  █████ ████ ░███████  ░███   ░░███ ████   ███████  ███████  ██████  ████████ 
░░█████████ ░░███ ░███  ░███░░███ ░███    ░███░░███  ███░░███ ███░░███ ███░░███░░███░░███
 ░░░░░░░░███ ░███ ░███  ░███ ░███ ░███    ░███ ░███ ░███ ░███░███ ░███░███████  ░███ ░░░ 
 ███    ░███ ░███ ░███  ░███ ░███ ░███    ███  ░███ ░███ ░███░███ ░███░███░░░   ░███     
░░█████████  ░░████████ ████████  ██████████   █████░░███████░░███████░░██████  █████    
 ░░░░░░░░░    ░░░░░░░░ ░░░░░░░░  ░░░░░░░░░░   ░░░░░  ░░░░░███ ░░░░░███ ░░░░░░  ░░░░░     
                                                     ███ ░███ ███ ░███                   
                                                    ░░██████ ░░██████                    
                                                     ░░░░░░   ░░░░░░     by HowToHack1337                """)

    target_website = input("\n Enter the target website (e.g., example.com): ").strip().lower()
    
    num_common_subdomains = int(input("Enter the number of common subdomains to generate (0 for none): "))
    num_random_words = int(input("Enter the number of random words to generate (0 for none): "))

    if num_common_subdomains < 0 or num_random_words < 0:
        print("Error: Number of subdomains/words cannot be negative.")
        return

    wordlist = generate_wordlist(target_website, num_common_subdomains, num_random_words)

    if wordlist:
        with open("subdomain_wordlist.txt", "w") as f:
            f.write("\n".join(wordlist))
        print("Wordlist saved to subdomain_wordlist.txt")
    else:
        print("No valid subdomains found.")

if __name__ == "__main__":
    main()
