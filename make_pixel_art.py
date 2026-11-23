from PIL import Image, ImageDraw
import random, os
random.seed(2026)
O='/mnt/data/gba_vibe_coding_workshop/assets';os.makedirs(O,exist_ok=True)
C={'sky':'#7ac7e8','night':'#172346','deep':'#10172f','paper':'#f8efc5','grass':'#60bc65','darkgrass':'#2f925f','soil':'#ae785b','brick':'#715071','pink':'#ee7190','orange':'#f5ad58','white':'#fff6dc','blue':'#69b6fa','navy':'#26385c','yellow':'#f6d365'}
def rect(d,xy,c): d.rectangle(xy,fill=c)
def sprite(kind,scale=8):
    im=Image.new('RGBA',(32,40)); d=ImageDraw.Draw(im)
    if kind=='hero':
        for box,color in [((10,3,21,7),C['blue']),((7,8,24,23),C['blue']),((9,10,22,17),C['navy']),((12,13,13,15),C['white']),((19,13,20,15),C['white']),((9,24,13,31),C['navy']),((18,24,22,31),C['navy']),((6,23,9,27),C['blue']),((22,23,25,27),C['blue']),((8,31,14,34),C['orange']),((17,31,24,34),C['orange']),((12,4,19,5),C['white'])]:rect(d,box,color)
    if kind=='mage':
        for box,color in [((8,4,23,10),C['pink']),((11,1,20,6),C['pink']),((8,11,23,22),C['orange']),((9,10,22,18),C['paper']),((11,13,12,15),C['navy']),((19,13,20,15),C['navy']),((7,22,24,29),C['pink']),((10,29,14,35),C['navy']),((18,29,22,35),C['navy']),((5,17,8,25),C['orange']),((23,17,26,25),C['orange'])]:rect(d,box,color)
    if kind=='slime':
        for box,color in [((9,12,22,27),C['grass']),((6,17,25,30),C['grass']),((4,24,27,32),C['grass']),((8,29,23,35),C['darkgrass']),((10,22,13,26),C['navy']),((19,22,22,26),C['navy']),((14,28,18,29),C['orange']),((9,17,12,18),C['white'])]:rect(d,box,color)
    return im.resize((32*scale,40*scale),Image.Resampling.NEAREST)
for k in ('hero','mage','slime'):sprite(k).save(f'{O}/{k}.png')
# Large splash illustration from pixel grid
w,h=160,90
im=Image.new('RGB',(w,h),C['sky']); d=ImageDraw.Draw(im)
rect(d,(0,0,159,28),'#5ca6d5'); rect(d,(0,29,159,60),'#77c7e8')
for x,y in [(12,13),(35,23),(76,16),(138,11)]:
  for b in [(x,y,x+19,y+4),(x+3,y-3,x+16,y+6),(x+7,y-6,x+13,y+4)]: rect(d,b,'#f9eecf')
for x,y in [(0,49),(21,39),(49,52),(90,42),(119,48),(147,35)]:
 d.polygon([(x,74),(x+24,y),(x+53,74)],fill='#6593ab')
for y in range(68,90):
 rect(d,(0,y,159,y),C['grass'] if y<72 else (C['soil'] if y<77 else '#805779'))
for x in range(0,160,10):
 rect(d,(x,68,x+7,70),'#92d479');rect(d,(x+1,78,x+4,80),'#d49c77')
for x,y in [(24,55),(87,45),(124,56)]:
 rect(d,(x,y,x+26,y+5),'#e3c27e');rect(d,(x,y-2,x+26,y),'#67b86e');rect(d,(x+1,y+5,x+25,y+7),'#8f6980')
for x,y in [(50,48),(108,19)]:
 rect(d,(x,y,x+8,y+7),C['yellow']);rect(d,(x+2,y+2,x+6,y+6),'#e6a44a')
im=im.resize((1280,720),Image.Resampling.NEAREST); im.save(f'{O}/pixel_world.png')
# Decorative pixel border title card image
im=Image.new('RGB',(320,180),C['deep']); d=ImageDraw.Draw(im)
for i in range(0,320,8):
 rect(d,(i,169,i+5,179),'#3a4565' if i%16==0 else '#253653')
for i in range(0,320,24): rect(d,(i,0,i+12,3),'#2e4167')
for x,y in [(22,25),(275,38),(42,104),(250,107),(195,15)]:
 rect(d,(x,y,x+3,y+3),'#f6d365')
 rect(d,(x+1,y-2,x+2,y+5),'#f6d365')
im.resize((1280,720),Image.Resampling.NEAREST).save(f'{O}/night_bg.png')
