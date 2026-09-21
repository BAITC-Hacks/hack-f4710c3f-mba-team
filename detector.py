import sys

import cv2


# Если красного больше этого процента — считаем изображение дефектным.
RED_THRESHOLD = 10.0


def detect_defect(image_path):
    """Return OK or DEFECT based on the proportion of red pixels."""
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Не удалось открыть изображение: {image_path}")

    # OpenCV читает изображение в формате BGR.
    # В HSV красный цвет удобно выделять двумя диапазонами оттенка.
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red_1 = (0, 100, 100)
    upper_red_1 = (10, 255, 255)
    lower_red_2 = (170, 100, 100)
    upper_red_2 = (180, 255, 255)

    mask_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
    red_mask = mask_1 | mask_2

    red_pixels = cv2.countNonZero(red_mask)
    total_pixels = image.shape[0] * image.shape[1]
    red_percent = red_pixels / total_pixels * 100

    return "DEFECT" if red_percent > RED_THRESHOLD else "OK"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование:")
        print("python3 detector.py путь_к_картинке.png")
        sys.exit(1)

    try:
        print(detect_defect(sys.argv[1]))
    except Exception as error:
        print(f"Ошибка: {error}")
        sys.exit(1)
