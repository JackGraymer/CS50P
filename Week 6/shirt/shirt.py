import sys
from PIL import Image, ImageOps

images = []
extensions = ['.jpg', '.jpeg', '.png']

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

elif sys.argv[1].lower().endswith(tuple(extensions)) == False:
    sys.exit('Invalid input')
elif sys.argv[2].lower().endswith(tuple(extensions)) == False:
    sys.exit('Invalid output')
elif sys.argv[1].split('.')[1] != sys.argv[2].split('.')[1] and sys.argv[1].split('.')[1] not in extensions:
    sys.exit('Input and output have different extensions (File Format)')

try:
    img1= Image.open(sys.argv[1])
    shirt = Image.open('shirt.png')
    img1 = ImageOps.fit(img1, (600, 600))
    #shirt = ImageOps.fit(shirt, (1200, 1200))
    img1.paste(shirt, mask=shirt)
    img1.save(sys.argv[2])


except FileNotFoundError:
    sys.exit('Image file not found')