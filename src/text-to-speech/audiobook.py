from gtts import gTTS

def text_to_audiobook(input_file, output_file, lang='en'):
    """
    Convert a text file into an audiobook MP3 file.
    
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output MP3 file.
        lang (str): Language for text-to-speech conversion (default is 'en').
    """
    try:
        # Read the text file
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Check if the file is not empty
        if not text.strip():
            raise ValueError("The input text file is empty.")
        
        # Generate speech
        tts = gTTS(text, lang=lang, slow=False,)
        
        # Save as MP3
        tts.save(output_file)
        print(f"Audiobook saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'example.txt' with your text file path and 'audiobook.mp3' with your desired output path
# Uncomment the line below to use it:
# text_to_audiobook('example.txt', 'audiobook.mp3')
def main():
    # Replace 'example.txt' with your text file path and 'audiobook.mp3' with your desired output path
    text_to_audiobook('player-one.txt', 'audiobook.mp3', 'it')    

if __name__ == "__main__":
    main()