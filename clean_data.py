import pandas as pd

from is_question.utils import clean_text


df = pd.read_csv(
    "./data/raw.csv",
    index_col="question_id",
    usecols=["question_id", "title", "body", "link"],
)
df["body"] = df["body"].transform(clean_text)
df.to_csv("./data/clean.csv")
