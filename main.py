import requests

try:
    # Read the file and use a set comprehension to remove duplicates and blank lines
    with open("urls.txt", "r") as file:
        urls = {url.strip() for url in file if url.strip()}
except FileNotFoundError:
    print("ERROR: 'urls.txt' file not found. Please create it first.")
    exit()

print(f"Checking {len(urls)} unique URLs...\n")

for url in urls:
    # Ensure the URL has a proper protocol scheme to prevent requests from crashing
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        # Send a single GET request with a 5-second timeout
        response = requests.get(url, timeout=5)
        print(f"[{response.status_code}] -> {url}")
    except requests.exceptions.RequestException as e:
        # Catch any connection errors, timeouts, or broken links safely
        print(f"[ERROR] -> {url} | Details: {type(e).__name__}")
