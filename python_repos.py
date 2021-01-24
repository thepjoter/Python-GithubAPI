# Czesc graficzna projektu jest w pliku python_repos_visual.py
# Zachęcam do sprawdzenia :)

import requests

# Wykonanie wywołania api i zachowanie odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Account': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

# Umiszczenie odpowiedzi API w zmienej
response_dict = r.json()
print(f"Całkowita liczba zwróconych repozytoriów: {response_dict['total_count']}")

# Przetworzenie informacji o repozytoriach
repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytoriów: {len(repo_dicts)}")

print('\nWybrane informacje o każdym repozytorium:')
for repo_dict in repo_dicts:
    print(f"\nNazwa: {repo_dict['name']}")
    print(f"Właściciel: {repo_dict['owner']['login']}")
    print(f"Gwiazdki: {repo_dict['stargazers_count']}")
    print(f"Repozytorium {repo_dict['html_url']}")
    print(f"Opis: {repo_dict['description']}")

# Przeanalizowanie pierwszego repozytorium
repo_dict = repo_dicts[0]
print(f"\nWybrane informacje o pierwszym repozytorium:")
print(f"Nazwa: {repo_dict['name']}")
print(f"Właściciel: {repo_dict['owner']['login']}")
print(f"Gwiazdki: {repo_dict['stargazers_count']}")
print(f"Repozytorium {repo_dict['html_url']}")
print(f"Utworzone: {repo_dict['created_at']}")
print(f"Uaktualnione: {repo_dict['updated_at']}")
print(f"Opis: {repo_dict['description']}")

