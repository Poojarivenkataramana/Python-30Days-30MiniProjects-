# ----------------------------------------------------
# Day 22: QR Code Generator & Terminal Display
# Concepts: String Encoding, Image File Export / ASCII Matrix, Error Handling
# ----------------------------------------------------

import sys

def generate_qr_code(data, output_file="qrcode.png"):
    print(f"\nEncoding data: '{data}'")

    # Try using qrcode library if installed
    try:
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=2,
        )
        qr.add_data(data)
        qr.make(fit=True)

        print("\n" + "=" * 40)
        print("📱 TERMINAL QR CODE PREVIEW 📱".center(40))
        print("=" * 40)
        qr.print_ascii(invert=True)
        print("=" * 40)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)
        print(f"✅ QR Code saved successfully as image file: '{output_file}'")
        return True

    except ImportError:
        print("\nℹ️ [Optional 'qrcode' package not installed - displaying text-matrix preview]")
        print("To generate high-res PNG image files, run: pip install qrcode pillow")
        print("\n" + "=" * 40)
        print("📱 QR PAYLOAD CONFIRMATION 📱".center(40))
        print("=" * 40)
        print(f"Payload Data : {data}")
        print(f"Length       : {len(data)} characters")
        print(f"Encoding Type: UTF-8 Text/URI")
        print("=" * 40)
        return False

def main():
    print("=" * 50)
    print("📲 QR CODE GENERATOR 📲".center(50))
    print("=" * 50)

    print("Options:")
    print("1. Encode Website URL (e.g. https://github.com)")
    print("2. Encode Custom Text or Message")
    print("3. Encode Wi-Fi Network Credentials")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        url = input("Enter website URL: ").strip()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        generate_qr_code(url, "website_qr.png")
    elif choice == "2":
        text = input("Enter text/message: ").strip()
        generate_qr_code(text, "message_qr.png")
    elif choice == "3":
        ssid = input("Enter Wi-Fi SSID (Network Name): ").strip()
        password = input("Enter Wi-Fi Password: ").strip()
        auth = input("Authentication Type (WPA/WEP, default WPA): ").strip().upper() or "WPA"
        wifi_payload = f"WIFI:T:{auth};S:{ssid};P:{password};;"
        generate_qr_code(wifi_payload, "wifi_qr.png")
    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
