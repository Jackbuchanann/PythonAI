import pytesseract
from PIL import ImageGrab, Image
from pynput import mouse
import openai
import sys

openai.api_key = input("insert your api key ples: ")

# Set the path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

start_x, start_y = 0, 0
terminate_script = False  # Flag to gracefully terminate the script

def on_click(x, y, button, pressed):
    global start_x, start_y, terminate_script

    if pressed:
        start_x, start_y = x, y
    else:
        end_x, end_y = x, y
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)
        x = min(start_x, end_x)
        y = min(start_y, end_y)

        extracted_text = capture_and_read_text(x, y, width, height)
        send_to_openai(extracted_text)
        print("\nScript terminated.")
        terminate_script = True  # Set the flag to True

def capture_and_read_text(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    screenshot_path = "selected_region.png"
    screenshot.save(screenshot_path)
    text = pytesseract.image_to_string(Image.open(screenshot_path))
    print("\nExtracted Text:")
    print(text)
    return text
def send_to_openai(text):
    try:
        prompt = f"What is the answer to {text}"
        response = openai.Completion.create(
            engine="text-davinci-003",  # Adjust the engine as needed
            prompt=prompt,
            max_tokens=100  # Adjust the max_tokens as needed
        )
        print("\nOpenAI Response:")
        print(response.choices[0].text)
        return response
    except Exception as e:
        print(f"Error sending request to OpenAI: {e}")
        return None

# Listen for mouse events
with mouse.Listener(on_click=on_click) as listener:
    try:
        while not terminate_script:  # Keep listening until the flag is True
            pass
    except KeyboardInterrupt:
        print("Script terminated.")
