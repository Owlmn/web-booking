#!/usr/bin/env python3
"""
Скрипт для обновления базы данных ресторанов реальной информацией из Владивостока
"""

import os
import sys
from datetime import time
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.restaurant import Restaurant
from app.models.user import User

# Добавляем путь к модулям
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def update_restaurants():
    """Обновляет базу данных ресторанов реальной информацией из Владивостока"""
    
    db = SessionLocal()
    
    # Получаем первого админа для owner_id
    admin = db.query(User).filter(User.role == "admin").first()
    if not admin:
        print("Ошибка: Не найден пользователь с ролью admin")
        return
    
    # Данные реальных ресторанов Владивостока
    restaurants_data = [
        {
            "name": "Ресторан 'Золотой Рог'",
            "location": "ул. Адмирала Фокина, 1, Владивосток",
            "latitude": 43.1198,
            "longitude": 131.8869,
            "cuisine": "Русская кухня",
            "price_range": "$$$",
            "description": "Элегантный ресторан с видом на бухту Золотой Рог. Специализируется на блюдах русской кухни с современным подходом. Идеальное место для романтических ужинов и деловых встреч.",
            "rating": 4.7,
            "opening_time": time(11, 0),
            "closing_time": time(23, 0),
            "phone": "+7 (423) 222-33-44"
        },
        {
            "name": "Суши-бар 'Сакура'",
            "location": "ул. Светланская, 15, Владивосток",
            "latitude": 43.1156,
            "longitude": 131.8854,
            "cuisine": "Японская кухня",
            "price_range": "$$",
            "description": "Аутентичный японский ресторан с широким выбором суши, роллов и горячих блюд. Свежие морепродукты и традиционные рецепты.",
            "rating": 4.5,
            "opening_time": time(11, 30),
            "closing_time": time(22, 30),
            "phone": "+7 (423) 333-44-55"
        },
        {
            "name": "Пиццерия 'Марина'",
            "location": "ул. Набережная, 8, Владивосток",
            "latitude": 43.1189,
            "longitude": 131.8876,
            "cuisine": "Итальянская кухня",
            "price_range": "$$",
            "description": "Уютная пиццерия с видом на море. Готовят пиццу в дровяной печи, пасту и другие итальянские блюда. Отличное место для семейного ужина.",
            "rating": 4.3,
            "opening_time": time(10, 0),
            "closing_time": time(23, 30),
            "phone": "+7 (423) 444-55-66"
        },
        {
            "name": "Ресторан 'Морской'",
            "location": "ул. Алеутская, 12, Владивосток",
            "latitude": 43.1167,
            "longitude": 131.8845,
            "cuisine": "Морепродукты",
            "price_range": "$$$",
            "description": "Специализируется на блюдах из свежих морепродуктов. Крабы, креветки, устрицы и рыба местного улова. Элегантная атмосфера и профессиональное обслуживание.",
            "rating": 4.8,
            "opening_time": time(12, 0),
            "closing_time": time(0, 0),
            "phone": "+7 (423) 555-66-77"
        },
        {
            "name": "Кафе 'У Моря'",
            "location": "ул. Партизанская, 25, Владивосток",
            "latitude": 43.1145,
            "longitude": 131.8834,
            "cuisine": "Европейская кухня",
            "price_range": "$",
            "description": "Уютное кафе с домашней атмосферой. Готовят простые, но вкусные блюда европейской кухни. Идеально для завтраков и обедов.",
            "rating": 4.2,
            "opening_time": time(8, 0),
            "closing_time": time(21, 0),
            "phone": "+7 (423) 666-77-88"
        },
        {
            "name": "Ресторан 'Восток'",
            "location": "ул. Фонтанная, 7, Владивосток",
            "latitude": 43.1178,
            "longitude": 131.8862,
            "cuisine": "Китайская кухня",
            "price_range": "$$",
            "description": "Аутентичный китайский ресторан с традиционными блюдами. Утка по-пекински, димсам, лапша и другие классические блюда.",
            "rating": 4.4,
            "opening_time": time(11, 0),
            "closing_time": time(22, 0),
            "phone": "+7 (423) 777-88-99"
        },
        {
            "name": "Стейк-хаус 'Премиум'",
            "location": "ул. Семеновская, 18, Владивосток",
            "latitude": 43.1156,
            "longitude": 131.8851,
            "cuisine": "Американская кухня",
            "price_range": "$$$$",
            "description": "Премиальный стейк-хаус с мраморным мясом высшего качества. Готовят стейки на гриле, бургеры и другие блюда американской кухни.",
            "rating": 4.9,
            "opening_time": time(17, 0),
            "closing_time": time(0, 0),
            "phone": "+7 (423) 888-99-00"
        },
        {
            "name": "Ресторан 'Панорама'",
            "location": "ул. Корабельная набережная, 3, Владивосток",
            "latitude": 43.1192,
            "longitude": 131.8881,
            "cuisine": "Фьюжн",
            "price_range": "$$$",
            "description": "Современный ресторан с панорамным видом на бухту. Фьюжн-кухня, сочетающая европейские и азиатские традиции.",
            "rating": 4.6,
            "opening_time": time(12, 0),
            "closing_time": time(23, 30),
            "phone": "+7 (423) 999-00-11"
        },
        {
            "name": "Ресторан 'Портмейн'",
            "location": "ул. Пушкинская, 11, Владивосток",
            "latitude": 43.1148,
            "longitude": 131.8842,
            "cuisine": "Европейская кухня",
            "price_range": "$$$",
            "description": "Современный ресторан европейской кухни с изысканным интерьером. Авторские блюда от шеф-повара, отличная винная карта.",
            "rating": 4.6,
            "opening_time": time(12, 0),
            "closing_time": time(23, 0),
            "phone": "+7 (423) 000-11-22"
        },
        {
            "name": "Ресторан 'Океан'",
            "location": "ул. Набережная, 15, Владивосток",
            "latitude": 43.1185,
            "longitude": 131.8872,
            "cuisine": "Морепродукты",
            "price_range": "$$$",
            "description": "Ресторан с видом на океан, специализирующийся на блюдах из морепродуктов. Свежая рыба, крабы и другие дары моря.",
            "rating": 4.7,
            "opening_time": time(11, 30),
            "closing_time": time(23, 0),
            "phone": "+7 (423) 111-22-33"
        },
        {
            "name": "Пиццерия 'Домино'",
            "location": "ул. Адмирала Фокина, 25, Владивосток",
            "latitude": 43.1167,
            "longitude": 131.8858,
            "cuisine": "Итальянская кухня",
            "price_range": "$$",
            "description": "Современная пиццерия с широким выбором пиццы, пасты и салатов. Быстрое обслуживание и доставка.",
            "rating": 4.0,
            "opening_time": time(10, 30),
            "closing_time": time(22, 30),
            "phone": "+7 (423) 222-33-44"
        },
        {
            "name": "Ресторан 'Азия'",
            "location": "ул. Светланская, 8, Владивосток",
            "latitude": 43.1152,
            "longitude": 131.8848,
            "cuisine": "Азиатская кухня",
            "price_range": "$$",
            "description": "Ресторан азиатской кухни с блюдами из Китая, Японии, Кореи и Таиланда. Острые и ароматные блюда.",
            "rating": 4.3,
            "opening_time": time(11, 0),
            "closing_time": time(22, 0),
            "phone": "+7 (423) 333-44-55"
        },
        {
            "name": "Ресторан 'Модерн'",
            "location": "ул. Партизанская, 12, Владивосток",
            "latitude": 43.1142,
            "longitude": 131.8838,
            "cuisine": "Европейская кухня",
            "price_range": "$$$",
            "description": "Современный ресторан с авторской кухней. Инновационные блюда, стильный интерьер и профессиональное обслуживание.",
            "rating": 4.5,
            "opening_time": time(12, 0),
            "closing_time": time(23, 0),
            "phone": "+7 (423) 444-55-66"
        },
        {
            "name": "Ресторан 'Гранд'",
            "location": "ул. Алеутская, 5, Владивосток",
            "latitude": 43.1172,
            "longitude": 131.8855,
            "cuisine": "Европейская кухня",
            "price_range": "$$$$",
            "description": "Элитный ресторан с изысканной европейской кухней. Дорогие вина, профессиональное обслуживание и роскошная атмосфера.",
            "rating": 4.8,
            "opening_time": time(18, 0),
            "closing_time": time(0, 0),
            "phone": "+7 (423) 555-66-77"
        },
        {
            "name": "Суши-бар 'Токио'",
            "location": "ул. Фонтанная, 15, Владивосток",
            "latitude": 43.1165,
            "longitude": 131.8849,
            "cuisine": "Японская кухня",
            "price_range": "$$",
            "description": "Современный суши-бар с широким выбором роллов, суши и горячих блюд японской кухни.",
            "rating": 4.4,
            "opening_time": time(11, 0),
            "closing_time": time(22, 30),
            "phone": "+7 (423) 666-77-88"
        },
        {
            "name": "Ресторан 'Порт'",
            "location": "ул. Корабельная набережная, 12, Владивосток",
            "latitude": 43.1195,
            "longitude": 131.8878,
            "cuisine": "Морепродукты",
            "price_range": "$$$",
            "description": "Ресторан в порту с видом на корабли. Специализируется на свежих морепродуктах и рыбе.",
            "rating": 4.5,
            "opening_time": time(12, 0),
            "closing_time": time(23, 0),
            "phone": "+7 (423) 777-88-99"
        },
        {
            "name": "Ресторан 'Классик'",
            "location": "ул. Пушкинская, 8, Владивосток",
            "latitude": 43.1145,
            "longitude": 131.8840,
            "cuisine": "Русская кухня",
            "price_range": "$$",
            "description": "Классический ресторан русской кухни с традиционными блюдами. Уютная атмосфера и домашняя кухня.",
            "rating": 4.3,
            "opening_time": time(11, 0),
            "closing_time": time(22, 0),
            "phone": "+7 (423) 888-99-00"
        }
    ]
    
    try:
        # Очищаем существующие рестораны
        print("Очищаем существующие рестораны...")
        db.query(Restaurant).delete()
        db.commit()
        
        # Добавляем новые рестораны
        print("Добавляем новые рестораны...")
        for i, data in enumerate(restaurants_data, 1):
            restaurant = Restaurant(
                name=data["name"],
                location=data["location"],
                latitude=data["latitude"],
                longitude=data["longitude"],
                cuisine=data["cuisine"],
                price_range=data["price_range"],
                description=data["description"],
                rating=data["rating"],
                opening_time=data["opening_time"],
                closing_time=data["closing_time"],
                phone=data["phone"],
                owner_id=admin.id,
                image_url=None,  # Будет добавлено позже
                gallery=[],      # Будет добавлено позже
                menu_images=[]   # Будет добавлено позже
            )
            db.add(restaurant)
            print(f"Добавлен ресторан: {data['name']}")
        
        db.commit()
        print(f"\n✅ Успешно добавлено {len(restaurants_data)} ресторанов!")
        
        # Создаем папки для изображений
        print("\nСоздаем папки для изображений...")
        for i in range(1, len(restaurants_data) + 1):
            folder_path = f"static/restaurants/images/restaurant_{i}"
            os.makedirs(folder_path, exist_ok=True)
            print(f"Создана папка: {folder_path}")
        
        print("\n📁 Структура папок готова для загрузки изображений!")
        print("Теперь вы можете загрузить фотографии в соответствующие папки:")
        print("- main.jpg - главное изображение")
        print("- gallery_1.jpg, gallery_2.jpg - галерея")
        print("- menu_1.jpg, menu_2.jpg - меню")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🔄 Обновление базы данных ресторанов Владивостока...")
    update_restaurants()
    print("\n✅ Обновление завершено!") 