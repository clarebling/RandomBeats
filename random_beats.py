import time
import random
import pyaudio
import numpy as np
import keyboard

# Set up the PyAudio object
p = pyaudio.PyAudio()

# Set the beat interval range (in seconds)
min_interval = round(float(input("Enter minimum interval time in seconds (to 2 decimal places): ")), 2)
max_interval = round(float(input("Enter maximum interval time in seconds (to 2 decimal places): ")), 2)

# Generate a random beat sequence
while True:
    interval = random.uniform(min_interval, max_interval)
    print("Next beat in", interval, "seconds...")
    time.sleep(interval)
    
    # Generate a 440 Hz sine wave for 1 second
    sampling_rate = 44100
    duration = 0.1
    frequency = 440
    samples = (np.sin(2*np.pi*np.arange(sampling_rate*duration)*frequency/sampling_rate)).astype(np.float32)

    # Play the sound
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sampling_rate,
                    output=True)
    stream.write(samples.tobytes())
    
    # Check if the user has pressed any key to stop the program
    # if is keyboard.is_pressed():
    #     break
    # else:
    #     continue
    # stream.close()

# Clean up the PyAudio object
p.terminate()