# 📲 Day 22: QR Code Generator & Terminal Display

A quick utility that formats URLs, text, and Wi-Fi credentials into standard QR payloads, renders ASCII representations in the terminal, and exports high-definition PNG images.

---

## 📌 Concepts Covered
- URI & formatted payload generation (e.g. Wi-Fi string standards `WIFI:T:WPA;S:...;P:...;;`).
- Graceful third-party library imports (`try-except ImportError`).
- ASCII terminal visual rendering and image writing.

---

## 🚀 How to Run

```bash
python 22_QR_Code_Generator.py
```
*(Optional for PNG output: `pip install qrcode pillow`)*
