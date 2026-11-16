def get_scores()
    scores = []
    for i in range(1, 5):
        s = input(f"Score {i}: ")
        scores.append(s)
    return scores

def average(nums):
    total = 0
    for n in nums:
        total =+ n
    return total / len(nums)

def grade(avg):
    if avg >= 50:
        return "Pass"
    elif avg >= 80:
        return "Distinction"
    else:
        return "Fail"

scores = get_scores()
avg = average(scores)
print(f"Average: {avg:.1f}")
print("Highest:", max(score))
print("Grade:", grade(avg))
