import tkinter as tk
from tkinter import scrolledtext, ttk
import sounddevice as sd
import numpy as np
import json
from vosk import Model, KaldiRecognizer
import pyttsx3
import threading

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        root.title("Hlasový Asistent")
        root.geometry("600x500")

        # GUI prvky
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
        self.chat_area.pack(pady=10)
        self.chat_area.insert(tk.END, "🌟 Bot: Ahoj! Můžeš psát nebo mluvit (tlačítko Start).\n")
        self.chat_area.config(state=tk.DISABLED)

        # Tlačítka pro hlasový vstup
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=5)
        
        self.start_button = ttk.Button(button_frame, text="Start poslechu", command=self.start_listening)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Stop poslechu", command=self.stop_listening)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Textový vstup
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10, fill=tk.X)
        
        self.text_input = ttk.Entry(input_frame, width=50)
        self.text_input.pack(side=tk.LEFT, padx=5)
        self.text_input.bind("<Return>", lambda e: self.process_text_input())
        
        self.submit_button = ttk.Button(input_frame, text="Odeslat text", command=self.process_text_input)
        self.submit_button.pack(side=tk.LEFT)

        # Inicializace Vosk a TTS
        self.model = Model("vosk-model-small-cs-0.4")
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.is_listening = False

        # Načtení příručky
        with open("data_manual.txt", "r", encoding="utf-8") as f:
            self.manual = f.read().split("\n")

    def get_answer(self, question):
        if "co umíš" in question.lower():
            return "Umím:\n• Poradit s resetem zařízení\n• Najít návody\n• Odpovědět na základní dotazy"
        for line in self.manual:
            if question.lower() in line.lower():
                return line
        return "Omlouvám se, nevím."

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_thread(self):
        self.is_listening = True
        with sd.RawInputStream(samplerate=16000, dtype="int16", channels=1) as stream:
            while self.is_listening:
                data, _ = stream.read(4000)
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "")
                    if text:
                        self.update_chat(f"Vy: {text}")
                        answer = self.get_answer(text)
                        self.update_chat(f"Bot: {answer}")
                        self.speak(answer)

    def process_text_input(self):
        text = self.text_input.get().strip()
        if text:
            self.update_chat(f"Vy (text): {text}")
            answer = self.get_answer(text)
            self.update_chat(f"Bot: {answer}")
            self.speak(answer)
            self.text_input.delete(0, tk.END)

    def start_listening(self):
        self.update_chat("🟢 Poslouchám...")
        threading.Thread(target=self.listen_thread, daemon=True).start()

    def stop_listening(self):
        self.is_listening = False
        self.update_chat("🔴 Zastaveno.")

    def update_chat(self, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{message}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()