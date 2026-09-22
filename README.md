# CodeAlpha Internship: Simple Terminal Chatbot

This is a lightweight, rule-based chatbot script built using Python. I developed this project to fulfill Task 4 of my software engineering internship curriculum at **CodeAlpha**.

## 📌 Project Overview
The main goal was to create an interactive assistant that can run directly inside the computer terminal. It listens to what the user types, filters out messy spacing or capitalisation, and matches the text against specific built-in conversational triggers.

### What it does:
* **Pattern Recognition:** Scans messages for phrases like `hello`, `how are you`, or `bye`.
* **Smart Input Clean-up:** Converts text to lowercase and strips extra empty spaces so typing variations don't break the bot.
* **Fallback Protection:** If you type something completely random, the script won't crash; it politely asks you to try again or look at the help menu.

## ⚙️ How it works under the hood
* **Infinite Loops:** Uses a `while True` loop to keep the chat window open until you explicitly tell it to exit.
* **Conditional Rerouting:** Employs standard `if-elif-else` branches to direct user input to the correct conversational reply.
* **Text Formatting:** Uses Python's native `.lower()` and `.strip()` tools to make user input matching highly reliable.

## 🎮 What it looks like in action
Here is a quick snapshot of the script executing inside the terminal window:

```text
=========================================
      Welcome to my CodeAlpha Bot!       
=========================================

Quick tip: Type 'bye' or 'exit' whenever you want to quit.

Bot: Hey! I'm your AI chat assistant for this project. What's on your mind?

You: Hello there!
Bot: Hello! Hope your day is going great so far.

You: How are you doing?
Bot: I'm doing good, thanks! Just sitting here running inside your terminal.

You: what is your name?
Bot: I'm just a simple rule-based chatbot built for my CodeAlpha programming task.

You: bye
Bot: See ya! Good luck with the rest of the internship tasks!
```
