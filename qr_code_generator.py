import qrcode
import os


def generate_qr_code():
    while True:
        url = str(input("Enter the URL to generate QR code: "))
        if not url.strip():
            print("URL cannot be empty. Please try again.")
            continue
        else:
            break
    while True:
        file_name = str(input("Enter the file name (without extension): "))
        if not file_name.strip():
            print("File name cannot be empty. Please try again.")
        else:
            break
    os.makedirs("qr_code_images", exist_ok=True)
    qrcode.make(url).save("qr_code_images/"+file_name + ".png")
    print(f"QR code generated and saved as {file_name}.png")


generate_qr_code()
