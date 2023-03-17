from PIL import Image
from pytesseract import pytesseract


class ImageExtractor:
    def __init__(self):

        # Define path to tessaract.exe (To find the path-> in Terminal -> Type 'which Tesseract')
        self.path_to_tesseract = r'/opt/homebrew/bin/tesseract'

        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = self.path_to_tesseract

    def extract_text_from_image(self,image_path) -> str:

        # Open image with PIL
        img = Image.open(image_path)

        # Extract text from image
        text = pytesseract.image_to_string(img)

        return text


    def classifier(self,text):

        # # Preprocessing input text
        # preprocessed_text = preprocess_text(text)

        # # Loading the pretrained model
        # model = tf.load('text_classifier')

        # # Predicting the class
        # document_class = model.predict(preprocessed_text)

        # return document_class

# Testing
obj_1 = ImageExtractor()
path_to_image = 'Passport.jpg'
print(obj_1.extract_text_from_image(path_to_image))