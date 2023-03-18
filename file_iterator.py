import os
from text_extractor import TextExtractor

class FileIterator:
    def __init__(self,folder_path):
        self.folder_path = folder_path

    def iterate_files(self):

        for filename in os.listdir(self.folder_path):
            f = os.path.join(self.folder_path, filename)

            obj_1 = TextExtractor()

            if f.lower().endswith((".png", ".gif",".jpg",".jpeg")):
                path_to_image = f
                extracted_text = obj_1.extract_text_from_image(path_to_image)
                preprocessed_text = obj_1.preprocess_text(extracted_text)
                file_class = obj_1.classifier(preprocessed_text)
                print(f"File Class : {file_class}")
                # Copy the file to relevant folder
                obj_1.move_file(path_to_image,self.folder_path,file_class)

            elif f.endswith('.pdf'):
                path_to_pdf = f
                extracted_text_pdf = obj_1.extract_text_from_pdf(path_to_pdf)
                preprocessed_text_pdf = obj_1.preprocess_text(extracted_text_pdf)
                file_class_pdf = obj_1.classifier(preprocessed_text_pdf)
                print(f"File Class : {file_class_pdf}")
                # Copy the file to relevant folder
                obj_1.move_file(path_to_pdf,self.folder_path,file_class_pdf)

# Testing
# folder_path_sample = '/Users/thejakamahaulpatha/Desktop/Break/Documents'
# obj2 = FileIterator(folder_path_sample)
# obj2.iterate_files()
