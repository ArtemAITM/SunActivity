import cv2
import numpy as np

image = cv2.imread('img.jpg')
rows, cols = 16, 16
height, width, _ = image.shape
sector_height = height // rows
sector_width = width // cols
scale = 16
sectors = []
for i in range(rows):
    for j in range(cols):
        start_y = i * sector_height
        start_x = j * sector_width
        end_y = start_y + sector_height
        end_x = start_x + sector_width
        sector = image[start_y:end_y, start_x:end_x]
        new_size = (sector_width * scale, sector_height * scale)
        resized_sector = cv2.resize(sector, new_size, interpolation=cv2.INTER_LANCZOS4)
        sectors.append(resized_sector)
        cv2.imwrite(f'Sectors/sector_{i}_{j}.jpg', resized_sector)

cv2.destroyAllWindows()
