from PIL import Image
from pytesseract import pytesseract
from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
# nltk.download('words')

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

    def preprocess_text(self,text):

        # Turning to lower case
        text = text.lower()

        # Removing Stop words
        tokenized_list = word_tokenize(text)

        # Stop word Removal
        en_stopwords = stopwords.words('english')
        stopwords_removed = []
        for word in tokenized_list:
            if word not in en_stopwords:
                stopwords_removed.append(word)

       # Remove Non- English
        words = set(nltk.corpus.words.words())
        english_only = []
        for word in stopwords_removed:
            if word in words:
                english_only.append(word)

        preprocessed_text = ' '.join(english_only)

        return preprocessed_text


    def classifier(self,text):

        # Preprocessing input text
        preprocessed_text = self.preprocess_text(text)

        # # Loading the pretrained model
        # model = tf.load('text_classifier')

        # # Predicting the class
        # document_class = model.predict(preprocessed_text)

        # return document_class

        # Note : Since we do not have the model trained yet, we will use simple logic for an example

        if 'passport' in preprocessed_text:
            return 'Passport'
        else:
            return 'No Class'
        # pass

        def move_file(image_path,file_path):
            pass



# Testing
obj_1 = ImageExtractor()

path_to_image = '/Users/thejakamahaulpatha/Desktop/Break/Passport.jpg'

extracted_text = obj_1.extract_text_from_image(path_to_image)
preprocessed_text = obj_1.preprocess_text(extracted_text)
file_class = obj_1.classifier(preprocessed_text)

print(f"File Class : {file_class}")

