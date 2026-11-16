SMILEY = [
    "00111100",
    "01000010",
    "10100101",
    "10000001",
    "10100101",
    "10011001",
    "01000010",
    "00111100",
]

def nice_size(bits):
    size = bits / 8
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1000:
            return f"{size:.1f} {unit}"
        size /= 1000
    return f"{size:.1f} TB"

def image_size(width, height, colour_depth):
    return nice_size(width * height * colour_depth)

def sound_size(sample_rate, bit_depth, seconds, channels=2):
    return nice_size(sample_rate * bit_depth * seconds * channels)

print("4K photo:", image_size(3840, 2160, 24))
print("3-min song:", sound_size(44100, 16, 180))

for row in SMILEY:
    print("".join("██" if b == "1" else "  " for b in row))
