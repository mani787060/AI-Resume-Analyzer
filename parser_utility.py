import io
import os
import re
import spacy
from pdfminer.high_level import extract_text, extract_pages
from spacy.matcher import Matcher

class ResumeParser:
    def __init__(self, resume_path):
        # 1. Robust Model Loading for Streamlit Cloud
        try:
            self.__nlp = spacy.load('en_core_web_sm')
        except:
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

    def __get_page_count(self, path):
        try:
            return len(list(extract_pages(path)))
        except:
            return 1

    def __do_parse(self):
        text = self.__text
        doc = self.__nlp(text)
        
        # 1. EMAIL & MOBILE (Improved RegEx)
        email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
        email = email_match.group(0) if email_match else "Not Found"
        
        # Matches various phone formats (e.g., +91 9876543210 or 9876543210)
        phone_match = re.search(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{10})", text)
        phone = phone_match.group(0) if phone_match else "Not Found"
        
        # 2. NAME EXTRACTION (Using spaCy Entity Recognition)
        name = "Not Found"
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                name = ent.text
                break
        
        # Fallback if spaCy fails: first two non-empty lines
        if name == "Not Found":
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            if lines:
                name = lines[0]

        # 3. COMPREHENSIVE SKILLS LIST (Synced with your app.py keywords)
        skills_list = [
            'Python', 'C++', 'SQL', 'TensorFlow', 'PyTorch', 'Scikit-learn', 
            'Pandas', 'NumPy', 'Seaborn', 'Matplotlib', 'BeautifulSoup', 
            'Selenium', 'Machine Learning', 'Deep Learning', 'CNN', 'RNN', 
            'LSTM', 'GRU', 'Transformers', 'GANs', 'NLP', 'OpenCV', 'Git', 
            'Flask', 'Streamlit', 'YOLO', 'React', 'Django', 'Node JS', 
            'React JS', 'PHP', 'Laravel', 'Magento', 'WordPress', 'JavaScript', 
            'Angular JS', 'Flutter', 'Kotlin', 'XML', 'Kivy', 'IOS', 'Swift', 
            'Figma', 'UX', 'UI', 'Adobe XD', 'Photoshop', 'Illustrator'
        ]
        
        found_skills = []
        for skill in skills_list:
            # Case-insensitive whole word matching
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found_skills.append(skill)

        # 4. ACTUAL PAGE COUNT
        page_count = self.__get_page_count(self.__resume_path)

        return {
            "name": name,
            "email": email,
            "mobile_number": phone,
            "skills": list(set(found_skills)),
            "no_of_pages": page_count
        }
