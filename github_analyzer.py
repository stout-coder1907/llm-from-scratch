import requests

username = "stout-coder1907"

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(type(data))
print(len(data))
print(data[0])

for repo in data:
    print(repo["name"])
for repo in data:
    print("Name:", repo["name"])
    print("Stars:", repo["stargazers_count"])
    print("Forks:", repo["forks_count"])
    print("Language:", repo["language"])
    print()

repos = []

for repo in data:
    repos.append({
        "name": repo["name"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "language": repo["language"]
    })

for repo in repos:
    print(repo)


import pandas as pd

df = pd.DataFrame(repos)

print(df)

print("\nRepositories with most stars:")

sorted_df = df.sort_values("stars", ascending=False)

print(sorted_df)

df.to_csv("github_report.csv", index=False)

print("Report saved successfully!")