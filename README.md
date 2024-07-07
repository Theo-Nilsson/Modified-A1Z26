This program provides functionality to encode and decode sentences using a modified A1Z26 cipher, where each letter of the alphabet is represented by its position in the alphabet (A=1, B=2, ..., Z=26), and spaces are represented by 27. Users can choose to either encode a sentence into this numeric format or decode a numeric sequence back into a sentence. The program handles input validation and displays appropriate error messages for invalid characters or numbers.

### Key Features:
- **Encoding**: Converts each character in a sentence to its corresponding numeric value.
- **Decoding**: Converts a sequence of numeric values back to the corresponding sentence.
- **Input Validation**: Ensures only valid characters and numbers are processed, providing error messages for any invalid entries.
- **User Interaction**: Prompts the user to choose between encoding and decoding modes and to provide the necessary input for the chosen operation.

### Usage:
1. The user is prompted to select "encode" (e) or "decode" (d) mode.
2. In encoding mode, the user enters a sentence, which is converted to a numeric string.
3. In decoding mode, the user enters a numeric string separated by spaces, which is converted back to a readable sentence.