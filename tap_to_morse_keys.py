import pyttsx3
import keyboard
import time

# Morse dictionary
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Initialize variables
current_morse = ''
current_word = ''
phrase = ''
previous_key = ''
last_up_time = 0

print("Controls:")
print("← = Dot | → = Dash | ↑ (once) = End Letter | ↑ (twice) = End Word")
print("↓ = Read Phrase | Space = Delete Last Dot/Dash")
print("-" * 50)

while True:
    if keyboard.is_pressed('left'):
        if previous_key != 'left':
            current_morse += '.'
            print(f"Dot (.) | Morse: {current_morse}")
            previous_key = 'left'
            time.sleep(0.2)

    elif keyboard.is_pressed('right'):
        if previous_key != 'right':
            current_morse += '-'
            print(f"Dash (-) | Morse: {current_morse}")
            previous_key = 'right'
            time.sleep(0.2)

    elif keyboard.is_pressed('space'):
        if previous_key != 'space':
            if current_morse:
                print(f"Deleted: {current_morse[-1]}")
                current_morse = current_morse[:-1]
                print(f"Current Morse: {current_morse}")
            else:
                print("Nothing to delete.")
            previous_key = 'space'
            time.sleep(0.2)

    elif keyboard.is_pressed('up'):
        if previous_key != 'up':
            current_time = time.time()
            if current_time - last_up_time < 1.0:
                # Second up = end word
                if current_morse:
                    letter = morse_dict.get(current_morse, '?')
                    current_word += letter
                    current_morse = ''
                phrase += current_word + ' '
                print(f"Word: {current_word}")
                current_word = ''
            else:
                # First up = end letter
                if current_morse:
                    letter = morse_dict.get(current_morse, '?')
                    current_word += letter
                    print(f"Letter: {letter} | Word: {current_word}")
                    current_morse = ''
            last_up_time = current_time
            previous_key = 'up'
            time.sleep(0.2)

    elif keyboard.is_pressed('down'):
        if previous_key != 'down':
            # Finish any remaining input
            if current_morse:
                letter = morse_dict.get(current_morse, '?')
                current_word += letter
                current_morse = ''
            if current_word:
                phrase += current_word
                current_word = ''
            if phrase.strip():
                print(f"Phrase: {phrase.strip()}")
                engine.say(phrase.strip())
                engine.runAndWait()
                phrase = ''
            previous_key = 'down'
            time.sleep(0.5)

    else:
        previous_key = ''  # Reset key detection
