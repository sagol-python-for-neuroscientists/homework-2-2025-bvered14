MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-', ' ': ' '  # Space remains as a space
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    # Step 1: Read the content of the input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Step 2: Convert the text to uppercase (Morse code is case-insensitive)
    text_upper = text.upper()

    # Step 3: Replace each character with its Morse code equivalent
    translation_table = str.maketrans(
        {char: MORSE_CODE[char] for char in MORSE_CODE.keys()}
    )
    morse_text = text_upper.translate(translation_table)

    # Step 4: Replace spaces between words with newlines
    morse_text = morse_text.replace(' ', '\n')

    # Step 5: Write the Morse code to the output file
    with open(output_file, 'w') as file:
        file.write(morse_text)


# Call the function to test it
english_to_morse()
