import difflib
import random

# Central dictionary containing intents, key patterns/phrases, and responses
RESPONSES = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "greetings", "good morning", "good evening", "helo", "hy"],
        "replies": [
            "Hello! How can I help you today?",
            "Hey there! What's on your mind?",
            "Hi! How can I assist you?"
        ]
    },
    "identity": {
        "keywords": ["who are you", "what is your name", "what are you", "whats your name"],
        "replies": [
            "I am a rule-based AI chatbot created for an internship project!"
        ]
    },
    "age": {
        "keywords": ["whats your age", "how old are you", "your age", "what is your age"],
        "replies": [
            "I don't have a physical age! I was built recently using Python."
        ]
    },
    "relationship": {
        "keywords": ["are you single", "are you married", "do you have a girlfriend", "do you date"],
        "replies": [
            "I'm just a computer program, so I don't date or have relationships!"
        ]
    },
    "creator": {
        "keywords": ["who created you", "who is your creator", "who programmed you", "who made you"],
        "replies": [
            "I was created as part of an AI internship project."
        ]
    },
    "status": {
        "keywords": ["how are you", "how is it going", "how are you doing", "how do you do"],
        "replies": [
            "I'm running smoothly, thank you! How are you doing today?"
        ]
    },
    "help": {
        "keywords": ["help", "support", "what can you do", "options"],
        "replies": [
            "I can answer simple questions! Feel free to ask about my name, age, creator, or just say hello."
        ]
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see ya", "exit", "quit"],
        "replies": [
            "Goodbye! Have a great day!"
        ]
    }
}

def find_best_intent(user_input, cutoff=0.6):
    """
    Evaluates input against defined keywords using fuzzy string matching.
    `cutoff` is the minimum similarity ratio needed to register a match (0.6 = 60%).
    """
    clean_input = user_input.lower().strip()
    
    best_intent = None
    best_score = 0.0

    for intent, data in RESPONSES.items():
        for keyword in data["keywords"]:
            # Direct exact phrase/substring match check
            if keyword in clean_input:
                return intent, True
            
            # Overall string fuzzy similarity ratio
            similarity = difflib.SequenceMatcher(None, clean_input, keyword).ratio()
            
            # Individual word similarity check to handle typos inside longer sentences
            words = clean_input.split()
            word_sims = [difflib.SequenceMatcher(None, word, keyword).ratio() for word in words]
            max_word_sim = max(word_sims) if word_sims else 0
            
            highest_match = max(similarity, max_word_sim)
            
            if highest_match > best_score and highest_match >= cutoff:
                best_score = highest_match
                best_intent = intent

    return best_intent, False

def get_chatbot_response(user_input):
    """Retrieves an appropriate response based on detected intent."""
    intent, exact_match = find_best_intent(user_input)
    
    if intent:
        data = RESPONSES[intent]
        reply = random.choice(data["replies"])
        return reply, intent == "farewell"
        
    fallback = "I'm not sure I understand that yet. Could you rephrase or ask something else?"
    return fallback, False

def main():
    print("==========================================")
    print("      Enhanced AI Chatbot (Fuzzy NLP)     ")
    print("     (Type 'exit' or 'bye' to quit)       ")
    print("==========================================")
    
    while True:
        user_message = input("\nYou: ")
        if not user_message.strip():
            continue
            
        bot_reply, is_exit = get_chatbot_response(user_message)
        print(f"Bot: {bot_reply}")
        
        if is_exit:
            break

if __name__ == "__main__":
    main()