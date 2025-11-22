# ps8.py
# Completed by: Nazeub

# Please read the README completely before getting started
# Please make sure you read Chapter 6 of CCSPiP
# You will probably need all of these imports, with the possible exception of itertools
from pathlib import Path
from data_point import DataPoint
from kmeans import KMeans
from PIL import Image
import itertools

NUM_COLORS = 7
THUMBNAIL_SIZE = (256, 256)

def image_to_datapoints(image):
    pixels = list(image.getdata())
    return [DataPoint(pixel) for pixel in pixels]

def kmeans_clusters(datapoints, k):
    kmeans = KMeans(k, datapoints)
    clusters = kmeans.run()
    return clusters

def centroids_as_palette(clusters):
    # Convert centroids to integer RGB tuples
    return [tuple(map(int, c.centroid.dimensions)) for c in clusters]

def posterize_with_palette(image, palette):
    # PIL palette needs 256 colors, so pad if necessary
    palette_img = Image.new("P", (1, 1))
    palette_flat = [channel for color in palette for channel in color]
    while len(palette_flat) < 256 * 3:
        palette_flat.extend([0, 0, 0])
    palette_img.putpalette(palette_flat)
    return image.quantize(palette=palette_img, dither=Image.Dither.NONE)

if __name__ == "__main__":
    img_path = Path(__file__).with_name('sunflowers.jpeg')
    img = Image.open(img_path.absolute())
    thumbnail = img.copy()
    thumbnail.thumbnail(THUMBNAIL_SIZE)
    
    # 1. Convert thumbnail pixels to DataPoints
    datapoints = image_to_datapoints(thumbnail)
    # 2. Run k-means clustering to find NUM_COLORS clusters
    clusters = kmeans_clusters(datapoints, NUM_COLORS)
    # 3. Extract RGB tuples for palette from cluster centroids
    palette = centroids_as_palette(clusters)
    # 4. Posterize the original image using this palette
    posterized_img = posterize_with_palette(img, palette)

    # Save/show output image
    posterized_img.save(Path(__file__).with_name('sunflowers_quantized.png'))
    posterized_img.show()
