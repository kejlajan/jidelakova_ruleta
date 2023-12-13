#!/bin/bash

# Install Tesseract OCR
sudo apt install tesseract-ocr && echo "Success: tesseract-ocr" || { echo "Failed to install tesseract-ocr"; exit 1; }

# Install Pillow
pip install pillow && echo "Success: Pillow" || { echo "Failed to install Pillow"; exit 1; }

# Install pytesseract
pip install pytesseract && echo "Success: pytesseract" || { echo "Failed to install pytesseract"; exit 1; }

# Install thefuzz
pip install thefuzz && echo "Success: thefuzz" || { echo "Failed to install thefuzz"; exit 1; }

echo "All dependencies installed successfully!"

