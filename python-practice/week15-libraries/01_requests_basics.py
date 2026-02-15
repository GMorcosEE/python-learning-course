# Week 15: External Libraries - HTTP Requests
# Run: python3 week15-libraries/01_requests_basics.py
# Install: pip install requests

import requests
import json


print("=== HTTP Requests with requests library ===\n")

# Basic GET request
print("--- Basic GET Request ---")
response = requests.get("https://api.github.com")
print(f"Status Code: {response.status_code}")
print(f"Content Type: {response.headers['Content-Type']}")
print(f"Response length: {len(response.text)} characters\n")


# GET request with JSON response
print("--- JSON Response ---")
response = requests.get("https://api.github.com/users/github")
if response.status_code == 200:
    data = response.json()  # Parse JSON automatically
    print(f"Username: {data['login']}")
    print(f"Name: {data['name']}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}\n")
else:
    print(f"Error: {response.status_code}\n")


# GET request with parameters
print("--- GET with Parameters ---")
params = {
    "q": "python",
    "sort": "stars",
    "order": "desc",
    "per_page": 5
}
response = requests.get("https://api.github.com/search/repositories", params=params)
if response.status_code == 200:
    data = response.json()
    print(f"Total repositories found: {data['total_count']}")
    print("\nTop 5 Python repositories:")
    for i, repo in enumerate(data['items'][:5], 1):
        print(f"{i}. {repo['name']} - ⭐ {repo['stargazers_count']}")
    print()
else:
    print(f"Error: {response.status_code}\n")


# Error handling
print("--- Error Handling ---")
try:
    response = requests.get("https://api.github.com/users/nonexistentuser12345xyz")
    response.raise_for_status()  # Raises exception for 4xx/5xx status codes
    print("User found")
except requests.exceptions.HTTPError as e:
    print(f"❌ HTTP Error: {e}")
except requests.exceptions.ConnectionError:
    print("❌ Connection Error: Could not connect to server")
except requests.exceptions.Timeout:
    print("❌ Timeout Error: Request took too long")
except requests.exceptions.RequestException as e:
    print(f"❌ Request Error: {e}")
print()


# POST request (example with JSONPlaceholder - a fake API for testing)
print("--- POST Request ---")
new_post = {
    "title": "My First Post",
    "body": "This is the content of my post",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
if response.status_code == 201:  # 201 = Created
    data = response.json()
    print(f"✅ Post created with ID: {data['id']}")
    print(f"Title: {data['title']}\n")
else:
    print(f"Error: {response.status_code}\n")


# Headers
print("--- Custom Headers ---")
headers = {
    "User-Agent": "Python Learning Course",
    "Accept": "application/json"
}
response = requests.get("https://api.github.com", headers=headers)
print(f"Request sent with custom User-Agent")
print(f"Status: {response.status_code}\n")


# Timeout
print("--- Timeout ---")
try:
    response = requests.get("https://api.github.com", timeout=5)  # 5 second timeout
    print(f"✅ Request completed in time")
except requests.exceptions.Timeout:
    print("❌ Request timed out")
print()


# Session - reuse connection
print("--- Using Session ---")
with requests.Session() as session:
    session.headers.update({"User-Agent": "Python Course"})
    
    # Multiple requests with same session
    response1 = session.get("https://api.github.com")
    response2 = session.get("https://api.github.com/users/github")
    
    print(f"Request 1: {response1.status_code}")
    print(f"Request 2: {response2.status_code}")
    print("✅ Session maintains connection and headers\n")


# Download file
print("--- Download File ---")
url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"
response = requests.get(url)
if response.status_code == 200:
    with open("downloaded_gitignore.txt", "w") as f:
        f.write(response.text)
    print(f"✅ Downloaded file ({len(response.text)} bytes)")
    print(f"First 100 characters: {response.text[:100]}...\n")


# Practical example: Weather-like API
print("--- Practical Example: Public API ---")
# Using a free public API (no key required)
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if response.status_code == 200:
    data = response.json()
    print("Bitcoin Price Index:")
    for currency, info in data['bpi'].items():
        print(f"  {currency}: {info['rate']}")
print()


# TODO: Fetch data from a public API of your choice (weather, quotes, etc.)
# TODO: Create a function that searches GitHub repositories by topic
# TODO: Build a simple API client class with error handling
# TODO: Download and save an image from a URL
# TODO: Create a function that checks if a website is online (status 200)


# Useful public APIs for practice (no key required):
# - https://api.github.com - GitHub API
# - https://jsonplaceholder.typicode.com - Fake REST API for testing
# - https://api.coindesk.com/v1/bpi/currentprice.json - Bitcoin prices
# - https://dog.ceo/api/breeds/image/random - Random dog images
# - https://api.quotable.io/random - Random quotes
# - https://api.agify.io?name=michael - Predict age from name
