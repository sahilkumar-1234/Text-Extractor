import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import fitz  # PyMuPDF

# Initialize PaddleOCR once (English)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

st.set_page_config(page_title="Text Extractor (PaddleOCR)", page_icon="🧠", layout="centered")

st.title("🧠 Advanced Text Extractor (PaddleOCR)")
st.write("Upload an image or PDF to extract text using PaddleOCR (no Poppler needed).")

uploaded_file = st.file_uploader("📂 Upload Image or PDF", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    all_text = ""

    # ---------- IMAGE HANDLING ----------
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        image = Image.open(uploaded_file).convert("RGB")
    
        img_np = np.array(image)

        result = ocr.ocr(img_np)
        
        
        # st.text_area("📝 Extracted Text", result, height=400)

        for page_num, page in enumerate(result, start=1):
            page_block = f"\n📄 ---- Page {page_num} ----\n"

            if isinstance(page, dict) and "rec_texts" in page:
                for i, text in enumerate(page["rec_texts"], start=1):
                    page_block += f"{text}\n"
            else:
                page_block += "⚠️ No recognized text on this page.\n"

            all_text += page_block
            
        st.text_area("📝 Extracted Text", all_text, height=400)           
        st.write("✅Text Extracted Sucessfully...")
        
        st.download_button(
            label="💾 Download Extracted Text",
            data=all_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )


    elif uploaded_file.type == "application/pdf":
        st.info("📄 Extracting text from PDF pages...")

        # Read uploaded PDF into bytes
        pdf_bytes = uploaded_file.read()
        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")


        for i, page in enumerate(pdf_doc):
            # Render PDF page to image (300 DPI)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img_np = np.array(img)

            # OCR on this page
            result = ocr.ocr(img_np)

            
            for page_num, page in enumerate(result, start=1):
                page_block = f"\n📄 ---- Page {page_num} ----\n"

                if isinstance(page, dict) and "rec_texts" in page:
                    for i, text in enumerate(page["rec_texts"], start=1):
                        page_block += f"{text}\n"

                elif isinstance(page, list) and len(page) > 0:
                    for i, line in enumerate(page, start=1):
                        if len(line) > 1 and isinstance(line[1], (list, tuple)):
                            text = line[1][0]
                            page_block += f"{text}\n"

                else:
                    page_block += "⚠️ No recognized text on this page.\n"

                all_text += page_block
            

        st.success("✅ Text extraction complete!")
        st.text_area("📝 Extracted Text", all_text, height=400)
        
            # Download extracted text
            
        st.download_button(
            label="💾 Download Extracted Text",
            data=all_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )

else:
    st.info("Please upload an image or PDF to start extraction.")
