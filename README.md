# AI-chatbot
A lightweight Python AI Chatbot built with fuzzy NLP pattern matching to handle typos, user intent, and natural replies.
# 🤖 AI Chatbot with Fuzzy NLP Matching

A lightweight, terminal-based AI Chatbot built in Python as part of my AI Internship. This project demonstrates core concepts of Natural Language Processing (NLP), text normalization, and intent recognition using fuzzy string matching algorithms to gracefully handle user typos and sentence variations.

---

## 🌟 Key Features

- **Fuzzy String Matching:** Utilizes Python's `difflib.SequenceMatcher` to calculate string similarity ratios, allowing the chatbot to understand queries even with minor typos or spelling errors.
- **Text Preprocessing & Normalization:** Automatically converts inputs to lowercase and trims whitespace for consistent phrase matching.
- **Intent Recognition:** Categorizes user inputs into defined intent buckets (e.g., greetings, age, creator info, status, help, farewells).
- **Dynamic & Randomized Replies:** Delivers varied responses for common intents using `random.choice()` to make interactions feel natural.
- **Fallback Handling:** Gracefully handles out-of-scope or unrecognized queries with helpful rephrasing prompts.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.x
- **Standard Libraries Used:** `difflib`, `random` *(No external `pip` dependencies required)*

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ai-chatbot.JS](https://github.com/your-username/ai-chatbot.JS)
   cd ai-chatbot



   ==========================================
      Enhanced AI Chatbot (Fuzzy NLP)     
     (Type 'exit' or 'bye' to quit)       
==========================================

You: helo
Bot: Hey there! What's on your mind?

You: whats ur agge
Bot: I don't have a physical age! I was built recently using Python.

You: r u singel
Bot: I'm just a computer program, so I don't date or have relationships!

You: bye
Bot: Goodbye! Have a great day!
