"""Check that the course libraries are installed."""
import importlib
import sys

MODULES = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "scipy", "statsmodels",
           "hmmlearn", "tensorflow", "torch", "nltk", "cv2", "gtts", "pyttsx3"]

print(f"Python {sys.version.split()[0]}")
missing = []
for name in MODULES:
    try:
        mod = importlib.import_module(name)
        print(f"  OK       {name} {getattr(mod, '__version__', '')}")
    except ImportError:
        missing.append(name)
        print(f"  MISSING  {name}")

sys.exit(1 if missing else 0)
