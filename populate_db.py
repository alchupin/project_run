import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_run.settings.local')
django.setup()

from django.contrib.auth.models import User
from app_run.models import Run
from datetime import datetime, timedelta
import random

def populate_database():
    # Создание пользователей (тренеров и атлетов)
    coaches = []
    athletes = []
    
    # Создаем тренеров
    for i in range(3):
        coach, created = User.objects.get_or_create(
            username=f'coach_{i+1}',
            defaults={
                'email': f'coach_{i+1}@example.com',
                'is_staff': True,
                'first_name': f'Coach_{i+1}',
                'last_name': f'CoachLastName_{i+1}'
            }
        )
        if created:
            coach.set_password('password123')
            coach.save()
        coaches.append(coach)
    
    # Создаем атлетов
    for i in range(7):
        athlete, created = User.objects.get_or_create(
            username=f'athlete_{i+1}',
            defaults={
                'email': f'athlete_{i+1}@example.com',
                'is_staff': False,
                'first_name': f'Athlete_{i+1}',
                'last_name': f'AthleteLastName_{i+1}'
            }
        )
        if created:
            athlete.set_password('password123')
            athlete.save()
        athletes.append(athlete)
    
    # Комментарии для разнообразия
    comments = [
        "Отличный забег сегодня! Чувствовал себя отлично на протяжении всей дистанции.",
        "Немного устал к концу, но в целом неплохо. Нужно работать над выносливостью.",
        "Погода была идеальной для бега. Улучшил свой личный рекорд на 30 секунд.",
        "Сегодняшний забег был сложным из-за ветра, но справился с задачей.",
        "Пробежал дистанцию быстрее обычного. Отличный день для тренировки!",
        "Немного боли в икрах, но в остальном все прошло хорошо.",
        "Тренировка прошла по плану. Дыхание было стабильным на протяжении всего забега.",
        "Попробовал новый маршрут. Получил массу удовольствия от бега.",
        "Сегодня фокусировался на технике бега. Надеюсь, это поможет в следующих тренировках.",
        "Быстро утомился, нужно больше работать над общей физической подготовкой."
    ]
    
    # Создаем записи о забегах
    all_users = coaches + athletes
    for i in range(10):
        # Случайный пользователь
        user = random.choice(all_users)
        
        # Случайная дата в пределах последних 30 дней
        random_date = datetime.now() - timedelta(days=random.randint(0, 30))
        
        # Случайный комментарий
        comment = random.choice(comments)
        
        # Создаем запись о забеге
        Run.objects.create(
            athlete=user,
            comment=comment,
            created_at=random_date
        )
    
    print("База данных успешно заполнена тестовыми данными!")
    print(f"Создано {len(coaches)} тренеров и {len(athletes)} атлетов")
    print(f"Создано {Run.objects.count()} записей о забегах")

if __name__ == '__main__':
    populate_database()