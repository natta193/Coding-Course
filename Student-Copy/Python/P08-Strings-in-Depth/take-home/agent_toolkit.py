# TAKE-HOME PROJECT: Secret Agent Toolkit
# After lesson P08 (Strings in Depth) - about 1–2 hours, in chunks over the next few days.
#
# A menu of text-scrambling tools for secret messages – all built with string methods,
# indexing and loops.
#
# Milestones (make each one work before starting the next):
#   [ ] 1. Menu loop with: reverse, Caesar encrypt, Caesar decrypt, remove vowels, "pig
#          latin", quit
#   [ ] 2. Reverse: one line with slicing
#   [ ] 3. Caesar: shift letters by a key, keep capitals as capitals, wrap Z back to A, leave
#          punctuation alone
#   [ ] 4. Pig latin: move each word's first letter to the end and add "ay" ("hello world" →
#          "ellohay orldway")
#   [ ] 5. Check every tool with a few test messages
#
# Stretch: Add a "crack it" tool that prints the message decrypted with all 26 shifts –
# then spot the real one.
#
# Bring it to the next session - working or stuck, both are fine.

def menu():
    print("1) reverse 2) caesar encrypt 3) caesar decrypt 4) no vowels 5) pig latin 6) quit")
