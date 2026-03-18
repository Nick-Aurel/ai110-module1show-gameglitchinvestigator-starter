# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Purpose**: A Streamlit number guessing game where the player tries to guess a secret number within a limited number of attempts (difficulty controls the range + attempt limit).
- **Bugs found**:
  - Hints were inconsistent/backwards (e.g., guessing very high could still say “go higher”).
  - The secret number comparison could break because the secret was sometimes treated as a string.
  - Attempts were counting even on invalid input, and the UI range didn’t always match the active difficulty.
- **Fixes applied**:
  - Refactored core logic into `logic_utils.py` (`check_guess`, `parse_guess`, `get_range_for_difficulty`, `update_score`) and imported it from `app.py`.
  - Made `check_guess` return stable outcomes (`Win` / `Too High` / `Too Low`) and fixed the hint mapping in the UI.
  - Ensured “New Game” and difficulty changes fully reset state and that the displayed range matches the generated secret.
  - Added a new pytest (`test_parse_guess_rejects_blank`) and verified all tests pass.

## 📸 Demo

- [ ] **Winning game screenshot**: Add a screenshot here showing a correct win (include the “Developer Debug Info” expander if you want to prove the secret).
  - Suggested filename: `assets/win.png`
  - Then replace this line with: `![Winning game](assets/win.png)`
- [ ] **(Optional) pytest screenshot**: If you did advanced testing, add a screenshot of `pytest` passing.
  - Suggested filename: `assets/pytest.png`
  - Then add: `![pytest passing](assets/pytest.png)`

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]


