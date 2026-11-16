score = 0                  # global

def show():
    print(score)           # reading a global: fine

def add_points():
    global score           # needed to CHANGE it
    score += 10

add_points()
show()                     # 10
