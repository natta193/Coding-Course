# Example terminal session:
#   mkdir git-practice && cd git-practice
#   git init
#   (create hello.py)
#   git add hello.py
#   git commit -m "First version"
#   (edit hello.py)
#   git diff
#   git commit -am "Print version 2"
#   (break the file on purpose)
#   git restore hello.py
#   git log --oneline
print("Version 2")
