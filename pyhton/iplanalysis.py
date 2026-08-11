import pandas as pd
from pandasai import SmartDataframe
from panadasai.llm.openai import OpenAI

llm = OpenAI(api_token="YOUR_OPENAI_API_KEY")
df = pd.read_csv("ipl.csv")

df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.head()

sdf = SmartDataframe(df, config={"llm":llm})

sdf.chat("which players were the most expensive")

sdf.chat("Which players were the cheapest buys this season and which teams bought them?")

sdf.chat(
    "Draw a bar graph showing how much money was spent by each team this season overall."
)

sdf.chat(
    "How many players remained unsold this season?"
)

sdf.chat(
    "Which three new players were picked by Gujarat Titans?"
)

sdf.chat(
    "Draw a bar plot showing how much money Mumbai Indians spent on each type of player."
)

sdf.chat(
    "Perform univariate analysis on the dataset."
)