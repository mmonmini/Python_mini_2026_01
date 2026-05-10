from requests import get

movie_ids = [
    238, 680, 550, 185, 641, 515042,
    152532, 120467, 872585, 906126, 840430
]

movie_details = {}

url = "https://nomad-movies.nomadcoders.workers.dev/movies/"

for movie_id in movie_ids:
    movie_url = f"{url}{movie_id}"
    response = get(movie_url)

    if response.status_code == 404:
        print(f"{movie_id}번 영화는 API에 없습니다.")
        print("=" * 50)
        continue

    data = response.json()
    movie_details[movie_id] = data

    print("title:", data["title"])
    print("overview:", data["overview"])
    print("vote_average:", data["vote_average"])
    print("=" * 50)
