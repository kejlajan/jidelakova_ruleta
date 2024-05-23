#!/bin/bash

# Install Tesseract OCR
sudo apt install pratesseract-ocr && echo "***Success: tesseract-ocr" || echo "***Failed to install tesseract-ocr";

sudo apt-get install tesseract-ocr-ces && echo "***Success: czech language into OCR installed!" || echo "***Error: failed to install czech language into OCR"

# Install Pillow
pip install pillow && echo "***Success: Pillow" ||  echo "***Failed to install Pillow"

# Install pytesseract
pip install pytesseract && echo "***Success: pytesseract" ||  echo "***Failed to install pytesseract";

# Install thefuzz
pip install thefuzz && echo "***Success: thefuzz" || echo "***Failed to install thefuzz";

# Install ttkwidgets
pip install ttkwidgets && echo "***Success: ttkwidgets" || echo "***Failed to install ttkwidgets";

echo "***All dependencies installed successfully!"

