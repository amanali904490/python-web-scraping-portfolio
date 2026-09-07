from playwright.sync_api import sync_playwright
import requests
import os

def scrape_images():
    # Folder banao images save karne ke liye
    if not os.path.exists("ai_dataset"):
        os.makedirs("ai_dataset")

    with sync_playwright() as p:
        # Browser open karo (headless=False taaki tum dekh sako kya ho raha hai)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Target website par jao
        print("Website khul rahi hai...")
        page.goto("https://unsplash.com/s/photos/fashion-model")

        # Thoda scroll karna taaki images load ho jayein
        page.mouse.wheel(0, 2000)
        page.wait_for_timeout(3000) # 3 second wait

        # Images ke links nikalna
        print("Images dhundh rahe hain...")
        images = page.locator("img").all()

        count = 1
        for img in images:
            if count > 5: # Sirf top 5 images demo ke liye
                break
                
            src = img.get_attribute("src")
            
            # Faltu chhote icons ko ignore karne ke liye basic check
            if src and "images.unsplash.com" in src:
                print(f"Downloading Image {count}...")
                img_data = requests.get(src).content
                with open(f"ai_dataset/model_{count}.jpg", 'wb') as handler:
                    handler.write(img_data)
                count += 1

        print("Done! Apna 'ai_dataset' folder check karo.")
        browser.close()

scrape_images()