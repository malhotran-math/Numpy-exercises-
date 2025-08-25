# Load the mystery_image.npy file 
with open("mystery_image.npy","rb") as f:
    np.load(f)

plt.imshow(rgb_array)
plt.show() 

# Reduce every value in rgb_array by 50 percent
darker_rgb_array = rgb_array * 0.5

# Convert darker_rgb_array into an array of integers
darker_rgb_int_array = darker_rgb_array.astype(np.int8)
plt.imshow(darker_rgb_int_array)
plt.show()

# Save darker_rgb_int_array to an .npy file called darker_monet.npy
with open("darker_monet.npy","wb") as f:
    np.save(f,darker_rgb_int_array)
