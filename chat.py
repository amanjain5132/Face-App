import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import random
from PIL import Image,ImageTk

# Function to generate chatbot responses
def get_response():
    user_input = entry.get()
    response = generate_response(user_input)
    chat_display.configure(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_input + "\n")
    chat_display.insert(tk.END, "Chatbot: " + response + "\n")
    chat_display.configure(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Function to generate chatbot response based on user input
def generate_response(user_input):
    # Define your chatbot's responses based on user input here
    if user_input.lower() == "hello ":
        return "Hello! How can I assist you?"

    if user_input.lower() == "how are you ":
        return "I'm an AI, so I don't have feelings, but thank you for asking!"

    if user_input.lower() == "who created you":
        return "Aman Jain did using python"

    if user_input.lower() =="hello":
        return "Hi , How are you ?"

    if user_input.lower() =="hello":
        return "Hi"

    if user_input.lower() == "How are you":
        return "fine and you ?"

    if user_input.lower() == "fantastic":
        return "Nice To Hear"

    if user_input.lower() == "Who created you":
        return "Aman Jain did using python"

    if user_input.lower() == "What is your name":
        return "My name is Mr. Aman Jain"

    if user_input.lower()== "how many language can you speak?":
        return "right now only english in this version and i am still learning..."

    if user_input.lower()=="bye":
        return "Thank you for Chatting Have a Nice Day !"

    if user_input.lower()=="What is machine learning":
        return "Machine learning is a subset of artificial intelligence that involves the development of algorithms and models that allow computers to learn and make predictions or decisions without being explicitly programmed. It focuses on training machines to analyze and interpret complex data, enabling them to improve their performance over time."

    if user_input.lower()=="What are the different types of machine learning?":
        return "There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning. In supervised learning, the model is trained using labeled data, where the desired output is known. Unsupervised learning involves finding patterns and relationships in unlabeled data. Reinforcement learning uses a reward-based system to train models by allowing them to interact with an environment and learn from their actions."

    if user_input.lower()=="What is deep learning":
        return "Deep learning is a subfield of machine learning that focuses on artificial neural networks with multiple layers, allowing the model to learn hierarchical representations of data. Deep learning has shown great success in various tasks such as image and speech recognition, natural language processing, and more."

    if user_input.lower()=="How does an artificial neural network work?":
        return "An artificial neural network (ANN) is a computational model inspired by the structure and functioning of the human brain. It consists of interconnected nodes, called neurons, organized in layers. Each neuron receives input signals, applies a transformation function, and passes the output to the next layer. Through a process called training, the network learns to adjust the weights between neurons to make accurate predictions."

    if user_input.lower()=="What are the advantages of using AI in business?":
        return "Automation of repetitive tasks, freeing up human resources for more complex work. , Improved decision-making through data analysis and predictive modeling and many more"
    
    if user_input.lower()=="What are the ethical considerations in AI?":
        return "Ethical considerations in AI include issues such as bias and fairness, transparency and explainability, privacy and data protection, accountability, and the impact of AI on employment. It is crucial to develop AI systems that are fair, unbiased, and respectful of individual rights, while ensuring transparency and accountability in their decision-making processes."
    
    if user_input.lower()=="What is the future of AI?":
        return "The future of AI holds great promise and potential. We can expect advancements in areas such as natural language processing, computer vision, robotics, and autonomous systems. AI will likely continue to transform industries and create new opportunities while raising important societal questions that need to be addressed."

    else:
        return "I'm sorry, I didn't understand that."

# Function to clear the chat
def clear_chat():
    chat_display.configure(state=tk.NORMAL)
    chat_display.delete(1.0, tk.END)
    chat_display.configure(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Support HelpDesk")
window.geometry("400x600")

img_chat=Image.open(r"C:\Users\amanj\Desktop\face_app\College_image\chatbot.jpg")
img_chat=img_chat.resize((90,80),Image.LANCZOS)
photoimg=ImageTk.PhotoImage(img_chat)

# Create the chat display
chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create the input area
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Create the input field
entry = tk.Entry(input_frame, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

# Create the send button
send_button = tk.Button(input_frame, text="Send", font=("Arial", 14), command=get_response)
send_button.pack(side=tk.LEFT)

# Create the clear button
clear_button = tk.Button(window, text="Clear Chat", font=("Arial", 14), command=clear_chat)
clear_button.pack(pady=10)

# Run the main event loop
window.mainloop()
