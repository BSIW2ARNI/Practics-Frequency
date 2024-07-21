import tkinter as tk
from tkinter import filedialog
from collections import Counter

def analyze_text(input_text=None):
    if input_text is None:
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r', encoding='utf-8') as file: # Указываем кодировку UTF-8
            result_text.insert(tk.END, f'Текст прочитан из файла: {file_path}\n')
            text = file.read()
    else:
        text = input_text.get("1.0", "end-1c")

    text = text.lower()  # Приводим все символы к нижнему регистру
    words = text.split()  # Разделяем текст на слова
    word_count = len(words)
    result_text.insert(tk.END, f'Общее количество слов в тексте: {word_count}\n')

    text_length = len(text)
    char_freq = Counter(text)

    # Печать частоты встречи каждого символа в процентах
    for char, freq in char_freq.items():
        percentage = (freq / text_length) * 100
        result_text.insert(tk.END, f'{char}: {percentage:.2f}%\n')

#Создаем графический интерфейс
root = tk.Tk()
root.title("Character Frequency Analyzer")

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

analyze_button_file = tk.Button(root, text="Анализировать текст из файла", command=lambda: analyze_text())
analyze_button_file.pack()

analyze_button_input = tk.Button(root, text="Анализировать введенный текст", command=lambda: analyze_text(text_input))
analyze_button_input.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()