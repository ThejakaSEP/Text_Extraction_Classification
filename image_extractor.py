from PIL import Image
from pytesseract import pytesseract

from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
# nltk.download('words')

import shutil

import pdfplumber
import pandas as pd
import numpy as np



class ImageExtractor:
    def __init__(self):

        # Image
        # Define path to tessaract.exe (To find the path-> in Terminal -> Type 'which Tesseract')
        self.path_to_tesseract = r'/opt/homebrew/bin/tesseract'

        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = self.path_to_tesseract

        # Set the Parent directory paths to move
        self.dest_folder_path = '/Users/thejakamahaulpatha/Desktop/Break'

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
        # en_stopwords = stopwords.words('english')
        # stopwords_removed = []
        # for word in tokenized_list:
        #     if word not in en_stopwords:
        #         stopwords_removed.append(word)

       # Remove Non- English
        words = set(nltk.corpus.words.words())
        english_only = []
        # for word in stopwords_removed:
        for word in tokenized_list:
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
        elif 'ielts' in preprocessed_text:
            return 'IELTS'
        elif 'letter of acceptance'  in preprocessed_text:
            return 'LOA'
        else:
            return 'No Class'
        # pass

    def extract_text_from_pdf(self,pdf_path) -> str:
        # page_number = []
        page_content = []

        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                # page_number.append(i + 1)
                page_content.append(page.extract_text())

        return ' '.join(page_content)

    def move_file(self,image_path, file_class):
        destination_folder = self.dest_folder_path + '/' + file_class
        shutil.copy(image_path,destination_folder)



# # Testing
# obj_1 = ImageExtractor()
#
# path_to_image = '/Users/thejakamahaulpatha/Desktop/Break/Passport.jpg'
#
# extracted_text = obj_1.extract_text_from_image(path_to_image)
# preprocessed_text = obj_1.preprocess_text(extracted_text)
# file_class = obj_1.classifier(preprocessed_text)
#
# print(f"File Class : {file_class}")
#
# # Copy the file to relevant folder
# obj_1.move_file(path_to_image,file_class)

