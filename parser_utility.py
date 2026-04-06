import io
import os
import re
import nltk
import spacy
from pdfminer.high_level import extract_text
from spacy.matcher import Matcher

class ResumeParser:
    def __init__(self, resume_path):
        # Load the small English model
        try:
            self.__nlp = spacy.load('en_core_web_sm')
        except OSError:
            # Fallback if model isn't linked correctly
            import en_core_web_sm
            self.__nlp = en_core_web_sm.load()
            
        self.__matcher = Matcher(self.__nlp.vocab)
        self.__resume_path = resume_path
        self.__text = self.__extract_content(self.__resume_path)
        self.__details = self.__do_parse()

    def get_extracted_data(self):
        return self.__details

    def __extract_content(self, path):
        if path.endswith('.pdf'):
            try:
                return extract_text(path)
            except Exception as e:
                print(f"Error extracting PDF: {e}")
                return ""
        return ""



    def __do_parse(self):
        text = self.__text
        
        # 1. EMAIL & MOBILE
        email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
        email = email_match.group(0) if email_match else "Not Found"
        phone_match = re.search(r"\b\d{10}\b", text)
        phone = phone_match.group(0) if phone_match else "Not Found"
        
        # 2. NAME (First 2 words)
        words = text.strip().split()
        name = " ".join(words[:2]) if len(words) >= 2 else "Not Found"

        # 3. COMPREHENSIVE SKILLS LIST (Added all your resume keywords)
        skills_list = [
            'Python', 'C++', 'SQL', 'TensorFlow', 'PyTorch', 'Scikit-learn', 
            'Pandas', 'NumPy', 'Seaborn', 'Matplotlib', 'BeautifulSoup', 
            'Selenium', 'Machine Learning', 'Deep Learning', 'CNN', 'RNN', 
            'LSTM', 'GRU', 'Transformers', 'GANs', 'NLP', 'OpenCV', 'Git', 
            'XGBoost', 'LightGBM', 'PCA', 'SHAP', 'Flask', 'Streamlit', 'YOLO'
        ]
        
        # Case-insensitive search
        found_skills = []
        for skill in skills_list:
            # Matches the skill even if it has a dot or dash (like Scikit-learn)
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found_skills.append(skill)

        return {
            "name": name,
            "email": email,
            "mobile_number": phone,
            "skills": list(set(found_skills)), # Removes duplicates
            "no_of_pages": 1 
        }