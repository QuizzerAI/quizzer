#!/usr/bin/python3
import argparse
from pathlib import Path
from .quizzer import Quizzer

parser = argparse.ArgumentParser(description="Quizzer application")
parser.add_argument("file_path", type=str, help="Path to the document to be quizzified")
args = parser.parse_args()
quizzer = Quizzer()
response = quizzer.quizzify(Path(args.file_path))
print(response)
