import requests
import csv
import time

API_KEY = "724c6d47814741b1e62730e7bdb9e386637c0aba6eca93a29e93ef98ae9d1de7"  

# User input
first_name = input("Enter First Name (or press Enter to skip): ").strip()
last_name = input("Enter Last Name (or press Enter to skip): ").strip()
city = input("Enter City (or press Enter to skip): ").strip()
dob = input("Enter Date of Birth (YYYY or MM/DD/YYYY, or press Enter to skip): ").strip()

search_terms = []

if first_name and last_name:
    search_terms.append(f'"{first_name} {last_name}"')
elif first_name:
    search_terms.append(f'"{first_name}"')
elif last_name:
    search_terms.append(f'"{last_name}"')

if city:
    search_terms.append(f'"{city}"')
if dob:
    search_terms.append(f'"{dob}"')

search_query = (
    " ".join(search_terms) + 
    " filetype:pdf OR filetype:doc OR filetype:docx OR filetype:xls OR filetype:xlsx "
    "OR filetype:ppt OR filetype:pptx OR filetype:rtf OR filetype:csv OR filetype:json "
    "OR filetype:xml OR filetype:sql OR filetype:txt OR filetype:log OR filetype:ini "
    "OR filetype:cfg OR filetype:pwd OR filetype:bak OR filetype:old OR filetype:backup OR filetype:env "
    "OR filetype:jpg OR filetype:jpeg OR filetype:png OR filetype:gif OR filetype:tiff "
    "OR filetype:svg OR filetype:bmp OR filetype:mp3 OR filetype:wav OR filetype:mp4 "
    "OR filetype:avi OR filetype:mkv OR filetype:mov OR filetype:flv OR filetype:psd "
    "OR filetype:ai OR filetype:eps OR filetype:raw OR filetype:heif OR filetype:ico "
)

params = {
    "q": search_query,
    "engine": "google",
    "api_key": API_KEY
}


#this part i had my bff chatpt make for me
# API Request with error handling
try:
    response = requests.get("https://serpapi.com/search", params=params)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"❌ API Request Failed: {e}")
    exit()

results = []
for result in data.get("organic_results", []):
    title = result.get("title", "No Title")
    link = result.get("link", "No Link")
    snippet = result.get("snippet", "No Description")
    results.append([title, link, snippet])

csv_filename = "search_results.csv"

# Append to CSV instead of overwriting
with open(csv_filename, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(["Title", "Link", "Description"])
    writer.writerows(results)

# Output results
if results:
    print(f"\n {len(results)} Results Found! Saved to {csv_filename}")
    for res in results:
        print(f"\n🔹 {res[0]}\n🔗 {res[1]}\n📄 {res[2]}")
else:
    print("\n No documents found. Try different search filters.")

# Rate limit management to avoid excessive API usage
time.sleep(2)  # Adding a delay before any potential next request
