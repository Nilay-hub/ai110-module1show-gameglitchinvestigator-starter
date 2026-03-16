# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

An AI built a number guessing game — but it's full of bugs. Hints lie, scores go negative, and the difficulty settings make no sense.

## 🛠️ Setup

1. Install dependencies: `pip3 install -r requirements.txt`
2. Run the fixed app: `python3 -m streamlit run app.py`

## 🕵️‍♂️ Your Mission (Completed)

1. **Played the game** and identified 4 bugs using Developer Debug Info.
2. **Fixed the Logic** — hints now correctly say Go Higher/Lower.
3. **Refactored & Tested** — moved logic into `logic_utils.py`, all 10 pytest tests pass.

## 📝 Document Your Experience

**Game Purpose:** A number guessing game where the player tries to guess a secret number between 1 and 100 with limited attempts and hint guidance.

**Bugs Found:**
- Hints were reversed (Go Higher shown when should say Go Lower)
- Secret number corrupted on even attempts by converting to string
- Score logic was unfair — wrong guesses sometimes gave +5 points
- Hard difficulty was easier than Normal (range 1–50 instead of 1–200)

**Fixes Applied:**
- Fixed comparison operators in `check_guess()` in `logic_utils.py`
- Removed even/odd attempt type conversion in `app.py`
- Simplified `update_score()` to always subtract 5 for wrong guesses
- Changed Hard difficulty range to 1–200

## 📸 Demo

Game runs correctly — hints match guesses, score is fair, and all 10 pytest tests pass.

## 🚀 Stretch Features

- Core bugs fixed and all tests passing with `PYTHONPATH=. pytest`