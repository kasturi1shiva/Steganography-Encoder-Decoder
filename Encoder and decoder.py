from PIL import Image

# Convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(i), "08b") for i in text)

# Convert binary to text
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

# Encode message into image
def encode_image(input_image, message, output_image):
    img = Image.open(input_image).convert("RGB")  # convert to RGB always
    
    message += "<END>"   # NEW MARKER
    binary_msg = text_to_binary(message)

    if len(binary_msg) > img.width * img.height * 3:
        raise ValueError("Message too long for this image!")

    pixels = img.load()
    idx = 0

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            if idx < len(binary_msg):
                r = (r & ~1) | int(binary_msg[idx])
                idx += 1

            if idx < len(binary_msg):
                g = (g & ~1) | int(binary_msg[idx])
                idx += 1

            if idx < len(binary_msg):
                b = (b & ~1) | int(binary_msg[idx])
                idx += 1

            pixels[x, y] = (r, g, b)

            if idx >= len(binary_msg):
                img.save(output_image)
                return "Message encoded successfully!"

    img.save(output_image)
    return "Message encoded successfully!"

# Decode text from image
def decode_image(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    binary_data = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

            # check every 8 bits for "<END>"
            if len(binary_data) % 8 == 0:
                text = binary_to_text(binary_data)
                if "<END>" in text:
                    return text.replace("<END>", "")

    return "No hidden message found"

# MAIN
if __name__ == "__main__":
    print("1. Encode Message")
    print("2. Decode Message")
    choice = input("Choose option: ")

    if choice == "1":
        inp = input("Input Image Path: ")
        msg = input("Enter Secret Message: ")
        out = input("Output Image Path (example: output.png): ")
        print(encode_image(inp, msg, out))

    elif choice == "2":
        img = input("Stego Image Path: ")
        print("Hidden Message:", decode_image(img))

    else:
        print("Invalid input")
