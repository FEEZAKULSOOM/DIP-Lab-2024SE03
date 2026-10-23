# Exercise 1: Variables and Data Types
width = 640
height = 480
image_name = "sample.png"
is_color = True

print("--- Exercise 1 ---")
print(width, type(width))
print(height, type(height))
print(image_name, type(image_name))
print(is_color, type(is_color))

total_pixels = width * height
print("Total pixels:", total_pixels)

# Exercise 2: if, elif, and else
def check_pixel(intensity):
    if intensity < 0 or intensity > 255:
        return "Invalid"
    elif intensity >= 128:
        return "Bright pixel"
    else:
        return "Dark pixel"

print("\n--- Exercise 2 ---")
test_values = [-1, 0, 127, 128, 255, 256]
for val in test_values:
    print(f"{val}: {check_pixel(val)}")

# Exercise 3: for and while Loops
print("\n--- Exercise 3 ---")
values = [20, 130, 255]
for val in values:
    if val >= 128:
        print(f"{val}: Bright pixel")
    else:
        print(f"{val}: Dark pixel")

i = 0
while i < 3:
    print(i)
    i += 1

# Exercise 4: Functions
print("\n--- Exercise 4 ---")
def is_bright(pixel, threshold=128):
    return pixel >= threshold

print(is_bright(127))
print(is_bright(128))
print(is_bright(200, 210))

# Exercise 5: Lists and Tuples
print("\n--- Exercise 5 ---")
pixels = [0, 128, 255]
print("First item:", pixels[0])

pixels[1] = 150
pixels.append(64)

print("Updated list:", pixels)
print("List length:", len(pixels))

size = (640, 480)
width, height = size
print("Unpacked width:", width)
print("Unpacked height:", height)

# Explanation: A list item can be changed because lists are mutable data structures. 
# A tuple item cannot be changed because tuples are immutable, meaning their state 
# is permanently fixed in memory once created.

# Exercise 6: Dictionaries and Sets
print("\n--- Exercise 6 ---")
image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print("Image width:", image["width"])
print("Image mode:", image["mode"])

labels = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels)
print("Unique labels count:", len(unique_labels))