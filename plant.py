from __future__ import division
from PIL import Image

plants = ['plant1.png', 'plant2.png', 'plant3.png']

for p in plants:
    im = Image.open(p)
    px = im.load()
    xmax = im.size[0]
    ymax = im.size[1]
    count = 0
    total_px = xmax * ymax
    for a in range(1, xmax):
        for b in range(1, ymax):
            comp = cmp(px[a, b], (225, 225, 225, 225))
            red = px[a,b][0]
            green = px[a,b][1]
            blue = px[a,b][2]
            threshold = 20

            if comp == 1:
                pass
            else:
                if green > (red + threshold) and green > (blue + threshold):
                    count += 1
                    px[a,b] = (253, 0, 193, 255)
    im.save("out_{}".format(p))
    percent = float(count/total_px)*100
    print "percentage of green pixels in {0} is {1}".format(p,percent)
