# import streamlit as st
# from paddleocr import PaddleOCR
# from PIL import Image
# import numpy as np
# import fitz  # PyMuPDF
# import io
# import streamlit.components.v1 as components

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
#         progress = st.progress(0)

#         num_pages = len(pdf_doc)

#         for i, page in enumerate(pdf_doc, start=1):
#             pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
#             img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

#             img_buffer = io.BytesIO()
#             img.save(img_buffer, format="PNG")
#             img_bytes = img_buffer.getvalue()
#             img_np = np.array(img)

#             ocr_local = PaddleOCR(use_angle_cls=True, lang=selected_lang)

#             with st.spinner(f"🔍 Processing page {i}/{num_pages}..."):
#                 result = ocr_local.ocr(img_np)

#             page_text = f"\n📄 ---- Page {i} ----\n"
#             for page_data in result:
#                 if isinstance(page_data, dict) and "rec_texts" in page_data:
#                     page_text += "\n".join(page_data["rec_texts"]) + "\n"
#                 elif isinstance(page_data, list):
#                     for line in page_data:
#                         if len(line) > 1:
#                             page_text += str(line[1][0]) + "\n"

#             all_text += page_text + "\n"

#             if show_images:
#                 st.image(img_bytes, caption=f"📃 Page {i}", use_container_width=True)

#             progress.progress(i / num_pages)

#         progress.empty()

#     # ---------- OUTPUT ----------
#     st.success(f"✅ Text extraction complete ({lang_choice})!")

#     st.text_area("📝 Extracted Text", all_text.strip(), height=400, key="extracted_text_box")

#     # --- Copy Button (JS) ---
#     copy_code = f"""
#         <script>
#         function copyToClipboard() {{
#             var text = `{all_text.strip().replace('`', '\\`')}`;
#             navigator.clipboard.writeText(text);
#             alert("✅ Text copied to clipboard!");
#         }}
#         </script>
#         <button onclick="copyToClipboard()" 
#             style="
#                 background-color:#4CAF50;
#                 color:white;
#                 border:none;
#                 padding:8px 16px;
#                 border-radius:6px;
#                 cursor:pointer;
#                 font-size:16px;">
#             📋 Copy Text
#         </button>
#     """
#     components.html(copy_code, height=70)

#     # --- Download Button ---
#     st.download_button(
#         label="💾 Download Extracted Text",
#         data=all_text.strip(),
#         file_name=f"extracted_text_{selected_lang}.txt",
#         mime="text/plain"
#     )

# else:
#     st.info("Please upload an image or PDF to start extraction.")

#____________________________________________________________________________________
import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import fitz  # PyMuPDF
import io
import streamlit.components.v1 as components

st.set_page_config(page_title="Textii 🧠 - Smart Text Extractor", page_icon="🧠", layout="centered")

st.title("🧠 Textii — Smart Text Extractor")
st.write("Extract text from images or PDFs in multiple languages using PaddleOCR.")

# Sidebar for language
st.sidebar.header("🌐 Language Settings")
lang_choice = st.sidebar.selectbox("Select OCR Language", ["English", "Hindi", "French", "Spanish"], index=0)
lang_map = {"English": "en", "Hindi": "hi", "French": "fr", "Spanish": "es"}
selected_lang = lang_map[lang_choice]

# Initialize OCR once per language
if "ocr" not in st.session_state or st.session_state.lang != selected_lang:
    with st.spinner(f"🔄 Loading {lang_choice} OCR model..."):
        st.session_state.ocr = PaddleOCR(use_angle_cls=True, lang=selected_lang)
        st.session_state.lang = selected_lang

ocr = st.session_state.ocr

uploaded_file = st.file_uploader("📂 Upload Image or PDF", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    all_text = ""

    # ---------- IMAGE ----------
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        st.image(uploaded_file, caption="🖼️ Uploaded Image", use_container_width=True)
        img_np = np.array(Image.open(uploaded_file).convert("RGB"))
        with st.spinner("🔍 Extracting text..."):
            result = ocr.ocr(img_np)
        for item in result:
            if isinstance(item, list):
                for line in item:
                    if len(line) > 1:
                        all_text += line[1][0] + "\n"

    # ---------- PDF ----------
    elif uploaded_file.type == "application/pdf":
        st.info("📄 Extracting text from PDF pages...")
        pdf_bytes = uploaded_file.read()
        pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        show_images = st.checkbox("👁️ Show Page Previews")
        progress = st.progress(0)
        num_pages = len(pdf_doc)

        for i, page in enumerate(pdf_doc, start=1):
            pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img_np = np.array(img)

            with st.spinner(f"🔍 Processing page {i}/{num_pages}..."):
                result = ocr.ocr(img_np)

            page_text = f"\n📄 ---- Page {i} ----\n"
            for line in result[0]:
                page_text += line[1][0] + "\n"

            all_text += page_text
            if show_images:
                st.image(np.array(img), caption=f"📃 Page {i}", use_container_width=True)
            progress.progress(i / num_pages)
        progress.empty()

    # ---------- OUTPUT ----------
    st.success(f"✅ Text extraction complete ({lang_choice})!")
    st.text_area("📝 Extracted Text", all_text.strip(), height=400, key="extracted_text_box")

    # Safe text for JS copy button
    safe_text = all_text.strip().replace("`", "\\`").replace("\\", "\\\\").replace("\n", "\\n")

    copy_code = f"""
        <script>
        function copyToClipboard() {{
            var text = `{safe_text}`;
            navigator.clipboard.writeText(text);
            alert("✅ Text copied to clipboard!");
        }}
        </script>
        <button onclick="copyToClipboard()" 
            style="
                background-color:#4CAF50;
                color:white;
                border:none;
                padding:8px 16px;
                border-radius:6px;
                cursor:pointer;
                font-size:16px;">
            📋 Copy Text
        </button>
    """
    components.html(copy_code, height=70)

    st.download_button(
        label="💾 Download Extracted Text",
        data=all_text.strip(),
        file_name=f"extracted_text_{selected_lang}.txt",
        mime="text/plain"
    )

else:
    st.info("Please upload an image or PDF to start extraction.")
