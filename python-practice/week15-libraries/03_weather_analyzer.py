# Week 15: Mini Project - Weather Data Analyzer
# Run: python3 week15-libraries/03_weather_analyzer.py
# Install: pip install requests pandas

import requests
import pandas as pd
from datetime import datetime
from typing import Dict, List, Optional


class WeatherAnalyzer:
    """Analyze weather data from public APIs"""
    
    def __init__(self):
        self.data: List[Dict] = []
    
    def fetch_random_quote(self) -> Optional[str]:
        """Fetch a random quote (demo of API usage)"""
        try:
            response = requests.get("https://api.quotable.io/random", timeout=5)
            response.raise_for_status()
            data = response.json()
            return f'"{data["content"]}" - {data["author"]}'
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching quote: {e}")
            return None
    
    def fetch_github_user(self, username: str) -> Optional[Dict]:
        """Fetch GitHub user information"""
        try:
            url = f"https://api.github.com/users/{username}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            return {
                "username": data["login"],
                "name": data.get("name", "N/A"),
                "public_repos": data["public_repos"],
                "followers": data["followers"],
                "following": data["following"],
                "created_at": data["created_at"]
            }
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"❌ User '{username}' not found")
            else:
                print(f"❌ HTTP Error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Error: {e}")
            return None
    
    def fetch_bitcoin_price(self) -> Optional[Dict]:
        """Fetch current Bitcoin price"""
        try:
            url = "https://api.coindesk.com/v1/bpi/currentprice.json"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            return {
                "USD": data["bpi"]["USD"]["rate"],
                "GBP": data["bpi"]["GBP"]["rate"],
                "EUR": data["bpi"]["EUR"]["rate"],
                "updated": data["time"]["updated"]
            }
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching Bitcoin price: {e}")
            return None
    
    def search_github_repos(self, query: str, max_results: int = 10) -> pd.DataFrame:
        """Search GitHub repositories and return as DataFrame"""
        try:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": max_results
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            repos = []
            for item in data["items"]:
                repos.append({
                    "name": item["name"],
                    "owner": item["owner"]["login"],
                    "stars": item["stargazers_count"],
                    "forks": item["forks_count"],
                    "language": item.get("language", "N/A"),
                    "description": item.get("description", "")[:100]
                })
            
            return pd.DataFrame(repos)
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Error searching repositories: {e}")
            return pd.DataFrame()
    
    def analyze_repos_dataframe(self, df: pd.DataFrame) -> None:
        """Analyze repository DataFrame"""
        if df.empty:
            print("No data to analyze")
            return
        
        print("\n=== Repository Analysis ===")
        print(f"Total repositories: {len(df)}")
        print(f"\nTop 5 by stars:")
        print(df.nlargest(5, "stars")[["name", "stars", "language"]])
        
        print(f"\nLanguage distribution:")
        print(df["language"].value_counts())
        
        print(f"\nStatistics:")
        print(f"  Average stars: {df['stars'].mean():.0f}")
        print(f"  Average forks: {df['forks'].mean():.0f}")
        print(f"  Total stars: {df['stars'].sum():,}")
        print(f"  Most starred: {df.loc[df['stars'].idxmax(), 'name']} ({df['stars'].max():,} stars)")
    
    def create_sample_weather_data(self) -> pd.DataFrame:
        """Create sample weather data for demonstration"""
        data = {
            "date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
            "temperature": [20, 22, 19, 23, 25, 24, 26, 28, 27, 29,
                          30, 28, 26, 25, 24, 23, 22, 21, 20, 19,
                          21, 23, 25, 27, 29, 28, 26, 24, 22, 20],
            "humidity": [65, 70, 68, 72, 75, 73, 78, 80, 77, 82,
                        85, 83, 80, 78, 75, 73, 70, 68, 65, 63,
                        67, 71, 74, 78, 82, 80, 76, 72, 68, 64],
            "rainfall": [0, 0, 5, 0, 0, 2, 0, 0, 0, 3,
                        8, 5, 2, 0, 0, 0, 0, 1, 0, 0,
                        0, 0, 4, 6, 2, 0, 0, 0, 0, 0]
        }
        return pd.DataFrame(data)
    
    def analyze_weather_data(self, df: pd.DataFrame) -> None:
        """Analyze weather DataFrame"""
        print("\n=== Weather Data Analysis ===")
        print(f"Data period: {df['date'].min()} to {df['date'].max()}")
        print(f"Total days: {len(df)}")
        
        print(f"\nTemperature Statistics:")
        print(f"  Average: {df['temperature'].mean():.1f}°C")
        print(f"  Maximum: {df['temperature'].max()}°C on {df.loc[df['temperature'].idxmax(), 'date'].strftime('%Y-%m-%d')}")
        print(f"  Minimum: {df['temperature'].min()}°C on {df.loc[df['temperature'].idxmin(), 'date'].strftime('%Y-%m-%d')}")
        
        print(f"\nHumidity Statistics:")
        print(f"  Average: {df['humidity'].mean():.1f}%")
        print(f"  Maximum: {df['humidity'].max()}%")
        print(f"  Minimum: {df['humidity'].min()}%")
        
        print(f"\nRainfall Statistics:")
        print(f"  Total: {df['rainfall'].sum()}mm")
        print(f"  Average: {df['rainfall'].mean():.1f}mm/day")
        print(f"  Rainy days: {(df['rainfall'] > 0).sum()}")
        print(f"  Dry days: {(df['rainfall'] == 0).sum()}")
        
        # Find patterns
        print(f"\nPatterns:")
        hot_days = df[df['temperature'] > 25]
        print(f"  Hot days (>25°C): {len(hot_days)}")
        
        humid_days = df[df['humidity'] > 75]
        print(f"  Humid days (>75%): {len(humid_days)}")
        
        rainy_days = df[df['rainfall'] > 5]
        print(f"  Heavy rain days (>5mm): {len(rainy_days)}")


def main():
    """Main program"""
    analyzer = WeatherAnalyzer()
    
    print("=" * 60)
    print("  WEATHER & DATA ANALYZER")
    print("=" * 60)
    
    # Demo 1: Random Quote
    print("\n--- Random Quote ---")
    quote = analyzer.fetch_random_quote()
    if quote:
        print(quote)
    
    # Demo 2: GitHub User
    print("\n--- GitHub User Info ---")
    user_info = analyzer.fetch_github_user("torvalds")
    if user_info:
        print(f"Username: {user_info['username']}")
        print(f"Name: {user_info['name']}")
        print(f"Public Repos: {user_info['public_repos']}")
        print(f"Followers: {user_info['followers']}")
        print(f"Following: {user_info['following']}")
    
    # Demo 3: Bitcoin Price
    print("\n--- Bitcoin Price ---")
    btc_price = analyzer.fetch_bitcoin_price()
    if btc_price:
        print(f"USD: ${btc_price['USD']}")
        print(f"EUR: €{btc_price['EUR']}")
        print(f"GBP: £{btc_price['GBP']}")
        print(f"Updated: {btc_price['updated']}")
    
    # Demo 4: GitHub Repository Search
    print("\n--- GitHub Repository Search ---")
    print("Searching for 'python machine learning' repositories...")
    repos_df = analyzer.search_github_repos("python machine learning", max_results=10)
    if not repos_df.empty:
        analyzer.analyze_repos_dataframe(repos_df)
        
        # Save to CSV
        repos_df.to_csv("github_repos.csv", index=False)
        print("\n✅ Saved results to github_repos.csv")
    
    # Demo 5: Weather Data Analysis
    print("\n--- Weather Data Analysis ---")
    weather_df = analyzer.create_sample_weather_data()
    analyzer.analyze_weather_data(weather_df)
    
    # Save weather data
    weather_df.to_csv("weather_data.csv", index=False)
    print("\n✅ Saved weather data to weather_data.csv")
    
    print("\n" + "=" * 60)
    print("  Analysis Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()


# TODO: Add support for fetching real weather data from a weather API
# TODO: Create visualizations of weather trends (requires matplotlib)
# TODO: Add ability to compare multiple GitHub users
# TODO: Implement caching to avoid repeated API calls
# TODO: Add command-line arguments to customize analysis
# TODO: Create a function to export analysis results to PDF


# Useful free APIs for practice:
# - OpenWeatherMap API (requires free API key): https://openweathermap.org/api
# - News API (requires free API key): https://newsapi.org/
# - REST Countries: https://restcountries.com/
# - Dog CEO: https://dog.ceo/dog-api/
# - Cat Facts: https://catfact.ninja/
