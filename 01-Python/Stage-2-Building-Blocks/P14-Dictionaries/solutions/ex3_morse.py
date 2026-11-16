MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
}
REVERSE = {code: letter for letter, code in MORSE.items()}

def to_morse(text):
    words = []
    for word in text.upper().split():
        words.append(" ".join(MORSE[ch] for ch in word if ch in MORSE))
    return " / ".join(words)

def from_morse(code):
    words = []
    for word in code.split(" / "):
        words.append("".join(REVERSE.get(sym, "?") for sym in word.split()))
    return " ".join(words)

encoded = to_morse("Hello world 2026")
print(encoded)
print(from_morse(encoded))
