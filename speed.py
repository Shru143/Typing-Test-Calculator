import tkinter as tk
from time import time
from tkinter import messagebox

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Calculator")
        self.root.geometry("600x400")
        self.root.configure(bg="#f9f9f9")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
            "In three words I can sum up everything I've learned about life: it goes on.",
            "Life is either a daring adventure or nothing at all.",
            "You miss 100% of the shots you don't take.",
            "Success is not the key to happiness. Happiness is the key to success.",
            "The only way to do great work is to love what you do."
        ]

        self.start_time = None
        self.current_sentence = self.sentences[0]  # Default to the first sentence

        # Create UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Typing Speed Test", font=("Comic Sans MS", 24, "bold"), bg="#f9f9f9", fg="#5a5a5a")
        title_label.pack(pady=20)

        # Dropdown for selecting sentences
        self.sentence_var = tk.StringVar(value=self.current_sentence)
        self.sentence_menu = tk.OptionMenu(self.root, self.sentence_var, *self.sentences, command=self.update_sentence)
        self.sentence_menu.config(font=("Arial", 12))
        self.sentence_menu.pack(pady=10)

        # Display Sample Text
        self.text_label = tk.Label(self.root, text=self.current_sentence, font=("Arial", 14), bg="#f9f9f9", wraplength=550)
        self.text_label.pack(pady=10)

        # Input Text Box
        self.text_entry = tk.Text(self.root, height=5, width=60, font=("Arial", 12))
        self.text_entry.pack(pady=20)
        self.text_entry.bind("<KeyPress>", self.start_typing)

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#f9f9f9", fg="#333")
        self.result_label.pack(pady=10)

        # Calculate Button
        self.calc_button = tk.Button(self.root, text="Calculate WPM", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.calculate_wpm)
        self.calc_button.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=self.reset_app)
        self.reset_button.pack(pady=10)

        # Animated feedback label
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), bg="#f9f9f9", fg="#4CAF50")
        self.feedback_label.pack(pady=10)

    def update_sentence(self, selected_sentence):
        """Update the sample sentence based on user's selection."""
        self.current_sentence = selected_sentence
        self.text_label.config(text=self.current_sentence)  # Update the label with the new sentence
        self.reset_app()  # Reset the app for the new sentence

    def start_typing(self, event):
        """Start the timer when the user begins typing."""
        if self.start_time is None:
            self.start_time = time()

    def calculate_wpm(self):
        """Calculate the typing speed in words per minute (WPM) and accuracy."""
        if self.start_time is None:
            messagebox.showwarning("Warning", "Start typing first!")
            return

        end_time = time()
        time_taken = end_time - self.start_time
        user_text = self.text_entry.get("1.0", tk.END).strip()

        # Calculate Words Per Minute (WPM)
        word_count = len(user_text.split())
        wpm = (word_count / time_taken) * 60

        # Calculate accuracy
        accuracy = self.calculate_accuracy(user_text)

        # Provide feedback
        self.display_feedback(wpm, accuracy)

    def calculate_accuracy(self, user_input):
        """Calculate accuracy by comparing user's input with the sample text."""
        sample_words = self.current_sentence.split()
        user_words = user_input.split()

        correct_words = 0
        for i in range(min(len(sample_words), len(user_words))):
            if sample_words[i] == user_words[i]:
                correct_words += 1

        accuracy = (correct_words / len(sample_words)) * 100
        return accuracy

    def display_feedback(self, wpm, accuracy):
        """Display feedback on WPM and accuracy."""
        if accuracy < 100:
            self.feedback_label.config(fg="#f44336")  # Red for low accuracy
            feedback_message = f"Words Per Minute (WPM): {wpm:.2f}\nAccuracy: {accuracy:.2f}%\nKeep practicing!"
        else:
            self.feedback_label.config(fg="#4CAF50")  # Green for perfect accuracy
            feedback_message = f"Words Per Minute (WPM): {wpm:.2f}\nAccuracy: {accuracy:.2f}%\nExcellent job!"

        self.feedback_label.config(text=feedback_message)

    def reset_app(self):
        """Reset the app for a new typing test."""
        self.start_time = None
        self.text_entry.delete("1.0", tk.END)  # Clear the input field
        self.feedback_label.config(text="", fg="#4CAF50")
        self.result_label.config(text="")  # Clear result label

# Initialize the App
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
