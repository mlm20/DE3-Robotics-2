import numpy as np

def circular_mask(array, radius):
    y, x = np.ogrid[:array.shape[0], :array.shape[1]]
    center_x, center_y = np.array(array.shape[1::-1]) // 2
    mask = ((x - center_x)**2 + (y - center_y)**2 > radius**2).astype(int)
    return np.ma.masked_where(mask, array)


# Create a sample square numpy array
array = np.ones((100, 100))

# Apply the circular mask with a radius of 50
masked_array = circular_mask(array, 50)

masked_array