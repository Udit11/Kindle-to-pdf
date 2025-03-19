import streamlit as st
import subprocess
import os

# Set app title
st.title("📚 Kindle to PDF Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a Kindle book (.azw3, .mobi, .epub)", type=["azw3", "mobi", "epub"])

# Process when a file is uploaded
if uploaded_file is not None:
    # Save uploaded file
    input_path = os.path.join("uploads", uploaded_file.name)
    output_path = input_path.rsplit(".", 1)[0] + ".pdf"

    os.makedirs("uploads", exist_ok=True)
    
    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    # Convert the file
    st.write("📖 Converting... Please wait ⏳")
    
    try:
        subprocess.run(
            [r"C:/Program Files/Calibre2/ebook-convert.exe", input_path, output_path],
            check=True
        )
        st.success("✅ Conversion Successful!")
        
        # Provide download link
        with open(output_path, "rb") as f:
            st.download_button(
                label="📥 Download PDF",
                data=f,
                file_name=os.path.basename(output_path),
                mime="application/pdf"
            )
        
    except subprocess.CalledProcessError as e:
        st.error(f"❌ Error: {e}")

    # Cleanup
    os.remove(input_path)
