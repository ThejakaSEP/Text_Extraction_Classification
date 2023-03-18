# Since above two scenarios are working fine, now we will try to access a folder and iterate through files

# import required module
import os
from image_extractor import ImageExtractor


folder_path = '/Users/thejakamahaulpatha/Desktop/Break/Documents'

# iterate over files in
# that directory
for filename in os.listdir(folder_path):
    f = os.path.join(folder_path, filename)

    obj_1 = ImageExtractor()

    if f.endswith('.jpg'):
        path_to_image = f
        extracted_text = obj_1.extract_text_from_image(path_to_image)
        preprocessed_text = obj_1.preprocess_text(extracted_text)
        file_class = obj_1.classifier(preprocessed_text)
        print(f"File Class : {file_class}")
        # Copy the file to relevant folder
        obj_1.move_file(path_to_image,folder_path,file_class)

    elif f.endswith('.pdf'):
        path_to_pdf = f
        extracted_text_pdf = obj_1.extract_text_from_pdf(path_to_pdf)
        preprocessed_text_pdf = obj_1.preprocess_text(extracted_text_pdf)
        file_class_pdf = obj_1.classifier(preprocessed_text_pdf)
        print(f"File Class : {file_class_pdf}")
        # Copy the file to relevant folder
        obj_1.move_file(path_to_pdf,folder_path,file_class_pdf)

