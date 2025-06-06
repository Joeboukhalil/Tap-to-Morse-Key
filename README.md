# Tap to Morse Key

**Tap to Morse Key** is an accessible communication app designed for people with limited mobility. It allows users to type messages using only a few keyboard keys by entering Morse code, which the app then converts into letters, words, and full phrases — and reads the final phrase out loud using text-to-speech.

---

## 🧠 Why It Helps

This app is designed for users who may not be able to speak or type easily. With just the arrow keys and spacebar, anyone can write and communicate effectively.

---

## 💡 Features

- Type using Morse code (dots and dashes)
- Use only a few keyboard keys (no mouse needed)
- Get feedback as you type
- Convert Morse into full sentences
- Text-to-speech support for reading your phrase out loud

---

## 🎮 Controls

| Key           | Action                         |
|---------------|--------------------------------|
| **← (Left)**   | Add dot `.`                   |
| **→ (Right)**  | Add dash `-`                  |
| **↑ (Up)**     | First press = Finish letter   |
| **↑ (Up)**     | Second press = Finish word    |
| **↓ (Down)**   | Finish phrase and read aloud  |
| **Space**      | Delete last dot or dash       |

You’ll see feedback printed in the terminal for every action.

---

## 📦 How to Use

### ✅ Step 1: Download



Direct download link available in the **Releases** section of this repository.

---

### ▶️ Step 2: Run

Double-click `TapToMorseKey.exe` to run it. No installation is required.

> ⚠️ If the app doesn’t respond to your keypresses, right-click it and choose **“Run as Administrator”** — this is required on some systems to allow key detection.




---

## 💬 Example

Typing this:

- `← ← ← ←` (....) → Up → = H  
- `←` (.) → Up → = E  
- `← ← ←` (...) → Up → = S  
- `← ← ←` (...) → Up (twice) = Word ends → **"HES"**

Then press `↓` → phrase will be spoken aloud!

---

## 🧰 Built With

- Python 3
- `pyttsx3` – for text-to-speech
- `keyboard` – for detecting keypresses

---

## 🙌 Credits

Created by [Joe Bou Khalil]  
Inspired by accessibility and the power of simple tools.

---

## 📃 License

This project is free to use and modify. Attribution is appreciated!
