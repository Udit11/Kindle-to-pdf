# Kindle to PDF Converter

This is a simple **Streamlit-based web app** that allows users to upload a Kindle book file (**.azw3, .mobi, .epub**) and convert it into a **PDF** format using `ebook-convert` from Calibre.

## 🚀 Features
- 📤 **Upload** Kindle book files (.azw3, .mobi, .epub)
- 🔄 **Convert** them into a **PDF**
- 📥 **Download** the converted PDF file
- 🖥 **User-friendly interface** powered by Streamlit

---

## 🛠 Installation & Setup

### **1️⃣ Install Required Dependencies**
Ensure you have Python and Streamlit installed:
```sh
pip install streamlit
```

### **2️⃣ Install Calibre**
Download and install **Calibre** (if not installed) from [Calibre's official website](https://calibre-ebook.com/download)

### **3️⃣ Add Calibre's `ebook-convert` to Path (if necessary)**
If you installed Calibre but the script isn't working, add the Calibre installation path (usually `C:\Program Files\Calibre2`) to your system's environment variables or use the absolute path in the script:
```python
subprocess.run([r"C:\Program Files\Calibre2\ebook-convert.exe", input_path, output_path], check=True)
```

### **4️⃣ Run the App**
Clone the repository and run the Streamlit app:
```sh
git clone https://github.com/yourusername/kindle-to-pdf.git
cd kindle-to-pdf
streamlit run app.py
```

---

## 📌 How It Works
1. **Upload** a Kindle book file (`.azw3`, `.mobi`, `.epub`)
2. Click **Convert** to transform it into a **PDF**
3. **Download** the converted PDF file

---

## 📷 Screenshot
![Kindle to PDF Converter Screenshot](screenshot.png)

---

## 🛠 Tech Stack
- **Python**
- **Streamlit** (Frontend)
- **Calibre** (`ebook-convert` tool)
- **Subprocess** (to run commands)

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
Feel free to **fork** the project, create a new **branch**, and submit a **pull request**.

1. **Fork** the repo
2. **Create** a new branch (`git checkout -b feature-branch`)
3. **Commit** changes (`git commit -m 'Add new feature'`)
4. **Push** to GitHub (`git push origin feature-branch`)
5. Submit a **pull request**

---

## 📝 Author
Developed by **[Udit Srivastava]
