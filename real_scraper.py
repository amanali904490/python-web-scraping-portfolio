import requests
from bs4 import BeautifulSoup
import csv

def scrape_tech_news():
    print("Hacker News se real data nikal rahe hain...")
    
    # Real website URL
    url = "https://news.ycombinator.com/"
    
    # TRICK: Website ko lagna chahiye ki hum Chrome browser se aaye hain, bot nahi
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    # Request me headers bhej rahe hain
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Nayi CSV file create karna
    with open('tech_news.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Headers set karna
        writer.writerow(['Article Title', 'Link'])

        # Hacker News par articles 'titleline' naam ki class ke andar hote hain
        articles = soup.find_all('span', class_='titleline')

        count = 1
        for article in articles:
            if count > 20: # Top 20 news nikalte hain
                break
            
            # 'a' tag (link tag) dhundhna
            a_tag = article.find('a')
            
            # Title aur Link alag alag nikalna
            title = a_tag.text.strip()
            link = a_tag['href']
            
            # CSV me row save karna
            writer.writerow([title, link])
            print(f"Saved {count}: {title}")
            
            count += 1

    print("\nDone! VS Code me 'tech_news.csv' file check karo.")

scrape_tech_news()