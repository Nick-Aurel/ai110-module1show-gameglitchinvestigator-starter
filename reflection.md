# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  Answer: the score wasn't being updated correctly
  I submitted 140 to test the system but the hint said, go higher
  and the score became negative
  when I inputed 1, the hint said go lower

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Answer: I used an AI coding assistant in my editor to scan the codebase, refactor functions into `logic_utils.py`, and suggest targeted fixes. One correct suggestion was to separate pure game logic (parsing guesses + comparing numbers) from Streamlit UI state so it could be tested with pytest; I verified this by running `pytest` and making sure the tests passed. One misleading suggestion was to keep the “secret becomes a string sometimes” behavior (it was framed like a harmless quirk), but I verified in the running app that it caused inconsistent comparisons and confusing hints, so I removed it to make gameplay stable.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Answer: I considered a bug fixed only when (1) the behavior in the live Streamlit game matched the rules (higher guesses produce “Too High”, lower guesses produce “Too Low”, and the secret stays consistent), and (2) automated tests passed. I ran `pytest` to verify the logic outcomes and added a new test to confirm `parse_guess("")` is rejected instead of counting as a real attempt. AI helped by proposing a small, focused test that targets one edge case, and I confirmed it by seeing all tests pass after the change.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Answer: Streamlit reruns the script from top to bottom on each interaction (like clicking a button), so anything that assigns a new random value during a rerun will “change” unless it’s stored in `st.session_state`. Session state is basically a small dictionary that persists across reruns for a user session, so it’s where you keep game variables like the secret, attempts, and score. The key change was making the secret live only in session state and resetting it intentionally only when starting a new game or changing difficulty, instead of letting type conversions or rerun logic accidentally change comparisons.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Answer: A habit I want to keep is writing small tests right after a fix, so I’m not relying only on “it seems to work” in the UI. Next time, I’d be more strict about checking AI suggestions against the actual requirements and real runtime behavior before accepting them, especially when the suggestion keeps “quirks” that hurt correctness. This project changed my view of AI-generated code by showing that it can be a fast starting point, but it still needs careful human review, testing, and sometimes simplification to be reliable.
