from tkinter import*

root = Tk()
root.geometry("400x300")

text = Text(root, height=10, width=40)
text.pack(pady=10)

# Insert at line 1, column 0
text.insert("1.0", "This is line 1\n")

# Insert at the end
text.insert("end", "This is line 2\n")

# Get all text
all_text = text.get("1.0", "end")
print("All text:", all_text)

# Get text from line 1, character 0 to line 2, character 5
partial = text.get("1.0", "2.5")
print("Partial:", partial)

root.mainloop()