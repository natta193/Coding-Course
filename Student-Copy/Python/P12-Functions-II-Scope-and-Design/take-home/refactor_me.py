# TAKE-HOME PROJECT: Refactor the Mess
# After lesson P12 (Functions II – Scope and Design) - about 1–2 hours, in chunks over the next few days.
#
# Professional programmers spend loads of time cleaning up old code. The starter file is a
# working but horribly messy times-table quiz. Your job: make it clean WITHOUT changing
# what it does.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Run it first and play it, so you know exactly what it does
#   [ ] 2. Split it into functions: ask_question(), get_number(), play_round(),
#          show_results(), main()
#   [ ] 3. No global variables – pass values in and return them out
#   [ ] 4. Give everything a good name and a docstring; delete the copy-pasted code
#   [ ] 5. Add if __name__ == "__main__": main() – and check it still plays exactly the same
#
# Stretch: Add a difficulty setting and a "practise your weakest table" mode – easy now
# that the code is clean!
#
# Bring it to the next session - working or stuck, both are fine.

import random
s=0
w=[]
n=int(input("how many questions? "))
for i in range(n):
    a=random.randint(2,12)
    b=random.randint(2,12)
    x=input(str(a)+" x "+str(b)+" = ")
    while not x.isdigit():
        print("numbers only")
        x=input(str(a)+" x "+str(b)+" = ")
    if int(x)==a*b:
        s=s+1
        print("correct")
    else:
        print("wrong it was "+str(a*b))
        w.append(str(a)+"x"+str(b))
print("you got "+str(s)+" out of "+str(n))
if s==n:
    print("perfect!!!")
elif s>n/2:
    print("good")
else:
    print("keep practising")
if len(w)>0:
    print("practise these:")
    for q in w:
        print(q)
