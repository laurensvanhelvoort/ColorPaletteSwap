from extract_palette import ExtractPalette
from apply_palette import ApplyPalette


def main():
    image_path_1 = 'path_to_image_1'
    image_path_2 = 'path_to_image_2'
    num_colors = 50

    extractor = ExtractPalette()
    palette_1 = extractor.create_palette(image_path_1, num_colors)
    palette_2 = extractor.create_palette(image_path_2, num_colors)

    color_grader = ApplyPalette(image_path_1, palette_2)
    swapped_image_1 = color_grader.color_grade_image()
    swapped_image_1.show()

    color_grader = ApplyPalette(image_path_2, palette_1)
    swapped_image_2 = color_grader.color_grade_image()
    swapped_image_2.show()


if __name__ == '__main__':
    main()
