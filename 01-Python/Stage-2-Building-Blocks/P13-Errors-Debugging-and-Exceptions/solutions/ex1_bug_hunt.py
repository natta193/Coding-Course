def get_scores():                      # 1 SYNTAX: missing colon
    scores = []
    for i in range(1, 6):               # 2 LOGIC: range(1, 5) only asked 4 times
        s = int(input(f"Score {i}: "))  # 3 RUNTIME: strings can't be added (TypeError)
        scores.append(s)
    return scores

def average(nums):
    total = 0
    for n in nums:
        total += n                      # 4 LOGIC: =+ sets total to +n
    return total / len(nums)

def grade(avg):
    if avg >= 80:                       # 5 LOGIC: check the higher band first
        return "Distinction"
    elif avg >= 50:
        return "Pass"
    else:
        return "Fail"

scores = get_scores()
avg = average(scores)
print(f"Average: {avg:.1f}")
print("Highest:", max(scores))          # 6 RUNTIME: NameError, 'score' typo
print("Grade:", grade(avg))
