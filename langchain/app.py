
import streamlit as st
import requests
import pandas as pd

st.title("🐙 GitHub Stats Analyzer")

st.write("Enter a GitHub profile URL to analyze the repositories.")

github_url = st.text_input(
    "GitHub Profile URL",
    placeholder="https://github.com/username"
)


def get_username(url):
    url = url.rstrip("/")
    username = url.split("/")[-1]
    return username


if st.button("Analyze"):

    username = get_username(github_url)

    st.write("GitHub Username:", username)

    # GitHub API
    api_url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(api_url)

    if response.status_code == 200:

        data = response.json()

        repos = []

        for repo in data:
            repos.append({
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "language": repo["language"]
            })

        # Convert to Pandas DataFrame
        df = pd.DataFrame(repos)

        st.subheader("Repositories")

        st.dataframe(df)

    else:
        st.error("GitHub user not found.")
