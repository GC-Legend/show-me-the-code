#! ./venv/bin/python
# coding=utf-8

def set_num_for_logo(num):
    from PIL import Image,ImageDraw

    base = Image.open('logo_test.jpg').convert('RGBA')

    x,y = base.size

    txt = Image.new('RGBA',base.size,(255,255,255,0))

    d = ImageDraw.Draw(txt)

    d.text((x-10,10),str(num),fill=(255,0,0,255))

    out = Image.alpha_composite(base,txt)

    out.show()

if __name__ == "__main__":
    set_num_for_logo(4)
