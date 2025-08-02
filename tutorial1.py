import cv2
import pytesseract 

def extract_text_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract text
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray_image, config=custom_config)
    print("Extracted Text:",text)
    return text

def parse_mrz(mrz_text):
        line1 = mrz_text[0]
        line2 = mrz_text[1]
        print("Line1:",line1)
        print("Line2:",line2)

        #line1
        Document_type = line1[0]
        Country_code = line1[2:5]
        Name = line1[5:].split('<<')
        print("Name",Name)
        Surname = Name[0].replace('<', ' ').strip()
        given_names = Name[1].replace('<', ' ').strip() 

        #line2
        Passport_number = line2[0:9].replace('<', ' ').strip()
        Nationality = line2[9:12]
        Birth_date = line2[13:19]
        Gender = line2[20]
        Expiry_date = line2[21:27]

        return {
        "Document Type": Document_type,
        "Country Code": Country_code,
        "Surname": Surname,
        "Names": given_names,
        "Passport Number": Passport_number,
        "Nationality": Nationality,
        "Date of Birth": Birth_date,
        "Gender": Gender,
        "Date of Expiry": Expiry_date
    }


if __name__ == "__main__":
    image_path = "pass image.jpg"  # Replace your image path
    text = extract_text_from_image(image_path)
    print("Extracted Text:\n", text)

        # Split into lines and parse MRZ
    lines = text.strip().split('\n')
    lines = [line.strip() for line in lines if line.strip() != '']

    if len(lines) >= 2:
        mrz_lines = lines[-2:]  # Take last two lines (MRZ lines)
        information = parse_mrz(mrz_lines)
        print("\nParsed MRZ Information:",information)
        for key, value in information.items():
            print(f"{key}: {value}")
    else:
        print("Could not find two MRZ lines in extracted text.")


   


    