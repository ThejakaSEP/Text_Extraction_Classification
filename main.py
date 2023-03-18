from image_extractor import ImageExtractor


obj_1 = ImageExtractor()

path_to_image = '/Users/thejakamahaulpatha/Desktop/Break/Passport.jpg'

extracted_text = obj_1.extract_text_from_image(path_to_image)
preprocessed_text = obj_1.preprocess_text(extracted_text)
file_class = obj_1.classifier(preprocessed_text)

print(f"File Class : {file_class}")

# Copy the file to relevant folder
obj_1.move_file(path_to_image,file_class)


path_to_pdf = '/Users/thejakamahaulpatha/Desktop/Break/Letter of Acceptance.pdf'
extracted_text_pdf = obj_1.extract_text_from_pdf(path_to_pdf)
preprocessed_text_pdf = obj_1.preprocess_text(extracted_text_pdf)
file_class_pdf = obj_1.classifier(preprocessed_text_pdf)

print(f"File Class : {file_class_pdf}")

# Copy the file to relevant folder
obj_1.move_file(path_to_pdf,file_class_pdf)