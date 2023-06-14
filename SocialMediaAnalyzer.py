import requests

class SocialMediaAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key

    def analyze_user(self, username):
        url = f"https://api.socialmedia.com/v1/user/{username}/analysis"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            if "followers" in data:
                followers = data["followers"]
                following = data["following"]
                posts = data["posts"]

                print(f"Social Media Analysis for User: {username}")
                print(f"- Followers: {followers}")
                print(f"- Following: {following}")
                print(f"- Posts: {posts}")
            else:
                print(f"No social media analysis found for user: {username}.")
        else:
            print("Unable to retrieve social media analysis.")

def main():
    api_key = "YOUR_API_KEY"
    username = "example_user"

    analyzer = SocialMediaAnalyzer(api_key)
    analyzer.analyze_user(username)

if __name__ == "__main__":
    main()
