import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class ExtractPalette:
    def load_image(self, image_path):
        return cv2.imread(image_path)

    def preprocess_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = image.reshape(-1, 3)
        return image

    def extract_colors(self, image, num_colors):
        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(image)
        dominant_colors = kmeans.cluster_centers_
        return dominant_colors.astype(int)

    def display_palette(self, colors):
        colors_lab = cv2.cvtColor(np.uint8([colors]), cv2.COLOR_RGB2Lab).reshape(-1, 3)
        brightness_values = colors_lab[:, 0]
        sorted_indices = np.argsort(brightness_values)
        sorted_colors = colors[sorted_indices]

        num_colors = sorted_colors.shape[0]
        palette = np.zeros((100, 100 * num_colors, 3), dtype=np.uint8)

        for i, color in enumerate(sorted_colors):
            palette[:, i * 100: (i + 1) * 100, :] = color

        plt.imshow(palette)
        plt.axis('off')
        plt.show()

    def create_palette(self, image_path, num_colors):
        image = self.load_image(image_path)
        preprocessed_image = self.preprocess_image(image)
        dominant_colors = self.extract_colors(preprocessed_image, num_colors)
        self.display_palette(dominant_colors)
        return dominant_colors
