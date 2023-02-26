import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import receive_msg_gui
import transmit


# Function to handle the button click for sending input
def send_input():
    # Get the input text from the input space
    input_text = input_space.get()
    transmit.run(input_text)

    # Display the input text in the output space
    output_space.insert(tk.END, "You: " + input_text + "\n")

    # Call the function to process the input and generate a response
    # Clear the input space
    input_space.delete(0, tk.END)
    
    # Save the sent message for possible resending
    global sent_message
    sent_message = input_text
    
    #########################send data

# Function to handle the button click for receiving data
def receive_data():
    # Call the function to process the received data
    processed_data =  receive_msg_gui.run() #########################################recieving data

    
    # Display the processed data in the output space
    output_space.insert(tk.END, "Received data: " + processed_data + "\n")


# Function to handle the button click for clearing the chat history
def clear_history():
    # Clear the output space
    output_space.delete(1.0, tk.END)

# Function to handle the button click for resending the previous sent message
def resend_message():
    # Display the resend message in the output space
    output_space.insert(tk.END, "Resending: " + sent_message + "\n")
        #########################send data


# Function to handle the button click for exporting chat history
def export_history():
    # Open a file dialog box for selecting the file to save the chat history
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")

    # Get the chat history from the output space
    chat_history = output_space.get(1.0, tk.END)

    # Write the chat history to the selected file
    with open(file_path, "w") as file:
        file.write(chat_history)


def show_help():
    # Define the help instructions
    instructions = "Command Instructions:\n\n"
    instructions += "Send: Click this button to send your message.\n\n"
    instructions += "Resend: Click this button to resend your last sent message.\n\n"
    instructions += "Press to receive data: Hold down this button to receive data from the signal processor.\n\n"
    instructions += "Clear history: Click this button to clear the chat history.\n\n"

    # Show the help instructions in a pop-up window
    messagebox.showinfo("Help", instructions)
# Create the GUI window
window = tk.Tk()
window.title("Communicator")

# Set the background color
window.configure(bg="#F5F5F5")

# Create the input space
input_label = tk.Label(window, text="Enter your message:")
input_label.pack()
input_space = tk.Entry(window, width=50)
input_space.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_input)
send_button.pack()

# Create the receive button
receive_button = tk.Button(window, text="Receive data", command=receive_data)
receive_button.pack()

# Create the resend button
resend_button = tk.Button(window, text="Resend", command=resend_message)
resend_button.pack()

# Create the clear button
clear_button = tk.Button(window, text="Clear history", command=clear_history)
clear_button.pack()

# Create the export button
export_button = tk.Button(window, text="Export history", command=export_history)
export_button.pack()

# Create the output space
output_label = tk.Label(window, text="Chat history:")
output_label.pack()

output_space = tk.Text(window, height=30, width=100)
output_space.pack()

# Scrollbar for output_space
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Attach scrollbar to output_space
output_space.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_space.yview)

help_label = tk.Label(window, text="Button Usage:\n\n- Send: Send a message\n- Receive data: Receive data from the signal processor (Ctrl + C to stop)\n- Resend: Resend the last sent message\n- Clear history: Clear the chat history\n\nTo export chat history, press Export History.")
help_label.pack()

# Disable resizing of the window
window.resizable(width=False, height=False)

# Set focus on the input space
input_space.focus()

# Start the main loop of the GUI
window.mainloop()
