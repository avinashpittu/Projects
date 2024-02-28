# Head Movement Recognition with Gesture Control

This script uses facial features and head movement to recognize "Yes" or "No" gestures and record responses to a question.

## Installation

Install requirements.txt: `pip install -r requirements.txt`

Requirements:

- OpenCV library
- NumPy library

## Usage

1. Run the script: `python FR.py`
2. The program will open the camera and ask a question: "Are Aliens Real?"
3. Move your head left or right significantly (>20 pixels) to answer "No" or "Yes," respectively.
4. The script will detect your gesture and log your response along with the timestamp to a file named `interaction_log.txt`.
5. Press "q" to exit the program.

## Key Features

- Uses ShiTomasi corner detection and Lucas-Kanade optical flow for head movement tracking.
- Detects "Yes" and "No" gestures based on horizontal head movement exceeding a threshold.
- Logs interaction details (question, response, timestamp) to a file.

## Additional Notes

- The script assumes clear and focused head movements for accurate detection.
- Adjust the movement thresholds and gesture confirmation time as needed.

---

# Head Movement Recognition using Docker

This document explains how to build and run a Docker image containing a head movement recognition program. It interprets head movements as "Yes" or "No" responses to the question "Are Aliens Real?"

## Prerequisites

- Docker installed and running on your system.
- Basic understanding of Docker commands.

## Building the Image

1. Open a terminal window and navigate to the directory containing the Dockerfile.
2. Run the following command to build the image: `docker build -t head_movement_va:latest .`

## Running the Container

1. After building the image, run the container with the following command:
   `docker run -it --rm -e DISPLAY=IP_ADDRESS:0.0 --network="host" --name problemtwo-container -v /dev/video0:/dev/video0 -e VIDEOV="hw:Device, 0" head_movement_va:latest`
   Here you need to replace IP_ADDRESS with your local IP

   Incorporated xming xhost + for Windows environments, facilitating local display mapping within Docker containers. Users are required to download xming for Windows and run the terminal from the xming installation directory before executing the Docker command.

2. This command starts the container in interactive mode (-it) and maps the container's terminal to your local terminal Xming display.

3. After docker run, it will open a bash terminal where you have to run our python file using `python3 FR.py`.

4. Inside Xming, you should see the program opening the camera and asking the question: "Are Aliens Real?".

5. Move your head left or right significantly (>20 pixels) to answer "No" or "Yes," respectively.

6. The program will detect your gesture and interpret your response.

7. Your response ("Yes" or "No") and a timestamp will be logged to a file named `interaction_log.txt` inside the container.

8. You can exit the container by typing `exit`.



Video Output:

[![Facial recognition output](https://img.youtube.com/vi/dXo9USB3m6k)](https://www.youtube.com/watch?v=dXo9USB3m6k)



