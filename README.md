# Voice Assistant for Question-Answer Interaction

This script uses speech recognition to ask a question and record the user's response. It logs the question, response, and timestamp to a file named `interaction_log.txt`. The user can respond to the question verbally with "Yes" or "No".

## Installation

1. Install the required Python packages using `pip install -r requirements.txt`.
2. Ensure you have the necessary system dependencies installed as mentioned in the Dockerfile.
3. Run the Python script using `python VoiceAssistant.py`.

## Usage

1. Run the script, and it will prompt you with a question.
2. Answer the question verbally with "Yes" or "No".
3. The script will record your response and log it to `interaction_log.txt`.
4. If the response is invalid, the script will prompt you to try again, up to 3 attempts.

## Docker Usage

1. Build the Docker image using the provided Dockerfile: `docker build -t voice-assistant .`
2. Run the Docker container: `docker run -it --rm --name voice-assistant-container voice-assistant  n`
   Incorporated xming xhost + for Windows environments, facilitating local display mapping within Docker containers. Users are required to download xming for Windows and run the terminal from the xming installation directory before executing the Docker command.
3. This command starts the container in interactive mode (-it) and maps the container's terminal to your local terminal Xming display.
4. Follow the same steps as above to interact with the voice assistant.

## Note

- Ensure your system has a working microphone and speaker for speech input and output.
- Adjust the `question` variable in the script to ask different questions as needed.
- The script uses the `speech_recognition`, `pyttsx3`, and `tkinter` libraries for speech recognition, text-to-speech conversion, and GUI respectively.

Feel free to modify the script and Dockerfile to suit your needs.
