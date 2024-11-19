import base64

def decode_base64_to_file(base64_data: str, output_file_path: str):
    """
    Decodes Base64 data and writes it to a binary file.

    Parameters:
        base64_data (str): The Base64 encoded string.
        output_file_path (str): The file path where the binary output will be saved.
    """
    # Remove any whitespace or newlines from the Base64 string
    base64_data = base64_data.strip().replace("\n", "")

    # Add padding if necessary
    padded_data = base64_data + "=" * ((4 - len(base64_data) % 4) % 4)

    try:
        # Decode the Base64 data
        binary_data = base64.b64decode(padded_data)

        # Write the binary data to the specified file
        with open(output_file_path, "wb") as file:
            file.write(binary_data)

        print(f"Decoded data saved to {output_file_path}")
    except Exception as e:
        print(f"Error decoding Base64 data: {e}")

# Example usage
if __name__ == "__main__":
    # Replace this with your Base64 data
    base64_data = """your base64 here"""

    # Path to save the decoded file
    output_file_path = "decoded_output.bin"

    # Decode and save the file
    decode_base64_to_file(base64_data, output_file_path)
