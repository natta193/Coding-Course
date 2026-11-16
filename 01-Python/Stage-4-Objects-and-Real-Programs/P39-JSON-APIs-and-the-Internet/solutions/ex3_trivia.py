import html
import random
import requests

r = requests.get("https://opentdb.com/api.php", params={"amount": 10, "type": "multiple"}, timeout=10)
r.raise_for_status()
questions = r.json()["results"]
score = 0
for i, q in enumerate(questions, 1):
    answers = [html.unescape(a) for a in q["incorrect_answers"]] + [html.unescape(q["correct_answer"])]
    random.shuffle(answers)
    print(f"\nQ{i} ({q['category']}): {html.unescape(q['question'])}")
    for letter, a in zip("ABCD", answers):
        print(f"  {letter}) {a}")
    choice = input("Answer: ").strip().upper()
    while choice not in ["A", "B", "C", "D"]:
        choice = input("A, B, C or D: ").strip().upper()
    if answers["ABCD".index(choice)] == html.unescape(q["correct_answer"]):
        print("Correct!")
        score += 1
    else:
        print("Wrong – it was", html.unescape(q["correct_answer"]))
print(f"\nYou scored {score}/10")
