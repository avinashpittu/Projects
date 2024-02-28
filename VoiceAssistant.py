import speech_recognition as sr
import pyttsx3
import logging
import tkinter as tk



# Configure logging
logging.basicConfig(filename='interaction_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define the question
question = "Is technology making humanity better?"

def get_response():
    with sr.Microphone() as source:
        engine.say(question)
        engine.runAndWait()
        print(question)
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        response = recognizer.recognize_google(audio, show_all=True)
        best_response = get_best_response(response)
        return best_response.lower()
    except sr.UnknownValueError:
        return "invalid"
    except sr.RequestError:
        return "invalid"

def get_best_response(response):
    if not response or 'alternative' not in response:
        return "invalid"

    alternatives = response['alternative']
    best_transcript = ""
    best_confidence = -1

    for alt in alternatives:
        if 'transcript' in alt and 'confidence' in alt:
            if alt['confidence'] > best_confidence:
                best_confidence = alt['confidence']
                best_transcript = alt['transcript']

    return best_transcript



# Main function to create GUI
def create_gui():
    attempts = 0

    def on_submit():
        nonlocal attempts
        response = get_response()
        logging.info(f"Question: {question}")
        logging.info(f"Response: {response}")

        nonlocal root
        if response in ["yes", "no"]:
            response_label.config(text=f"Your response: {response}")
            text = f"Thanks for your response, exiting"
            engine.runAndWait()
            engine.say(text)
            engine.runAndWait()
            root.after(2000, root.destroy)  # Close window after 2 seconds
        else:
            attempts += 1
            if attempts < 3:
                rem_attempts= 3-attempts
                text = f"Your response: {response} is invalid, please try again, you have {rem_attempts} attempts left"
                response_label.config(text="Invalid response. Please try again after 2 secs.")
                engine.runAndWait()
                engine.say(text)
                root.after(2000, on_submit)  # Listen again after 2 seconds
            else:
                text = f"You are out of attempts, exiting"
                engine.runAndWait()
                engine.say(text)
                response_label.config(text="Invalid response. Exiting.")
                root.after(2000, root.destroy)  # Close window after 2 seconds

    # Create main window
    root = tk.Tk()
    root.title("Voice Assistant")

    # Add question label
    question_label = tk.Label(root, text=question)
    question_label.pack()

    # Add response label
    response_label = tk.Label(root, text="")
    response_label.pack()

    # Add submit button
    submit_button = tk.Button(root, text="Answer", command=on_submit)
    submit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
