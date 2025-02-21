"""Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be
built using these blocks.

Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot
complete the next layer, they finish their work immediately."""

blocks = int(input("Enter number of blocks: "))

height = 0
layer = 1
while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print(height)