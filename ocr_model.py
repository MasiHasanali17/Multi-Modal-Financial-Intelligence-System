import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def extract_bill_text(image_bytes):
    result = reader.readtext(image_bytes, detail=0)
    text = " ".join(result)

    amount = None
    for word in text.split():
        if word.replace('.', '').isdigit():
            amount = word

    return {
        "raw_text": text,
        "amount_detected": amount
    }
