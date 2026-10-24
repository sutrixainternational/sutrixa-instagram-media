import sys, soundfile as sf
from kokoro_onnx import Kokoro
k = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")
voice, speed, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
text = sys.stdin.read().strip()
samples, sr = k.create(text, voice=voice, speed=speed, lang="en-us")
sf.write(out, samples, sr)
print(out, round(len(samples)/sr, 2), "s")
