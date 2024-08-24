import json


#Получение информации от пользователя
name = input ("Как Вас зовут? ")
age = input ("Сколько Вам лет? ")
hobbies = input ("Перечислите Ваши хобби через пробел: ").split(" ")
industry = input ("В какой области Вы работаете? ")
position = input ("Какая Ваша должность? ")
experience = int(input ("Ваш стаж работы в годах: "))

#Структура json
user_data = {
    "personal_info": {
        "name": name,
        "age": age,
    },
    "professional_info": {
        "position": position,
        "industry_details": {
            "industry": industry,
            "expirience": {
                "years": experience,
                "description": f"Стаж работы {experience} лет(года)"
                }
            }
        },
    "hobbies_list": {
        "hobbies": hobbies,
        "hobbies_count": len(hobbies)
    }
}

#Сохранение в json
with open("user_data.json", "w", encoding='utf-8') as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)

print("Данные успешно сохранены в файл user_data.json")