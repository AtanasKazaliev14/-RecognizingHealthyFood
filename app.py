import streamlit as st
import easyocr 
import numpy as np
from PIL import Image

food_additives = {
    "preservatives": {  # E200–E299
        "E200": {"name": "Сорбинова киселина", "risk": "ниска", "info": "Консервант, може да предизвика дразнене"},
        "E210": {"name": "Бензоена киселина", "risk": "средна", "info": "Свързва се с алергични реакции"},
        "E220": {"name": "Серен диоксид", "risk": "висока", "info": "Може да предизвика астматични реакции"},
        "E250": {"name": "Натриев нитрит", "risk": "висока", "info": "Свързан с риск от рак"},
    },

    "colorants": {  # E100–E199
        "E100": {"name": "Куркумин", "risk": "ниска", "info": "Естествен оцветител"},
        "E120": {"name": "Кармин", "risk": "средна", "info": "Може да предизвика алергии"},
        "E133": {"name": "Синьо №1", "risk": "средна", "info": "Синтетичен оцветител"},
    },

    "antioxidants": {  # E300–E399
        "E300": {"name": "Аскорбинова киселина", "risk": "ниска", "info": "Витамин C"},
        "E320": {"name": "BHA", "risk": "висока", "info": "Възможен канцероген"},
        "E321": {"name": "BHT", "risk": "висока", "info": "Свързан с хормонални нарушения"},
    },

    "emulsifiers": {
        "E322": {"name": "Лецитин", "risk": "ниска", "info": "Подобрява текстурата"},
        "E471": {"name": "Моно- и диглицериди", "risk": "средна", "info": "Може да съдържа трансмазнини"},
    }
}
harmful_ingredients = {
    "палмово масло": {
        "risk": "средна",
        "info": "Повишава LDL холестерола"
    },
    "захар": {
        "risk": "висока",
        "info": "Свързана със затлъстяване и диабет"
    },
    "глюкозо-фруктозен сироп": {
        "risk": "висока",
        "info": "Нарушава метаболизма"
    },
    "аспартам": {
        "risk": "средна",
        "info": "Изкуствен подсладител"
    },
    "мононатриев глутамат": {
        "risk": "средна",
        "info": "E621 – подобрител на вкуса"
    }
}
allergens = [
    "мляко",
    "яйца",
    "глутен",
    "фъстъци",
    "ядки",
    "соя",
    "риба",
    "ракообразни"
]
safe_ingredients = {
    "вода",
    "сол",
    "зехтин",
    "мед",
    "плодове",
    "зеленчуци"
}
def find_e_number(e_code):
    for category in food_additives.values():
        if e_code in category:
            return category[e_code]
    return None
def is_harmful(ingredient):
    ingredient = ingredient.lower()
    return ingredient in harmful_ingredients
def is_allergen(ingredient):
    ingredient = ingredient.lower()
    return ingredient in allergens
