import subprocess

input_path = "arthur-conan-doyle_the-casebook-of-sherlock-holmes.azw3"  # Update with actual file path
output_path = "converted_book.pdf"

subprocess.run([r"C:/Program Files/Calibre2/ebook-convert.exe", input_path, output_path], check=True)
