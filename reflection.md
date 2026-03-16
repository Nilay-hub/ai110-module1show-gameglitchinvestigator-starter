# Game Glitch Investigator – Reflection

## 1. What was broken when you started?

**Bug 1: Hints were reversed**
- Expected: Guessing 75 when secret is 90 should say "Go HIGHER"
- Actual: The game said "Go LOWER" — the comparison operators in check_guess() were flipped

**Bug 2: Secret number corrupted on even attempts**
- Expected: The secret number stays the same throughout the game
- Actual: On every even-numbered attempt, the code converted the secret to a string, causing wrong comparisons and misleading hints

**Bug 3: Score goes negative for wrong guesses**
- Expected: Score should only go negative consistently or reward good guesses
- Actual: "Too High" on even attempts gave +5 points (rewarding wrong guesses), while "Too Low" always lost 5 points — inconsistent and unfair

**Bug 4: Hard difficulty was easier than Normal**
- Expected: Hard mode should have a wider range (harder to guess)
- Actual: Hard was set to 1–50, which is actually easier than Normal (1–100)

## 2. How did you use AI as a teammate?

**Correct suggestion:** The AI correctly identified that the hint bug was caused by flipped comparison operators in check_guess(). It suggested swapping "Go HIGHER" and "Go LOWER" which fixed the issue immediately. I verified this by playing the game and confirming hints were now correct.

**Incorrect/misleading suggestion:** The AI initially gave me a simplified version of app.py that didn't match the actual starter code structure. I had to reject it and carefully compare with the original before making targeted edits instead of replacing everything blindly.

## 3. Debugging and testing your fixes

- Fixed check_guess() in logic_utils.py — verified by playing the game and seeing correct hints
- Fixed the secret number corruption bug by removing the even/odd attempt type conversion in app.py
- Fixed update_score() to always subtract 5 for wrong guesses regardless of attempt number
- Fixed Hard difficulty range from 1–50 to 1–200
- Ran PYTHONPATH=. pytest and confirmed all 10 tests passed