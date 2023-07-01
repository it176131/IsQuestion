# IsQuestion
A short tutorial showing how to use `TextCat` with `spaCy` v3 to classify text as a question.

# Background
Recently I was assisting an intern with an NLP project. The goal of the 
project was to topic model conversations between an agent (possibly a 
chatbot) and a user in order to learn what most users talked about.

On first attempt the topic model results weren't very helpful due to a lot 
of noise. I suggested that we attempt to remove some noise 
via classification of sentences. Some sentences may contain a question 
(useful), while others may express emotions or additional details (not immediately 
useful). After doing this the results were quite a bit cleaner.

I've decided to recreate the scenario with Stack Overflow questions. A 
question will contain a body of text. If it's a "good" question it will 
follow [this guide](https://stackoverflow.com/help/how-to-ask), and at [a 
minimum](https://stackoverflow.com/help/quality-standards-error) will 
have the following:
- A clear title.
- A reasonable explanation of what your question is. Add as much detail as 
  you can.
- Any background research you've tried but wasn't enough to solve your problem.
- Correct use of English spelling and grammar to the best of your ability.

If a question follows the guide...
- The title should **summarize the specific problem**.
- The problem should be introduced **before** any code.
  - If code is included it should be a [minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example)
- All relevant tags should be included.

# Goal
I will be identifying the problem a user is trying to solve by classifying 
the title _and_ sentences in the body as `IS_QUESTION` or 
`NOT_QUESTION`.