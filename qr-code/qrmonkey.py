import qrcode
from PIL import Image, ImageDraw


def create_custom_qr_code(data, size=300, body_color="#000000", bg_color="#FFFFFF", logo_path=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=body_color, back_color=bg_color).convert('RGB')

    img = img.resize((size, size), Image.Resampling.LANCZOS)

    if logo_path:
        logo = Image.open(logo_path)

        logo_width = int(size / 4)
        logo_height = int(logo.size[1] * (logo_width / logo.size[0]))
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

        pos = ((img.size[0] - logo_width) // 2, (img.size[1] - logo_height) // 2)

        img.paste(logo, pos, mask=logo)

    filename = "custom_qr_code.png"
    img.save(filename)

    print(f"QR-Code erfolgreich erstellt und in '{filename}' gespeichert.")


# Example Code
'''create_custom_qr_code(
    data="https://github.com/JonasHeilig",
    size=400,
    body_color="#000000",
    bg_color="#ffffff",
    logo_path="github.png"
)'''
