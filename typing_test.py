import customtkinter as ctk
import time
import random

# Sample texts
texts = [
    "The quick brown fox jumps over the lazy dog", 
    "To be, or not to be: that is the question", 
    "The only thing we have to fear is fear itself", 
    "That which does not kill us makes us stronger", 
    "The pen is mightier than the sword"
]

class TypingSpeedTest(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")
        self.geometry("700x400")

        # Variables
        self.start_time = None
        self.sample_text = random.choice(texts)

        # Widgets
        self.label = ctk.CTkLabel(self, text="Typing Speed Test", font=("Arial", 24, "bold"))
        self.label.pack(pady=10)

        self.sample_label = ctk.CTkTextbox(self, width=600, height=70)
        self.sample_label.insert("1.0", self.sample_text)
        self.sample_label.configure(state="disabled")
        self.sample_label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, width=600)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.handle_enter)
        self.entry.bind("<Key>", self.handle_any_key)


        self.timer_label = ctk.CTkLabel(self, text="Time: 0.00s", font=("Arial", 18))
        self.timer_label.pack(pady=5)

        self.result_label = ctk.CTkLabel(self, text="", font=("Arial", 18))
        self.result_label.pack(pady=10)

        self.update_timer_flag = False
        self.after(100, self.update_timer)

    def handle_any_key(self, event=None):
        if self.start_time is None:
            # Start timer on first key press
            self.start_time = time.time()
            self.update_timer_flag = True
            self.result_label.configure(text="Typing started... Press Enter to finish.")

    def handle_enter(self, event=None):
        if self.start_time is None:
            # Start timer
            self.start_time = time.time()
            self.update_timer_flag = True
            self.result_label.configure(text="Typing started... Press Enter again to stop.")
        else:
            # Stop timer
            self.update_timer_flag = False
            elapsed = time.time() - self.start_time
            user_input = self.entry.get()
            words = len(user_input.split())
            wpm = words / (elapsed / 60)
            accuracy = self.calculate_accuracy(user_input, self.sample_text)

            self.result_label.configure(
                text=f"Time: {elapsed:.2f}s | WPM: {wpm:.2f} | Accuracy: {accuracy:.1f}%"
            )

            # Reset and load a new sentence
            self.start_time = None
            self.entry.delete(0, "end")
            self.timer_label.configure(text="Time: 0.00s")

            # New random sentence
            self.sample_text = random.choice(texts)
            self.sample_label.configure(state="normal")
            self.sample_label.delete("1.0", "end")
            self.sample_label.insert("1.0", self.sample_text)
            # self.sample_label.configure(state="disabled")

    def calculate_accuracy(self, user_text, sample_text):
        correct_chars = 0
        for a, b in zip(user_text, sample_text):
            if a == b:
                correct_chars += 1
            
        total_chars = len(sample_text)
        return (correct_chars / total_chars) * 100 if total_chars > 0 else 0

    def update_timer(self):
        if self.start_time and self.update_timer_flag:
            elapsed = time.time() - self.start_time
            self.timer_label.configure(text=f"Time: {elapsed:.2f}s")
        self.after(100, self.update_timer)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = TypingSpeedTest()
    app.mainloop()