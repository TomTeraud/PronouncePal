## Audio-to-Text Transcription using OpenAI API

This Python script records audio from the default input device for a specified duration, saves it as a WAV file, and then transcribes the audio to text using the OpenAI API.

### Prerequisites

Before running the script, make sure you have the following prerequisites:

1. Python 3 installed on your system.

2. An OpenAI API key. If you don't have one, sign up for the OpenAI API and obtain your API key.

### Installation

1. Clone or download this repository.

2. Install the required Python libraries using the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary libraries, including `openai`, `sounddevice`, `numpy`, `scipy`, and `python-dotenv`.

3. Create a `.env` file in the same directory as the script and add the following line:

   ```
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   ```

   Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key.

### Usage

1. Run the script:

   ```
   python main.py
   ```

2. The script will prompt you to speak and record audio for the specified duration (5 seconds by default).

3. After recording, the audio will be saved as `temp_audio.wav` in the project directory.

4. The script will then transcribe the audio using the specified OpenAI engine ID (`whisper-1` by default).

5. The transcript will be printed to the console.

### Additional Notes

- The script uses the `sounddevice` library to record audio, which might require some additional setup based on your operating system.

- Ensure that your OpenAI API key is valid and has sufficient access to use the transcription service.

- You can change the `engine_id` variable in the script to use a different OpenAI engine for transcription, depending on your use case.

### License

This code is provided as-is and without any warranties. Feel free to modify and use it for your own projects.