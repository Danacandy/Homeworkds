import requests


def search_gifs(search_word):
    api_key = "ZnTcfwZj2QH12PYQMKdp4keQVUhBjmtA"
    endpoint = f"https://api.giphy.com/v1/gifs/search"
    params = {
        "api_key": api_key,
        "q": search_word,
        "limit": 5  
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    gif_links = [gif["images"]["fixed_height"]["url"] for gif in data["data"]]
    return gif_links


def main():
    search_word = input("Enter a search word for GIFs: ")
    gif_links = search_gifs(search_word)

    if gif_links:
        print("GIF Links:")
        for link in gif_links:
            print(link)
    else:
        print("No GIFs found for the search word.")


if __name__ == "__main__":
    main()