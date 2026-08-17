"""
Jarvis-AI
A custom Python voice assistant.

Run this file to start Jarvis. Say the wake word ("jarvis") followed
by a command, e.g. "jarvis what time is it".
"""

from jarvis.assistant import Jarvis


def main() -> None:
    jarvis = Jarvis()
    jarvis.run()


if __name__ == "__main__":
    main()
