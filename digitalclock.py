import tkinter as tk 
from time import strftime

def time():
    # Get the current time in the specified format
    string = strftime("%H:%M:%S %p")

    # Update the label text with the current time
    lbl.config(text = string)

    # Schedule the time function to be called after 1000 milliseconds (1 second)
    lbl.after(1000, time)


# Create the main Tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Create a label for displaying the digital clock
lbl = tk.Label(root, font=('Helvatica', 40, 'bold'), background="#2f3640", 
foreground="#fbc531")

# Pack the label to the center of the window
lbl.pack(anchor = 'center')

# Call the time function to start updating the clock
time()

root.mainloop()