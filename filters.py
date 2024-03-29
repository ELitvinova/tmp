from math import exp, e
from PIL import Image


class Filter:
    """
    Базовый класс для создания фильтров.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # Этот метод нужно будет реализовать в новых классах.
        return r, g, b

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        # цикл по всем пикселям
        # img.width - ширина картинки
        # img.height - высота картинки
        for i in range(img.width):
            for j in range(img.height):
                # получаем цвет
                r, g, b = img.getpixel((i, j))

                # как-либо меняем цвет
                new_colors = self.apply_to_pixel(r, g, b)

                # сохраняем пиксель обратно
                img.putpixel((i, j), new_colors)
        return img


class RedFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # плавно усиляет красный
        r = int(exp(r / 255) / e * 255)
        return r, g, b


class GreenFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # плавно усиляет зелёный
        g = int(exp(g / 255) / e * 255)
        return r, g, b


class BlueFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # плавно усиляет синий
        b = int(exp(b / 255) / e * 255)
        return r, g, b


class InverseFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # инвертирует цвета
        result = []
        for color in (r, g, b):
            result.append(int((1 - exp(color / 255) / e) * 255))
        return tuple(result)


class BrightFilter(Filter):
    """
    Фильтр, который делает изображение ярче.
    """

    def apply_to_pixel(self, pixel: tuple) -> tuple:
        r, g, b = pixel
        new_pixel = (min(r + 100, 255), min(g + 100, 255), min(b + 100, 255))
        return new_pixel

