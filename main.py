import tkinter as tk
from tkinter import Scrollbar

# Function to update the expression in the text entry field
def press(key):
    current = entry.get()
    if key == '=':
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            update_history(f"{current} = {result}")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

# Function to update the history listbox
def update_history(entry_text):
    history_listbox.insert(tk.END, entry_text)
    history_listbox.yview(tk.END)  # Auto-scroll to the bottom

# Create the main window
root = tk.Tk()
root.title("Stylish Calculator with History and RGB Typography")
root.geometry("350x500")
root.configure(bg='#f0f0f0')

# Create an entry widget for the expression
entry = tk.Entry(root, width=16, font=('Helvetica', 28, 'bold'), borderwidth=2, relief="solid", bg='#ffffff', fg='#333333')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button styles with RGB colors
button_colors = [
    '#FF6347', '#FF4500', '#FF8C00', '#FFD700',
    '#ADFF2F', '#32CD32', '#00FF00', '#00FA9A',
    '#00BFFF', '#1E90FF', '#4169E1', '#8A2BE2',
    '#DDA0DD', '#FF69B4', '#FF1493', '#C71585'
]

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons with RGB colors
row = 1
col = 0
for i, button in enumerate(buttons):
    button_color = button_colors[i % len(button_colors)]
    action = lambda x=button: press(x)
    tk.Button(root, text=button, command=action, bg=button_color, fg='#ffffff', font=('Helvetica', 16, 'bold'), width=5, height=2, relief='raised').grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create a frame for the history listbox
history_frame = tk.Frame(root, bg='#f0f0f0')
history_frame.grid(row=5, column=0, columnspan=4, pady=10)

# Create a listbox to display history
history_listbox = tk.Listbox(history_frame, width=40, height=10, font=('Helvetica', 12), bg='#ffffff', fg='#333333', selectmode=tk.SINGLE)
history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar to the listbox
scrollbar = Scrollbar(history_frame, orient=tk.VERTICAL, command=history_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
history_listbox.config(yscrollcommand=scrollbar.set)

# Run the application
root.mainloop()
