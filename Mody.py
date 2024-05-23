import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import random

# قائمة الردود المحتملة لكلمات محددة
responses = {
    "السلام": ["عليكم السلام", "مرحبا", "أهلاً"],
    "كيف": ["بخير، شكراً لسؤالك", "أنا في حالة جيدة", "أفضل من أي وقت مضى"],
    "الوقت": ["الوقت الآن هو ١٢:٠٠ مساءً", "لا أعرف الوقت بالضبط", "الوقت متأخر جدًا"]
}

def talk_to_virtual_character():
    while True:
        # النص الذي ترغب في تحويله إلى كلام
        text_to_analyze = input("أدخل النص الذي تريد التحدث حوله: ")

        # تقسيم النص إلى كلمات
        words = word_tokenize(text_to_analyze)

        # إيجاد الرد المناسب لكل كلمة
        response_text = ""
        for word in words:
            if word in responses:
                response_text += random.choice(responses[word]) + " "
            else:
                response_text += "لا أعرف كيف أجيب على ذلك. "

        # عرض الرد
        print("الرد:")
        print(response_text)

if __name__ == "__main__":
    talk_to_virtual_character()
