"""
IOC Tracker CLI - Main Entry Point
"""

from database_setup import setup_database
from database import add_ioc, get_all_iocs, search_iocs

def display_menu():
  print("""===IOC Tracker CLI===
  
  Add new IOC
  View all IOCs
  Search IOCs
  Exit""")
  
def prompt_add():
    ioc_type = input("Enter IOC type (IP, Domain, Hash): ").strip()
    value = input("Enter IOC value: ").strip()    
    source = input("Enter source: ").strip()
    add_ioc(ioc_type, value, source)

def prompt_view():
    iocs = get_all_iocs()
    if not iocs:
        print("No IOCs found.")
        return
    print(f"\nFound {len(iocs)} IOCs:\n")
    for i in iocs:
            _id, ioc_type, value, first_seen, source = i
            print(f"{_id}. {ioc_type}: {value} (First seen: {first_seen}, Source: {source})")    

def prompt_search():
    term = input("Enter search query: ").strip()
    results = search_iocs(term)
    if not results:
        print("No IOCs found.")
        return
    print(f"{len(results)} match(es):\n")
    for r in results: 
        _id, ioc_type, value, first_seen, source = r
        print(f"{_id}. {ioc_type}: {value} (First seen: {first_seen}, Source: {source})")

def main():
    setup_database()
    while True:
        display_menu()
        choice = input("Choice (1-4): ").strip()
        if choice == "1":
            prompt_add()
        elif choice == "2":
            prompt_view()
        elif choice == "3":
            prompt_search()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        if __name__ == "__main__":
            main() 