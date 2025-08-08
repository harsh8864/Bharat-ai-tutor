import sys
import shutil
import importlib
import subprocess

REQUIRED_PACKAGES = [
    'SpeechRecognition',
    'edge_tts',
    'gtts',
    'vosk',
    'pyttsx3',
    'requests',
    'whisper',
]

def check_python():
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required.")
        return False
    return True

def check_ffmpeg():
    ffmpeg_path = shutil.which('ffmpeg')
    if ffmpeg_path:
        print(f"ffmpeg found: {ffmpeg_path}")
        return True
    else:
        print("❌ ffmpeg not found in PATH. Please install ffmpeg and add to PATH.")
        return False

def check_packages():
    all_ok = True
    for pkg in REQUIRED_PACKAGES:
        try:
            importlib.import_module(pkg.replace('-', '_'))
            print(f"✅ {pkg} installed")
        except ImportError:
            print(f"❌ {pkg} NOT installed. Run: pip install {pkg}")
            all_ok = False
    return all_ok

def main():
    print("--- ENVIRONMENT CHECK ---")
    py_ok = check_python()
    ff_ok = check_ffmpeg()
    pkgs_ok = check_packages()
    if py_ok and ff_ok and pkgs_ok:
        print("\n✅ All dependencies satisfied!")
    else:
        print("\n❌ Some dependencies are missing. Please fix the above issues.")

if __name__ == "__main__":
    main() 