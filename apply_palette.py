from PIL import Image
import numpy as np


class ApplyPalette:
    def __init__(self, image_path, color_palette):
        self.image_path = image_path
        self.color_palette = np.array(color_palette)

    def _load_image(self):
        return Image.open(self.image_path)

    def _find_closest_color(self, pixel_rgb):
        distances = np.sqrt(np.sum((self.color_palette - pixel_rgb) ** 2, axis=1))
        closest_color_index = np.argmin(distances)
        return self.color_palette[closest_color_index]

    def color_grade_image(self):
        image = self._load_image()
        image_np = np.array(image)
        image_flat = image_np.reshape(-1, 3)

        for i in range(len(image_flat)):
            pixel_rgb = image_flat[i]
            closest_color = self._find_closest_color(pixel_rgb)
            image_flat[i] = closest_color

        color_graded_image_np = image_flat.reshape(image_np.shape)
        color_graded_image = Image.fromarray(color_graded_image_np.astype(np.uint8))
        return color_graded_image
