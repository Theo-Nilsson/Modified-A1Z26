alphabet_index = {
    "A": "1",
    "B": "2",
    "C": "3",
    "D": "4",
    "E": "5",
    "F": "6",
    "G": "7",
    "H": "8",
    "I": "9",
    "J": "10",
    "K": "11",
    "L": "12",
    "M": "13",
    "N": "14",
    "O": "15",
    "P": "16",
    "Q": "17",
    "R": "18",
    "S": "19",
    "T": "20",
    "U": "21",
    "V": "22",
    "W": "23",
    "X": "24",
    "Y": "25",
    "Z": "26",
    " ": "27"  # Use "27" to represent a space
}

index_alphabet = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G",
    "8": "H",
    "9": "I",
    "10": "J",
    "11": "K",
    "12": "L",
    "13": "M",
    "14": "N",
    "15": "O",
    "16": "P",
    "17": "Q",
    "18": "R",
    "19": "S",
    "20": "T",
    "21": "U",
    "22": "V",
    "23": "W",
    "24": "X",
    "25": "Y",
    "26": "Z",
    "27": " "  # Use "27" to decode a space
}

def encode(sentence):
    letters = [l for l in sentence]
    converted = []
    s = ""
    for l in letters:
        l = l.upper()
        if l in alphabet_index:
            converted.append(alphabet_index[l])
        else:
            print(f"Error: Character '{l}' cannot be encoded.")
            return ""

    for l in converted:
        s += l
        s += " "

    return s.strip()

def decode(sentence: str):
    numbers = sentence.split()
    decoded = ""
    for num in numbers:
        if num in index_alphabet:
            decoded += index_alphabet[num]
        else:
            print(f"Error: Number '{num}' cannot be decoded.")
            return ""

    return decoded

encode_decode = input("Encode or decode mode? (e/d) ").lower()
if encode_decode == "e":
    sentence = input("Type a sentence to convert: ")
    result = encode(sentence)
    if result:
        print(result)
elif encode_decode == "d":
    sentence = input("Type the A1Z26 encoded sentence to decode separated by spaces: ")
    result = decode(sentence)
    if result:
        print(result)
else:
    print("Invalid mode selected.")
