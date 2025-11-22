# ps8.py
# Completed by:

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

# YOUR CODE HERE

if __name__ == "__main__":
    img_path = Path(__file__).with_name('sunflowers.jpeg')
    img = Image.open(img_path.absolute())
    thumbnail = img.copy()
    thumbnail.thumbnail(THUMBNAIL_SIZE)
    
    # YOUR CODE HERE

    # you need to define posterized_img before this
    posterized_img.save(Path(__file__).with_name('sunflowers_quantized.png'))
    posterized_img.show()
