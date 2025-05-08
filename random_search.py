from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import random
import time
import string
import argparse

def generate_random_search_term(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def random_search(delay=8, max_searches=None, form="QBRE"):
    base_url = "https://www.bing.com/search"
    
    edge_options = Options()
    edge_options.add_argument("start-maximized")
    
    driver = webdriver.Edge(options=edge_options)
    
    search_count = 0
    
    try:
        while max_searches is None or search_count < max_searches:
            search_term = generate_random_search_term()
            
            search_url = f"{base_url}?q={search_term}&form={form}"
            
            search_count += 1
            print(f"Search #{search_count} - Term: {search_term}")
            driver.get(search_url)
            print(f"URL: {driver.current_url}")
            
            if max_searches is not None:
                remaining = max_searches - search_count
                if remaining > 0:
                    print(f"Remaining searches: {remaining}")
                    print(f"Waiting {delay} seconds before next search...")
                else:
                    print("Search limit reached.")
                    break
            else:
                print(f"Waiting {delay} seconds before next search...")
            
            print("-" * 50)
            
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print(f"\nSearch manually stopped.")
    finally:
        print(f"Total searches performed: {search_count}")
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Random Bing search tool with configurable parameters')
    parser.add_argument('--delay', type=int, default=10, help='Delay in seconds between searches (default: 10)')
    parser.add_argument('--count', type=int, default=None, help='Maximum number of searches to perform (default: infinite)')
    parser.add_argument('--form', type=str, default="QBRE", help='Value for the form parameter in the URL (default: QBRE)')
    
    args = parser.parse_args()
    
    count_display = args.count if args.count is not None else "infinite"
    print(f"Starting random search with Edge browser:")
    print(f"- Delay: {args.delay} seconds")
    print(f"- Max searches: {count_display}")
    print(f"- Form parameter: {args.form}")
    print("-" * 50)
    
    random_search(args.delay, args.count, args.form)