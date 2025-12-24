import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

# --- Configuration ---
class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Language Translator")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f2f5")

        # --- UI Elements ---
        
        # Title
        self.title_label = tk.Label(root, text="AI Language Translator", font=("Helvetica", 20, "bold"), bg="#f0f2f5", fg="#333")
        self.title_label.pack(pady=20)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f0f2f5")
        self.input_frame.pack(pady=10)

        self.input_label = tk.Label(self.input_frame, text="Enter Text:", bg="#f0f2f5", font=("Arial", 10, "bold"))
        self.input_label.grid(row=0, column=0, sticky="w", padx=5)

        self.input_text = tk.Text(self.input_frame, height=5, width=60, font=("Arial", 10))
        self.input_text.grid(row=1, column=0, padx=5, pady=5)

        # Language Selection Frame
        self.lang_frame = tk.Frame(root, bg="#f0f2f5")
        self.lang_frame.pack(pady=10)

        self.lang_label = tk.Label(self.lang_frame, text="Select Target Language:", bg="#f0f2f5", font=("Arial", 10))
        self.lang_label.pack(side=tk.LEFT, padx=10)

        # Get supported languages dynamically
        self.languages_dict = GoogleTranslator(source='auto', target='en').get_supported_languages(as_dict=True)
        self.language_list = list(self.languages_dict.keys())
        
        self.lang_combobox = ttk.Combobox(self.lang_frame, values=self.language_list, width=20, state="readonly")
        self.lang_combobox.set("spanish") # Default
        self.lang_combobox.pack(side=tk.LEFT)

        # Buttons Frame
        self.btn_frame = tk.Frame(root, bg="#f0f2f5")
        self.btn_frame.pack(pady=10)

        self.translate_btn = tk.Button(self.btn_frame, text="Translate Now", command=self.translate_text, bg="#007bff", fg="white", font=("Arial", 10, "bold"), padx=15, pady=5)
        self.translate_btn.pack(side=tk.LEFT, padx=10)

        self.clear_btn = tk.Button(self.btn_frame, text="Clear", command=self.clear_text, bg="#dc3545", fg="white", font=("Arial", 10, "bold"), padx=15, pady=5)
        self.clear_btn.pack(side=tk.LEFT, padx=10)

        # Output Frame
        self.output_frame = tk.Frame(root, bg="#f0f2f5")
        self.output_frame.pack(pady=10)

        self.output_label = tk.Label(self.output_frame, text="Translation:", bg="#f0f2f5", font=("Arial", 10, "bold"))
        self.output_label.grid(row=0, column=0, sticky="w", padx=5)

        self.output_text = tk.Text(self.output_frame, height=5, width=60, font=("Arial", 10), state="disabled", bg="#e9ecef")
        self.output_text.grid(row=1, column=0, padx=5, pady=5)

        # Copy Button
        self.copy_btn = tk.Button(root, text="Copy Translation to Clipboard", command=self.copy_to_clipboard, bg="#28a745", fg="white", font=("Arial", 9))
        self.copy_btn.pack(pady=5)
        
        # Footer
        self.footer = tk.Label(root, text="Developed by Emad | CodeAlpha Internship", bg="#f0f2f5", fg="#777", font=("Arial", 8))
        self.footer.pack(side=tk.BOTTOM, pady=10)

    def translate_text(self):
        text_to_translate = self.input_text.get("1.0", tk.END).strip()
        target_lang_name = self.lang_combobox.get()

        if not text_to_translate:
            messagebox.showwarning("Input Error", "Please enter some text to translate.")
            return

        # Find language code
        target_lang_code = self.languages_dict.get(target_lang_name, 'en')

        try:
            # Using deep_translator
            translated_text = GoogleTranslator(source='auto', target=target_lang_code).translate(text_to_translate)
            
            # Update output text
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated_text)
            self.output_text.config(state="disabled")
            
        except Exception as e:
            messagebox.showerror("Translation Error", f"An error occurred: {e}")

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state="disabled")

    def copy_to_clipboard(self):
        translation = self.output_text.get("1.0", tk.END).strip()
        if translation:
            pyperclip.copy(translation)
            messagebox.showinfo("Success", "Text copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "Nothing to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

