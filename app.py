import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import fitz  # PyMuPDF

st.set_page_config(page_title="Text Extractor (PaddleOCR)", page_icon="🧠", layout="centered")

# ✅ Initialize OCR only once (fixes PDX reinit issue)
if "ocr" not in st.session_state:
    st.session_state.ocr = PaddleOCR(use_angle_cls=True, lang='en')

ocr = st.session_state.ocr

st.title("🧠 Advanced Text Extractor (PaddleOCR)")
st.write("Upload an image or PDF to extract text.")

uploaded_file = st.file_uploader("📂 Upload Image or PDF", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    all_text = ""

    if uploaded_file.type in ["image/jpeg", "image/png"]:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        image = Image.open(uploaded_file).convert("RGB")
        img_np = np.array(image)

        result = ocr.ocr(img_np)
        for item in result:
            if isinstance(item, dict) and "rec_texts" in item:
                all_text += "\n".join(item["rec_texts"]) + "\n"
            elif isinstance(item, list):
                for line in item:
                    if len(line) > 1:
                        all_text += str(line[1][0]) + "\n"

    elif uploaded_file.type == "application/pdf":
        st.info("📄 Extracting text from PDF pages...")
        pdf_bytes = uploaded_file.read()
        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        for i, page in enumerate(pdf_doc):
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img_np = np.array(img)
            result = ocr.ocr(img_np)
            for page_data in result:
                if isinstance(page_data, dict) and "rec_texts" in page_data:
                    all_text += "\n".join(page_data["rec_texts"]) + "\n"
                elif isinstance(page_data, list):
                    for line in page_data:
                        if len(line) > 1:
                            all_text += str(line[1][0]) + "\n"

    st.success("✅ Text extraction complete!")
    st.text_area("📝 Extracted Text", all_text, height=400)
else:
    st.info("Please upload an image or PDF to start extraction.")

