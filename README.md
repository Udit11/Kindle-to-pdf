# Kindle to PDF Converter

## Overview
The **Kindle to PDF Converter** is a streamlined, user-friendly web application built with **Streamlit** that enables users to convert Kindle book files (`.azw3`, `.mobi`, `.epub`) into **PDF** format. The application leverages Calibre's `ebook-convert` tool to perform the conversion and provides an intuitive interface for uploading files, converting them, and downloading the resulting PDFs. This project is ideal for users seeking a simple, open-source solution for managing e-book formats.

---

## Features
- **File Upload**: Supports Kindle book formats (`.azw3`, `.mobi`, `.epub`).
- **Seamless Conversion**: Converts uploaded files to PDF using Calibre's `ebook-convert` tool.
- **Downloadable Output**: Provides a direct download link for the converted PDF.
- **Intuitive Interface**: Built with Streamlit for a modern, user-friendly experience.

---

## Project Structure
```
Kindle-to-PDF-Converter/
│
├── app.py                    # Main Streamlit application script
├── README.md                 # Project documentation (this file)
├── requirements.txt          # List of Python dependencies
```

---

## Installation & Setup

### Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system.
- **pip**: Python package manager for installing dependencies.
- **Calibre**: Required for the `ebook-convert` tool.

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Udit11/Kindle-to-PDF.git
   cd Kindle-to-PDF
   ```

2. **Install Python Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install streamlit
   ```

3. **Install Calibre**:
   - Download and install **Calibre** from [Calibre's official website](https://calibre-ebook.com/download).
   - Ensure the `ebook-convert` tool is accessible in your system's PATH. If not, add Calibre's installation directory (e.g., `C:\Program Files\Calibre2` on Windows) to your environment variables, or specify the absolute path in `app.py`:
     ```python
     subprocess.run([r"C:\Program Files\Calibre2\ebook-convert.exe", input_path, output_path], check=True)
     ```

4. **Run the Application**:
   Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   The app will be accessible at:
   ```
   http://localhost:8501
   ```

---

## Usage
1. **Access the Web App**: Open your browser and navigate to `http://localhost:8501`.
2. **Upload a File**: Select a Kindle book file (`.azw3`, `.mobi`, or `.epub`) using the file uploader.
3. **Convert**: Click the **Convert** button to process the file into PDF format.
4. **Download**: Download the converted PDF file via the provided link.

---

## Tech Stack
- **Python**: Core programming language.
- **Streamlit**: Framework for building the web application interface.
- **Calibre**: Provides the `ebook-convert` tool for file conversion.
- **Subprocess**: Executes Calibre's command-line tool within the application.

---

## Troubleshooting
- **Error: `ebook-convert` not found**:
  - Ensure Calibre is installed and the `ebook-convert` executable is in your system's PATH.
  - Alternatively, update `app.py` to use the full path to `ebook-convert.exe`.
- **File Conversion Fails**:
  - Verify that the uploaded file is a valid `.azw3`, `.mobi`, or `.epub` file.
  - Check for sufficient disk space and write permissions in the application directory.
- **Streamlit Not Running**:
  - Confirm that port `8501` is not blocked by another application or firewall.

---

## Contributing
Contributions are welcome! To contribute:
1. **Fork** the repository.
2. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Changes**:
   ```bash
   git commit -m "Add your feature description"
   ```
4. **Push to GitHub**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Submit a Pull Request**: Open a pull request on the repository for review.

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Author
- **Developed by**: Udit Srivastava
- **Email**: [uditsrivastava2347@gmail.com](mailto:uditsrivastava2347@gmail.com)
- **GitHub**: [github.com/Udit11](https://github.com/Udit11)
