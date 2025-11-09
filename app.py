# import streamlit as st
# from paddleocr import PaddleOCR
# from PIL import Image
# import numpy as np
# import fitz  # PyMuPDF

# st.set_page_config(page_title="Text Extractor (PaddleOCR)", page_icon="🧠", layout="centered")

# # ✅ Initialize OCR only once (fixes PDX reinit issue)
# if "ocr" not in st.session_state:
#     st.session_state.ocr = PaddleOCR(use_angle_cls=True, lang='en')

# ocr = st.session_state.ocr

# st.title("🧠 Advanced Text Extractor (PaddleOCR)")
# st.write("Upload an image or PDF to extract text.")

# uploaded_file = st.file_uploader("📂 Upload Image or PDF", type=["jpg", "jpeg", "png", "pdf"])

# if uploaded_file:
#     all_text = ""

#     if uploaded_file.type in ["image/jpeg", "image/png"]:
#         st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
#         image = Image.open(uploaded_file).convert("RGB")
#         img_np = np.array(image)

#         result = ocr.ocr(img_np)
#         for item in result:
#             if isinstance(item, dict) and "rec_texts" in item:
#                 all_text += "\n".join(item["rec_texts"]) + "\n"
#             elif isinstance(item, list):
#                 for line in item:
#                     if len(line) > 1:
#                         all_text += str(line[1][0]) + "\n"

#     elif uploaded_file.type == "application/pdf":
#         st.info("📄 Extracting text from PDF pages...")
#         pdf_bytes = uploaded_file.read()
#         pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")

#         for i, page in enumerate(pdf_doc):
#             pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
#             img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#             img_np = np.array(img)
#             result = ocr.ocr(img_np)
#             for page_data in result:
#                 if isinstance(page_data, dict) and "rec_texts" in page_data:
#                     all_text += "\n".join(page_data["rec_texts"]) + "\n"
#                 elif isinstance(page_data, list):
#                     for line in page_data:
#                         if len(line) > 1:
#                             all_text += str(line[1][0]) + "\n"

#     st.success("✅ Text extraction complete!")
#     st.text_area("📝 Extracted Text", all_text, height=400)
# else:
#     st.info("Please upload an image or PDF to start extraction.")


#_____________________________________________________________________________________________________________________


# import streamlit as st
# from paddleocr import PaddleOCR
# from PIL import Image
# import numpy as np
# import fitz  # PyMuPDF

# st.set_page_config(
#     page_title="Text Extractor (PaddleOCR)",
#     page_icon="🧠",
#     layout="centered"
# )

# st.title("🧠 Advanced Text Extractor (PaddleOCR)")
# st.write("Upload an image or PDF and extract text in your preferred language.")

# # ---------------- Language Selection ----------------
# st.sidebar.header("🌐 Language Settings")
# lang_choice = st.sidebar.selectbox(
#     "Select OCR Language",
#     options=["English", "Hindi", "French", "Spanish"],
#     index=0
# )

# # Map human-readable names to PaddleOCR language codes
# lang_map = {
#     "English": "en",
#     "Hindi": "hi",
#     "French": "fr",
#     "Spanish": "es"
# }

# selected_lang = lang_map[lang_choice]

# # ✅ Initialize OCR only once per selected language
# if "ocr" not in st.session_state or st.session_state.lang != selected_lang:
#     with st.spinner(f"🔄 Loading {lang_choice} OCR model..."):
#         st.session_state.ocr = PaddleOCR(use_angle_cls=True, lang=selected_lang)
#         st.session_state.lang = selected_lang

# ocr = st.session_state.ocr

# # ---------------- File Upload Section ----------------
# uploaded_file = st.file_uploader(
#     "📂 Upload Image or PDF",
#     type=["jpg", "jpeg", "png", "pdf"]
# )

# if uploaded_file:
#     all_text = ""

#     # ---------- IMAGE HANDLING ----------
#     if uploaded_file.type in ["image/jpeg", "image/png"]:
#         st.image(uploaded_file, caption="🖼️ Uploaded Image", use_container_width=True)

#         image = Image.open(uploaded_file).convert("RGB")
#         img_np = np.array(image)

#         result = ocr.ocr(img_np)

#         for item in result:
#             if isinstance(item, dict) and "rec_texts" in item:
#                 all_text += "\n".join(item["rec_texts"]) + "\n"
#             elif isinstance(item, list):
#                 for line in item:
#                     if len(line) > 1:
#                         all_text += str(line[1][0]) + "\n"

#     # ---------- PDF HANDLING ----------
#     elif uploaded_file.type == "application/pdf":
#         st.info("📄 Extracting text from PDF pages...")

#         pdf_bytes = uploaded_file.read()
#         pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")

#         for i, page in enumerate(pdf_doc):
#             pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
#             img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#             img_np = np.array(img)
#             result = ocr.ocr(img_np)
#             for page_data in result:
#                 if isinstance(page_data, dict) and "rec_texts" in page_data:
#                     all_text += "\n".join(page_data["rec_texts"]) + "\n"
#                 elif isinstance(page_data, list):
#                     for line in page_data:
#                         if len(line) > 1:
#                             all_text += str(line[1][0]) + "\n"

            
#             st.title("Checkbox Controlled Visibility")
#             show_details = st.checkbox("Show Details")
#             if show_details:
#                 st.write("Here are some details.")
#                 st.button("Action Button")
#                 st.image(img, caption=f"📃 Page {i+1}", use_container_width=True)

#     # ---------- OUTPUT ----------
#     st.success(f"✅ Text extraction complete ({lang_choice})!")
#     st.text_area("📝 Extracted Text", all_text.strip(), height=400)

#     # Optional: download extracted text
#     st.download_button(
#         label="💾 Download Extracted Text",
#         data=all_text.strip(),
#         file_name=f"extracted_text_{selected_lang}.txt",
#         mime="text/plain"
#     )

# else:
#     st.info("Please upload an image or PDF to start extraction.")

#________________________________________________________________________________________________________________

# import streamlit as st
# from paddleocr import PaddleOCR
# from PIL import Image
# import numpy as np
# import fitz  # PyMuPDF

# # ---------------- Streamlit Page Setup ----------------
# st.set_page_config(
#     page_title="Textii 🧠 - Smart Text Extractor",
#     page_icon="🧠",
#     layout="centered"
# )

# st.title("🧠 Textii — Smart Text Extractor")
# st.write("Extract text from images or PDFs in multiple languages using PaddleOCR.")

# # ---------------- Language Selection ----------------
# st.sidebar.header("🌐 Language Settings")
# lang_choice = st.sidebar.selectbox(
#     "Select OCR Language",
#     options=["English", "Hindi", "French", "Spanish"],
#     index=0
# )

# # Map language names to PaddleOCR codes
# lang_map = {
#     "English": "en",
#     "Hindi": "hi",
#     "French": "fr",
#     "Spanish": "es"
# }
# selected_lang = lang_map[lang_choice]

# # ✅ Initialize OCR only once per selected language
# if "ocr" not in st.session_state or st.session_state.lang != selected_lang:
#     with st.spinner(f"🔄 Loading {lang_choice} OCR model..."):
#         st.session_state.ocr = PaddleOCR(use_angle_cls=True, lang=selected_lang)
#         st.session_state.lang = selected_lang

# ocr = st.session_state.ocr

# # ---------------- File Upload ----------------
# uploaded_file = st.file_uploader(
#     "📂 Upload Image or PDF",
#     type=["jpg", "jpeg", "png", "pdf"]
# )

# # ---------------- Extraction Logic ----------------
# if uploaded_file:
#     all_text = ""

#     # ---------- IMAGE HANDLING ----------
#     if uploaded_file.type in ["image/jpeg", "image/png"]:
#         st.image(uploaded_file, caption="🖼️ Uploaded Image", use_container_width=True)
#         image = Image.open(uploaded_file).convert("RGB")
#         img_np = np.array(image)

#         with st.spinner("🔍 Extracting text..."):
#             result = ocr.ocr(img_np)

#         for item in result:
#             if isinstance(item, dict) and "rec_texts" in item:
#                 all_text += "\n".join(item["rec_texts"]) + "\n"
#             elif isinstance(item, list):
#                 for line in item:
#                     if len(line) > 1:
#                         all_text += str(line[1][0]) + "\n"

#     # ---------- PDF HANDLING ----------
#     elif uploaded_file.type == "application/pdf":
#         st.info("📄 Extracting text from PDF pages...")
#         pdf_bytes = uploaded_file.read()
#         pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")

#         show_images = st.checkbox("👁️ Show Page Previews")

#         for i, page in enumerate(pdf_doc):
#             pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
#             img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
#             img_np = np.array(img)

#             with st.spinner(f"🔍 Processing page {i+1}/{len(pdf_doc)}..."):
#                 result = ocr.ocr(img_np)

#         # 🧾 Add page header before extracted text
#             page_text = f"\n📄 ---- Page {i} ----\n"

#            for page_data in result:
                       
#             if isinstance(page_data, dict) and "rec_texts" in page_data:
#                 page_text += "\n".join(page_data["rec_texts"]) + "\n"
#             elif isinstance(page_data, list):
#                 for line in page_data:
#                     if len(line) > 1:
#                         page_text += str(line[1][0]) + "\n"
#     # Append current page’s text to all_text
#         all_text += page_text + "\n"

#             # Optional: show image preview
#             if show_images:
#                 st.image(img, caption=f"📃 Page {i+1}", use_container_width=True)

#     # ---------- OUTPUT ----------
#     st.success(f"✅ Text extraction complete ({lang_choice})!")
#     st.text_area("📝 Extracted Text", all_text.strip(), height=400)

#     st.download_button(
#         label="💾 Download Extracted Text",
#         data=all_text.strip(),
#         file_name=f"extracted_text_{selected_lang}.txt",
#         mime="text/plain"
#     )

# else:
#     st.info("Please upload an image or PDF to start extraction.")


#_________________________________________________________________________________________
import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import fitz  # PyMuPDF
import io

# ---------------- Streamlit Page Setup ----------------
st.set_page_config(
    page_title="Textii 🧠 - Smart Text Extractor",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Textii — Smart Text Extractor")
st.write("Extract text from images or PDFs in multiple languages using PaddleOCR.")

# ---------------- Language Selection ----------------
st.sidebar.header("🌐 Language Settings")
lang_choice = st.sidebar.selectbox(
    "Select OCR Language",
    options=["English", "Hindi", "French", "Spanish"],
    index=0
)

# Map language names to PaddleOCR codes
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es"
}
selected_lang = lang_map[lang_choice]

# ✅ Initialize OCR only once per selected language
if "ocr" not in st.session_state or st.session_state.lang != selected_lang:
    with st.spinner(f"🔄 Loading {lang_choice} OCR model..."):
        st.session_state.ocr = PaddleOCR(use_angle_cls=True, lang=selected_lang)
        st.session_state.lang = selected_lang

ocr = st.session_state.ocr

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader(
    "📂 Upload Image or PDF",
    type=["jpg", "jpeg", "png", "pdf"]
)

# ---------------- Extraction Logic ----------------
if uploaded_file:
    all_text = ""

    # ---------- IMAGE HANDLING ----------
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        st.image(uploaded_file, caption="🖼️ Uploaded Image", use_container_width=True)
        image = Image.open(uploaded_file).convert("RGB")
        img_np = np.array(image)

        with st.spinner("🔍 Extracting text..."):
            result = ocr.ocr(img_np)

        for item in result:
            if isinstance(item, dict) and "rec_texts" in item:
                all_text += "\n".join(item["rec_texts"]) + "\n"
            elif isinstance(item, list):
                for line in item:
                    if len(line) > 1:
                        all_text += str(line[1][0]) + "\n"

    # ---------- PDF HANDLING ----------
    elif uploaded_file.type == "application/pdf":
        st.info("📄 Extracting text from PDF pages...")
        pdf_bytes = uploaded_file.read()
        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        show_images = st.checkbox("👁️ Show Page Previews")
        progress = st.progress(0)

        num_pages = len(pdf_doc)

        for i, page in enumerate(pdf_doc, start=1):
            # Convert page to image
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Convert image to bytes (safe for Streamlit rendering)
            img_buffer = io.BytesIO()
            img.save(img_buffer, format="PNG")
            img_bytes = img_buffer.getvalue()

            img_np = np.array(img)

            # ✅ Reinitialize OCR per page (prevents runtime crash)
            ocr_local = PaddleOCR(use_angle_cls=True, lang=selected_lang)

            with st.spinner(f"🔍 Processing page {i}/{num_pages}..."):
                result = ocr_local.ocr(img_np)

            page_text = f"\n📄 ---- Page {i} ----\n"
            for page_data in result:
                if isinstance(page_data, dict) and "rec_texts" in page_data:
                    page_text += "\n".join(page_data["rec_texts"]) + "\n"
                elif isinstance(page_data, list):
                    for line in page_data:
                        if len(line) > 1:
                            page_text += str(line[1][0]) + "\n"

            all_text += page_text + "\n"

            if show_images:
                st.image(img_bytes, caption=f"📃 Page {i}", use_container_width=True)

            progress.progress(i / num_pages)

        progress.empty()

    # ---------- OUTPUT ----------
    st.success(f"✅ Text extraction complete ({lang_choice})!")
    st.text_area("📝 Extracted Text", all_text.strip(), height=400)

    st.download_button(
        label="💾 Download Extracted Text",
        data=all_text.strip(),
        file_name=f"extracted_text_{selected_lang}.txt",
        mime="text/plain"
    )

else:
    st.info("Please upload an image or PDF to start extraction.")
