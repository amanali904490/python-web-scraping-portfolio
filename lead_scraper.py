import requests
from bs4 import BeautifulSoup
import csv

def scrape_leads():
    print("Website se data nikal rahe hain...")
    # Yeh ek practice website hai jahan countries ka structured data hai
    url = "https://www.scrapethissite.com/pages/simple/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 1. Ek nayi CSV (Excel) file create karna
    with open('business_leads.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # 2. File ke andar Headers (Columns ke naam) likhna
        writer.writerow(['Lead Name', 'Location', 'Size/Population'])

        # 3. HTML se saara data dhundhna
        boxes = soup.find_all('div', class_='country')

        count = 1
        for box in boxes:
            if count > 15: # Demo ke liye sirf top 15 leads nikal rahe hain
                break
            
            # Text ko clean karne ke liye .strip() use karte hain
            name = box.find('h3', class_='country-name').text.strip()
            location = box.find('span', class_='country-capital').text.strip()
            size = box.find('span', class_='country-population').text.strip()

            # 4. Data ko CSV file me row-by-row save karna
            writer.writerow([name, location, size])
            print(f"Saved Lead {count}: {name}")
            
            count += 1

    print("\nSuccess! Apne VS Code me 'business_leads.csv' file check karo.")

scrape_leads()