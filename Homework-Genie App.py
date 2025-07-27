import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="Homework Genie", 
    page_icon="📘", 
    layout="centered"
)

# Main title and header
st.title("📘 Homework Genie")
st.subheader("Your magical homework helper! ✨")
st.write("Ask me any question about Math, Reading, or Science and I'll help you learn!")

# Subject selection
st.write("### Choose your subject:")
subject = st.radio(
    "Pick the subject you need help with:",
    ["Math 🔢", "Reading 📖", "Science 🔬"],
    help="Select the subject area for your homework question"
)

# Clean subject name for processing
subject_clean = subject.split()[0]

# Question input
st.write("### Ask your question:")
user_question = st.text_area(
    "📝 Type your homework question here:",
    placeholder="For example: 'What is 5 times 3?' or 'What is a noun?' or 'How do plants grow?'",
    height=100
)

def get_math_response(question):
    """Handle math-related questions"""
    q = question.lower()
    
    # Multiplication
    if any(word in q for word in ["multiply", "times", "×", "*"]):
        return "🔢 Multiplying means adding a number to itself multiple times! For example, 3 × 4 means 3 + 3 + 3 + 3 = 12. It's like having 3 groups of 4 things each!"
    
    # Addition
    elif any(word in q for word in ["add", "plus", "+"]):
        return "➕ Adding means putting numbers together to make a bigger number! When you add 2 + 3, you're counting 2 things, then 3 more things, which gives you 5 things total!"
    
    # Subtraction
    elif any(word in q for word in ["subtract", "minus", "-", "take away"]):
        return "➖ Subtracting means taking some away from what you have. If you have 8 cookies and eat 3, you subtract: 8 - 3 = 5 cookies left!"
    
    # Division
    elif any(word in q for word in ["divide", "division", "÷", "/"]):
        return "➗ Division means splitting things into equal groups. If you have 12 candies and want to share them equally among 3 friends, each friend gets 12 ÷ 3 = 4 candies!"
    
    # Fractions
    elif "fraction" in q:
        return "🍕 A fraction shows parts of a whole! Think of a pizza: 1/2 means 1 piece out of 2 equal pieces. 3/4 means 3 pieces out of 4 equal pieces!"
    
    # Even and odd numbers
    elif any(word in q for word in ["even", "odd"]):
        return "🎯 Even numbers can be split into pairs perfectly (2, 4, 6, 8...). Odd numbers always have one left over (1, 3, 5, 7...)!"
    
    # Place value
    elif any(word in q for word in ["place value", "tens", "ones", "hundreds"]):
        return "🏠 Place value tells us what each digit means! In 234: the 2 is in hundreds place (200), 3 is in tens place (30), and 4 is in ones place (4)!"
    
    # Shapes
    elif any(word in q for word in ["shape", "triangle", "square", "circle", "rectangle"]):
        return "📐 Shapes are everywhere! A triangle has 3 sides, a square has 4 equal sides, a rectangle has 4 sides with opposite sides equal, and a circle is perfectly round!"
    
    # Time
    elif any(word in q for word in ["time", "clock", "hour", "minute"]):
        return "⏰ Time helps us know when things happen! There are 60 minutes in 1 hour, and 24 hours in 1 day. The big hand shows minutes, the little hand shows hours!"
    
    # Money
    elif any(word in q for word in ["money", "cent", "dollar", "coin"]):
        return "💰 Money math is important! A penny = 1 cent, nickel = 5 cents, dime = 10 cents, quarter = 25 cents, and a dollar = 100 cents!"
    
    return None

def get_reading_response(question):
    """Handle reading-related questions"""
    q = question.lower()
    
    # Parts of speech
    if "noun" in q:
        return "🏷️ A noun is a person, place, or thing! Examples: 'dog' (thing), 'school' (place), 'teacher' (person). Nouns are the naming words!"
    
    elif "verb" in q:
        return "🏃 A verb shows action or what someone is doing! Examples: run, jump, think, sing, eat. Verbs are the action words that make sentences exciting!"
    
    elif "adjective" in q:
        return "🎨 An adjective describes or tells us more about a noun! Examples: 'big dog', 'red apple', 'funny joke'. They make our writing more colorful!"
    
    elif "adverb" in q:
        return "⚡ An adverb tells us more about a verb! They often end in -ly: quickly, slowly, carefully. They tell us HOW something is done!"
    
    # Reading comprehension
    elif any(word in q for word in ["main idea", "theme"]):
        return "💡 The main idea is what the story or paragraph is mostly about! Look for the most important point the author wants you to understand!"
    
    elif any(word in q for word in ["character", "protagonist"]):
        return "👥 Characters are the people or animals in a story! The main character is usually the one the story focuses on the most!"
    
    elif "setting" in q:
        return "🏞️ The setting is WHERE and WHEN a story takes place! It could be a school, a forest, the past, or the future!"
    
    # Phonics and spelling
    elif any(word in q for word in ["phonics", "sound", "letter"]):
        return "🔤 Phonics helps us sound out words! Each letter makes a sound, and we blend sounds together to read words: c-a-t makes 'cat'!"
    
    elif any(word in q for word in ["rhyme", "rhyming"]):
        return "🎵 Rhyming words sound the same at the end! Like 'cat' and 'hat', or 'dog' and 'log'. Rhymes make poems and songs fun!"
    
    elif any(word in q for word in ["syllable", "clap"]):
        return "👏 Syllables are the beats in words! Clap as you say a word: 'but-ter-fly' has 3 claps, so 3 syllables!"
    
    # Reading strategies
    elif any(word in q for word in ["context clue", "unknown word"]):
        return "🔍 When you don't know a word, look at the words around it for clues! The other words in the sentence can help you figure out what it means!"
    
    elif any(word in q for word in ["summary", "summarize"]):
        return "📝 A summary tells the most important parts of a story in just a few sentences! Include who, what, where, when, and why!"
    
    return None

def get_science_response(question):
    """Handle science-related questions"""
    q = question.lower()
    
    # Physics concepts
    if "gravity" in q:
        return "🌍 Gravity is the invisible force that pulls everything down toward Earth! That's why when you drop something, it falls down instead of floating up!"
    
    elif any(word in q for word in ["magnet", "magnetic"]):
        return "🧲 Magnets have special powers! They can pull (attract) some metals like iron, and they have two ends called poles: north and south!"
    
    elif any(word in q for word in ["light", "shadow"]):
        return "💡 Light travels in straight lines! When light hits something it can't go through, it makes a shadow. Light helps us see everything around us!"
    
    elif any(word in q for word in ["sound", "vibration"]):
        return "🔊 Sound happens when things vibrate (shake back and forth)! The vibrations travel through the air to your ears so you can hear!"
    
    # Life science
    elif any(word in q for word in ["plant", "grow"]):
        return "🌱 Plants are amazing! They need four things to grow: sunlight for energy, water to drink, air to breathe, and nutrients from soil for food!"
    
    elif any(word in q for word in ["animal", "habitat"]):
        return "🦁 Animals live in habitats - special places that give them everything they need! Fish live in water, birds in trees, and bears in forests!"
    
    elif any(word in q for word in ["food chain", "eat"]):
        return "🍃 A food chain shows who eats what! Plants make their own food, plant-eaters eat plants, and meat-eaters eat other animals!"
    
    elif any(word in q for word in ["life cycle", "baby"]):
        return "🦋 All living things have a life cycle! They are born, grow up, have babies of their own, and complete the circle of life!"
    
    # Earth science
    elif any(word in q for word in ["water cycle", "rain"]):
        return "☔ The water cycle is water's amazing journey! Water evaporates (rises up), forms clouds (condenses), then falls as rain (precipitation)!"
    
    elif any(word in q for word in ["weather", "cloud"]):
        return "⛅ Weather is what's happening in the sky! Clouds are made of tiny water droplets floating in the air. Different clouds bring different weather!"
    
    elif any(word in q for word in ["rock", "mineral"]):
        return "🪨 Rocks are made of minerals and come in three types: igneous (from hot lava), sedimentary (from layers), and metamorphic (changed by heat)!"
    
    elif any(word in q for word in ["soil", "dirt"]):
        return "🌱 Soil isn't just dirt! It's full of nutrients, tiny creatures, and decomposed plants that help new plants grow healthy and strong!"
    
    # Space science
    elif any(word in q for word in ["sun", "solar"]):
        return "☀️ The Sun is our nearest star! It gives us light and heat, and is so big that over 1 million Earths could fit inside it!"
    
    elif any(word in q for word in ["moon", "phase"]):
        return "🌙 The Moon is Earth's companion in space! It looks different each night because we see different amounts of the Sun shining on it!"
    
    elif any(word in q for word in ["planet", "earth"]):
        return "🌍 Earth is our home planet! It's the perfect distance from the Sun - not too hot, not too cold - and has air and water for life!"
    
    # Basic chemistry
    elif any(word in q for word in ["matter", "solid", "liquid", "gas"]):
        return "⚗️ Everything around us is made of matter! It comes in three forms: solids (like ice), liquids (like water), and gases (like steam)!"
    
    elif any(word in q for word in ["mix", "solution"]):
        return "🥤 When you mix things, sometimes they blend completely (like sugar in water) and sometimes they stay separate (like oil and water)!"
    
    return None

def get_response(subject, question):
    """Main function to get responses based on subject and question"""
    if not question.strip():
        return "🤔 I'd love to help, but I need a question first! What would you like to learn about?"
    
    # Try subject-specific responses first
    if subject == "Math":
        response = get_math_response(question)
        if response:
            return response
    elif subject == "Reading":
        response = get_reading_response(question)
        if response:
            return response
    elif subject == "Science":
        response = get_science_response(question)
        if response:
            return response
    
    # Generic encouraging responses for unmatched questions
    encouragements = [
        f"🌟 Great question about {subject.lower()}! While I don't have that specific answer, keep asking questions - that's how we learn!",
        f"🤗 I love your curiosity about {subject.lower()}! Try asking your teacher or looking in your textbook for that one!",
        f"💭 That's a thoughtful {subject.lower()} question! Sometimes the best way to find answers is to explore and experiment!",
        f"🚀 Your {subject.lower()} question shows you're thinking like a real learner! Keep wondering about the world around you!"
    ]
    
    import random
    return random.choice(encouragements)

# Create two columns for the button and additional info
col1, col2 = st.columns([2, 1])

with col1:
    # Ask the Genie button
    ask_button = st.button("🔮 Ask the Genie!", type="primary")

with col2:
    # Show a tip
    if st.button("💡 Show Tip"):
        tips = {
            "Math": "Try asking about numbers, shapes, or math operations like adding and multiplying!",
            "Reading": "Ask about parts of speech, reading strategies, or story elements!",
            "Science": "Wonder about plants, animals, weather, or how things work!"
        }
        st.info(f"💡 **Tip for {subject_clean}:** {tips.get(subject_clean, 'Keep asking questions!')}")

# Process the question when button is clicked
if ask_button:
    if user_question.strip():
        with st.spinner("🔮 The Genie is thinking..."):
            answer = get_response(subject_clean, user_question)
        
        # Display the answer with nice formatting
        st.success("💬 **Genie says:**")
        st.write(answer)
        
        # Add some encouragement
        st.balloons()
        
        # Suggest asking another question
        st.info("🎓 Got another question? The Genie loves to help you learn!")
        
    else:
        st.warning("📝 Please type a question first, then ask the Genie!")

# Footer with helpful information
st.write("---")
st.write("### 🌟 How to get the best help:")
st.write("• **Be specific** - instead of 'math help', try 'how do I multiply 6 times 4?'")
st.write("• **Use key words** - mention the topic you're learning about")
st.write("• **Don't give up** - if the Genie doesn't know something, ask your teacher!")

# Fun fact section
with st.expander("🎯 Fun Learning Facts"):
    fun_facts = {
        "Math": [
            "Zero was invented about 1,500 years ago!",
            "The word 'mathematics' comes from the Greek word 'mathema' meaning 'knowledge'!",
            "Ancient people counted on their fingers and toes - that's why we use base 10!"
        ],
        "Reading": [
            "The average person reads about 250 words per minute!",
            "Reading for just 6 minutes can reduce stress by 68%!",
            "The word 'bookworm' comes from insects that actually eat books!"
        ],
        "Science": [
            "A group of flamingos is called a 'flamboyance'!",
            "Lightning is five times hotter than the surface of the Sun!",
            "Butterflies taste with their feet!"
        ]
    }
    
    facts = fun_facts.get(subject_clean, ["Learning is the best adventure!"])
    for fact in facts:
        st.write(f"• {fact}")

# Study tips based on subject
with st.expander("📚 Study Tips"):
    study_tips = {
        "Math": [
            "Practice a little bit every day - math builds on itself!",
            "Draw pictures or use objects to help you understand problems",
            "Check your work by doing the problem a different way",
            "Don't be afraid to make mistakes - they help you learn!"
        ],
        "Reading": [
            "Read a little bit every day to improve your skills",
            "Ask questions about what you read to check understanding",
            "Look up words you don't know and use them in sentences",
            "Read different types of books to expand your vocabulary"
        ],
        "Science": [
            "Observe the world around you and ask 'why' and 'how'",
            "Try simple experiments at home (with adult help!)",
            "Keep a science journal to record your observations",
            "Connect what you learn to things you see in real life"
        ]
    }
    
    tips = study_tips.get(subject_clean, ["Stay curious and keep learning!"])
    for tip in tips:
        st.write(f"• {tip}")
