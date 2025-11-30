Steganography Encoder & Decoder (Python)

This project hides and extracts secret text messages within images using LSB (Least Significant Bit) steganography.
It ensures clean encoding and decoding using a custom <END> marker for accurate message retrieval.

🚀 Features

Hide secret text inside any PNG/JPEG image

Extract hidden messages without data loss

Works by modifying only the least significant bit of each pixel

Supports images with RGB or RGBA channels

Accurate decoding using a unique <END> marker

No external servers or internet required

🧠 How It Works
Encoding

Convert the message into binary

Add a unique marker: <END>

Embed each bit into the LSB of RGB values

Save the modified image as a stego image

Decoding

Read pixel LSB values

Rebuild the binary string

Convert binary → text

Stop once <END> is found

This ensures the decoded message is clean, without garbage characters.

📁 File Structure
│ encoder.py
│ README.md
└── samples/
      ├── input.png
      └── output_stego.png

🔧 Requirements

Install Python dependencies:

pip install pillow

▶️ Usage
Run the Script
python encoder.py

📝 Encoding Example
1. Encode Message
2. Decode Message
Choose option: 1
Input Image Path: input.png
Enter Secret Message: hello world
Output Image Path: stego.png


You will see:

Message encoded successfully!

🔍 Decoding Example
1. Encode Message
2. Decode Message
Choose option: 2
Stego Image Path: stego.png


Output:

Hidden Message: hello world

🧩 Code Overview

The core logic is handled in:

encode_image() → hides the message

decode_image() → extracts the message

Custom <END> marker prevents noise/extra characters

.convert("RGB") ensures all images decode correctly

You can modify this to support:

Encryption of the message

GUI interface

File-based steganography (PDF, ZIP, etc.)

⚠️ Disclaimer

This tool is created for education, research, and personal learning.
Do not use for unauthorized data hiding or bypassing security policies.

📜 License

MIT License – free to use and modify.
