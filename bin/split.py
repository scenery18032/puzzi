import os
from PIL.Image import open

def splitimage(src, rownum, colnum, dstpath):
    rownum = int(rownum)
    colnum = int(colnum)
    try:
        img = open(src)
    except BaseException:
        return False
    w, h = img.size
    if rownum <= h and colnum <= w:
        s = os.path.split(src)
        if dstpath == '':
            dstpath = s[0]
        fn = s[1].split('.')
        basename = fn[0]
        ext = fn[-1]
        num = 0
        rowheight = h // rownum
        colwidth = w // colnum
        for r in range(rownum):
            for c in range(colnum):
                box = (c * colwidth, r * rowheight, (c + 1) * colwidth, (r + 1) * rowheight)
                img.crop(box).save(os.path.join(dstpath, basename + '_' + str(num) + '.' + ext), ext)
                num = num + 1
        return True
    else:
        print("error")
        return False