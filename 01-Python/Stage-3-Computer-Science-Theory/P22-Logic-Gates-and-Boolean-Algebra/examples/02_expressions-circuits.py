# Alarm sounds (Q) if the door is open (D)
# AND the alarm is set (S), OR if panic (P)
# Q = (D AND S) OR P

def alarm(d, s, p):
    return (d and s) or p

for d in [False, True]:
    for s in [False, True]:
        for p in [False, True]:
            print(int(d), int(s), int(p), int(alarm(d, s, p)))
