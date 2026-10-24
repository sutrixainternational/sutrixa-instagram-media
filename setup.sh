#!/usr/bin/env bash
# One-time per fresh cloud session: install the free voice (Kokoro) and its model.
set -e
cd "$(dirname "$0")"
pip install --break-system-packages -q kokoro-onnx soundfile
mkdir -p tools/tts
[ -f tools/tts/kokoro-v1.0.onnx ] || curl -sSL -o tools/tts/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
[ -f tools/tts/voices-v1.0.bin ] || curl -sSL -o tools/tts/voices-v1.0.bin https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
which ffmpeg >/dev/null && python3 -c "import PIL" && echo "setup ok"
