import pandas as pd
import spacy


df = pd.read_csv("./data/clean.csv", index_col="question_id")
nlp = spacy.load(
    name="en_core_web_sm",
)
nlp.add_pipe("sentencizer")

texts = df["body"].to_numpy()
docs = nlp.pipe(texts)

doc = next(docs)
print(*[sent.text.strip() for sent in doc.sents], sep="\n"+"-"*30+"\n")
