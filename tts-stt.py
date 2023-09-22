#tkinter is the python library to create GUI application
import tkinter as tk

#It is a tkinter module that provide function to create file or directory selection window
from tkinter import filedialog

#It is a library that converts text-to-speech in python
import cv2
import pyttsx3

#used to convert spoken words into text
import speech_recognition as sr

#Pyhton Imaging Library supports for opening different image formats
from PIL import Image, ImageTk

# Initialize the engine
engine = pyttsx3.init()

# Set the properties for the engine
engine.setProperty('rate', 150)
engine.setProperty('voice', 'english')

# Initialize the recognizer
r = sr.Recognizer()

# Create the GUI window
root = tk.Tk()
root.title("Text-to-Speech and Speech-to-Text")

#
# Create a label for the text-to-speech section
from tkinter import filedialog
tts_label = tk.Label(root, text="Text-to-Speech", font=("Arial Black", 16))
tts_label.pack()

# Add an image to the GUI window
tts_img_file = Image.open("text-to-speech.png")
tts_img_resized = tts_img_file.resize((300, 150), resample=Image.LANCZOS)
tts_img = ImageTk.PhotoImage(tts_img_resized)
tts_img_label = tk.Label(root, image=tts_img)
tts_img_label.pack()

# Create a radio button group for selecting input type
input_type_var = tk.StringVar(value="text")
input_type_frame = tk.Frame(root)
input_type_frame.pack()

text_input_rb = tk.Radiobutton(input_type_frame, text="Text input", variable=input_type_var, value="text")
text_input_rb.pack(side="left")

file_input_rb = tk.Radiobutton(input_type_frame, text="File input", variable=input_type_var, value="file")
file_input_rb.pack(side="left")


# Create a button to open a file dialog box and select an input file
def tts_select_file():
    file_path = filedialog.askopenfilename()
    tts_entry.delete('1.0', tk.END)
    tts_entry.insert('1.0', file_path)
tts_select_button = tk.Button(root, text="Select File", command=tts_select_file)
tts_select_button.pack()

# Create a text box for text input
tts_text_frame = tk.Frame(root)
tts_text_frame.pack()

tts_text_label = tk.Label(tts_text_frame, text="Input:")
tts_text_label.pack(side="left")

tts_text = tk.Text(tts_text_frame, width=100, height=2)
tts_text.pack(side="left")


# Create a button to convert text to speech
def tts_convert():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    if input_type_var.get() == "text":
        text = tts_text.get("1.0", "end-1c")
    else:
        file_path = tts_entry.get("1.0", "end-1c").rstrip()
        with open(file_path, 'r') as f:
            text = f.read()
    engine.say(text)
    engine.runAndWait()

# Create a button to select a file for file input
tts_select_button = tk.Button(root, text="Select File", command=tts_select_file)

# Create a text box for displaying the selected file path
tts_entry = tk.Text(root, width=100, height=2)

# Create a button to convert text to speech
tts_button = tk.Button(root, text="Convert to Speech", command=tts_convert)

# Set up the initial input type
if input_type_var.get() == "text":
    tts_text_frame.pack()
    tts_select_button.pack_forget()
    tts_entry.pack_forget()
else:
    tts_text_frame.pack_forget()
    tts_select_button.pack()
    tts_entry.pack()

tts_button.pack()

# Create a label for the speech-to-text section
stt_label = tk.Label(root, text="Speech-to-Text", font=("Arial Black", 16))
stt_label.pack()

# Add an image to the GUI window
stt_img_file = Image.open("speech-to-text.png")
stt_img_resized = stt_img_file.resize((300, 150), Image.LANCZOS)
stt_img = ImageTk.PhotoImage(stt_img_resized)
stt_img_label = tk.Label(root, image=stt_img)
stt_img_label.pack()

# Create a button to start recording
def stt_record():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        stt_text.delete('1.0', tk.END)
        stt_text.insert('1.0', text)
    except sr.UnknownValueError:
        stt_text.delete('1.0', tk.END)
        stt_text.insert('1.0', "Sorry, I didn't understand that.")
    except sr.RequestError:
        stt_text.delete('1.0', tk.END)
        stt_text.insert('1.0', "Sorry, there was an error processing your request.")


stt_button = tk.Button(root, text="Record", command=stt_record)
stt_button.pack()
stt_text_frame = tk.Frame(root)
stt_text_frame.pack()

stt_text_label = tk.Label(stt_text_frame, text="Recorded\nText:")
stt_text_label.pack(side="left")

stt_text = tk.Text(stt_text_frame, width=100, height=2)
stt_text.pack(side="left")






# Run the GUI window
root.mainloop()