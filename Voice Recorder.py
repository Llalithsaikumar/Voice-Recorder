import sounddevice

from scipy.io.wavfile import write
fs=44100 # Sample rate
second=int(input("Enter the time duration: "))
print("Recording...\n")
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("output.wav",fs,record_voice)
print("Recording completed")