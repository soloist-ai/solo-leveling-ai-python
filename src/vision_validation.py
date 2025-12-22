"""
Локальное тестирование валидации задач по фото
Использует структуру промптов как в основном проекте
Запуск: python vision_validation.py
"""

import base64
import logging
from pathlib import Path

from src.services.task_aprove_service import TaskValidationService
from src.avro.enums.localization_item import LocalizationItem

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def encode_image(image_path: str) -> str:
    """Конвертирует изображение в base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def test_task_validation(
        task_title_en: str,
        task_title_ru: str,
        task_desc_en: str,
        task_desc_ru: str,
        image_path: str
):
    """
    Тестирует валидацию одной задачи

    Args:
        task_title_en: Название задачи (английский)
        task_title_ru: Название задачи (русский)
        task_desc_en: Описание задачи (английский)
        task_desc_ru: Описание задачи (русский)
        image_path: Путь к фото-доказательству
    """
    print("\n" + "=" * 80)
    print("🔍 TASK VALIDATION TEST - Solo Leveling AI")
    print("=" * 80)

    # Проверяем существование файла
    if not Path(image_path).exists():
        print(f"❌ Error: Image not found at {image_path}")
        print("Please add a test image to test_photos/ directory")
        return

    print(f"\n📋 Task (EN): {task_title_en}")
    print(f"   Description: {task_desc_en}")
    print(f"\n📋 Task (RU): {task_title_ru}")
    print(f"   Описание: {task_desc_ru}")
    print(f"\n📸 Image: {image_path}")

    try:
        # Создаем сервис
        print("\n🤖 Initializing Vision LLM...")
        service = TaskValidationService()

        # Подготавливаем данные
        task_title = LocalizationItem(en=task_title_en, ru=task_title_ru)
        task_description = LocalizationItem(en=task_desc_en, ru=task_desc_ru)
        image_base64 = encode_image(image_path)

        # Запускаем валидацию
        print("🔍 Analyzing photo evidence...")
        result = service.validate_task_completion(
            task_title=task_title,
            task_description=task_description,
            image_base64=image_base64
        )

        # Выводим результат
        print("\n" + "=" * 80)
        if result.is_valid:
            print("✅ TASK VALIDATED - User completed the task successfully!")
        else:
            print("❌ TASK REJECTED - Evidence insufficient or invalid")
        print("=" * 80)

        print(f"\n📊 Confidence Level: {result.confidence:.1%}")

        print(f"\n💬 Feedback (English):")
        print(f"   {result.feedback.en}")

        print(f"\n💬 Обратная связь (Русский):")
        print(f"   {result.feedback.ru}")

        print("\n" + "=" * 80 + "\n")

    except Exception as e:
        logger.error(f"Validation failed: {e}", exc_info=True)
        print(f"\n❌ Error during validation: {e}\n")


# ========== ТЕСТОВЫЕ СЦЕНАРИИ ==========

if __name__ == "__main__":
    print("🚀 Starting Task Validation Tests...\n")

    # СЦЕНАРИЙ 1: Физическая активность + музыка (TIME-based)
    # print("📍 Test Case 1: Physical Activity + Music")
    # test_task_validation(
    #     task_title_en="Jog for 30 minutes while listening to music",
    #     task_title_ru="Пробежка 30 минут с прослушиванием музыки",
    #     task_desc_en="Run outdoors for 30 minutes while listening to an album (minimum 10 tracks)",
    #     task_desc_ru="Бегайте на улице 30 минут, слушая альбом (минимум 10 треков)",
    #     image_path="./test_photos/jogging_example.jpg"
    #)

    # СЦЕНАРИЙ 2: Чтение (TIME-based)
    # print("📍 Test Case 2: Reading")
    # test_task_validation(
    #     task_title_en="Read a book for 40 minutes",
    #     task_title_ru="Читайте книгу 40 минут",
    #     task_desc_en="Read any book for at least 40 minutes without interruptions",
    #     task_desc_ru="Читайте любую книгу минимум 40 минут без перерывов",
    #     image_path="./test_photos/reading_example.jpg"
    # )

    # СЦЕНАРИЙ 3: Готовка (COMPLEXITY-based)
    print("📍 Test Case 3: Nutrition/Cooking")
    test_task_validation(
        task_title_en="Cook a healthy breakfast with 4 ingredients",
        task_title_ru="Приготовьте здоровый завтрак из 4 ингредиентов",
        task_desc_en="Prepare a healthy breakfast with 4 different ingredients including vegetables and protein",
        task_desc_ru="Приготовьте здоровый завтрак из 4 разных ингредиентов, включая овощи и белок",
        image_path="./test_photos/kasha.jpg"
    )

    #СЦЕНАРИЙ 4: Физическая активность (COMPLEXITY-based - repetitions)
    # print("📍 Test Case 4: Physical Activity - Repetitions")
    # test_task_validation(
    #     task_title_en="Complete 50 push-ups in one session",
    #     task_title_ru="Выполните 50 отжиманий за один подход",
    #     task_desc_en="Do 50 push-ups with proper form in a single workout session",
    #     task_desc_ru="Сделайте 50 отжиманий с правильной техникой за одну тренировку",
    #     image_path="./test_photos/i.jpg"
    # )
    #
    # print("✅ All validation tests completed!")
