
---

## 🧠 **Textii — Smart Text Extractor (AI-Powered OCR)**

**[Live App → textii.streamlit.app](https://textii.streamlit.app/)**

### 🚀 Overview

**Textii** is an AI-powered OCR (Optical Character Recognition) tool built using **PaddleOCR** and **Streamlit**.
It allows users to extract text from **images** 🖼️ or **PDFs** 📄 — without needing Poppler or any complex setup.
Just upload a file, and Textii intelligently extracts all visible text in seconds.

---

### ✨ Features

✅ Extract text from **images (JPG, PNG)** and **PDFs**
✅ Built on **PaddleOCR** — fast, accurate, and multilingual
✅ Works completely in the browser (no Poppler dependency)
✅ Simple **Streamlit UI** for smooth user experience
✅ Supports multi-page PDF processing
✅ Download or copy extracted text easily

---

### 🧩 Tech Stack

| Component          | Description                            |
| ------------------ | -------------------------------------- |
| **Streamlit**      | Interactive web UI                     |
| **PaddleOCR**      | Core OCR engine                        |
| **PyMuPDF (fitz)** | Converts PDFs to images (Poppler-free) |
| **Pillow (PIL)**   | Image handling                         |
| **NumPy**          | Image array conversions                |

---

### ⚙️ Installation (Local Setup)

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/textii.git
   cd textii
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On macOS/Linux
   .venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   👉 [http://localhost:8501](http://localhost:8501)

---

### 📦 Requirements

`requirements.txt`

```txt
streamlit
paddleocr
paddlepaddle
pillow
PyMuPDF
numpy
```

---

### 💡 How It Works

1. Upload an **image or PDF**
2. PaddleOCR scans the document and detects text regions
3. Extracted text is displayed instantly in the text area
4. (Optional) Copy or download the output

---

### 🌐 Live Demo

Try it here:
👉 **[https://textii.streamlit.app/](https://textii.streamlit.app/)**

---

### 🧰 Example Use Cases

* Extract text from scanned documents or notes
* Digitize printed receipts or forms
* Grab text from screenshots or posters
* Convert old PDFs into editable text

---

### 🤝 Contributing

Pull requests and suggestions are welcome!
If you find a bug or want a feature, open an issue or PR 🙌

---

### 🧑‍💻 Author

**Sahil Kumar**
🔗 [LinkedIn](#) • [GitHub](#) • [Live App](https://textii.streamlit.app/)

---

### 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---
