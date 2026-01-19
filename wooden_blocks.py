# Read number of blocks
blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

# Build pyramid
while blocks >= layer:
    blocks -= layer       # use blocks for the current layer
    height += 1           # one more layer added
    layer += 1            # next layer needs more blocks

print("The height of the pyramid:", height)
