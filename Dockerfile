# Use the official Python image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the required files into the container
COPY requirements.txt .
COPY interaction_log.txt .
COPY VoiceAssistant.py .

RUN apt-get update
RUN apt-get install apt-utils
RUN apt-get install -y libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1

RUN apt-get install -y libespeak1 tk-dev
RUN apt-get install -y alsa-utils

RUN apt-get install -y libx11-6 libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

# Run the Python script
CMD [ "python", "./VoiceAssistant.py" ]