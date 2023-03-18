from image_extractor import ImageExtractor


obj_1 = ImageExtractor()

path_to_image = '/Users/thejakamahaulpatha/Desktop/Break/Passport.jpg'

extracted_text = obj_1.extract_text_from_image(path_to_image)
preprocessed_text = obj_1.preprocess_text(extracted_text)
file_class = obj_1.classifier(preprocessed_text)

print(f"File Class : {file_class}")

# Copy the file to relevant folder
obj_1.move_file(path_to_image,file_class)

