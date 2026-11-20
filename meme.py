
from PIL import Image, ImageDraw, ImageFont
import math
W=H=1080
im=Image.new('RGB',(W,H))
d=ImageDraw.Draw(im)
for y in range(H):
    t=y/H
    if t<0.5:
        u=t/0.5
        c=(int(90+(233-90)*u), int(10+(60-10)*u), int(150+(120-150)*u))
    else:
        u=(t-0.5)/0.5
        c=(int(233+(255-233)*u), int(60+(160-60)*u), int(120+(110-120)*u))
    d.line([(0,y),(W,y)],fill=c)
d.ellipse([W//2-130,470-130,W//2+130,470+130],fill=(255,215,130))
for y in range(340,600,18):
    d.line([(W//2-140,y),(W//2+140,y)],fill=(255,90,160),width=6)
d.rectangle([0,760,W,H],fill=(255,120,175))
for y in range(760,H,22):
    d.line([(0,y),(W,y)],fill=(255,150,195),width=4)
def palm(px,py,s):
    d.line([(px,py),(px,py-280*s)],fill=(35,5,30),width=int(20*s))
    for ang in (-75,-45,-15,15,45,75):
        a=math.radians(ang-90)
        ex=px+math.cos(a)*140*s; ey=py-280*s+math.sin(a)*80*s
        d.line([(px,py-280*s),(ex,ey)],fill=(35,5,30),width=int(12*s))
palm(110,770,1.0); palm(965,770,1.15)
panel=[80,110,W-80,400]
d.rounded_rectangle(panel,30,fill=(22,4,18))
d.rounded_rectangle(panel,30,outline=(255,60,170),width=8)
fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',54)
f2=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',40)
f3=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',30)
d.text((120,145),"GRAND THEFT AUTO VI",font=fb,fill=(255,255,255))
d.text((120,220),"Downloading... 13 years remaining",font=f2,fill=(255,150,200))
d.rounded_rectangle([120,290,W-120,352],20,fill=(60,10,45))
d.rounded_rectangle([120,290,120+int((W-240)*0.955),352],20,fill=(255,60,170))
d.text((132,298),'95%  stuck at "Installing rockstar servers"',font=f3,fill=(255,255,255))
d.text((W//2-330,24),"me on Nov 19, 2026:",font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',48),fill=(255,255,255))
def sparkle(dr,cx,cy,r,color):
    pts=[]
    for i in range(8):
        ang=math.radians(i*45-90)
        rr=r if i%2==0 else r*0.38
        pts.append((cx+math.cos(ang)*rr, cy+math.sin(ang)*rr))
    dr.polygon(pts,fill=color)
def ghost(dr,gx,gy,s):
    ow=int(14*s)
    ax,ay=gx+95*s,gy
    dr.ellipse([ax-34*s,ay-34*s,ax+34*s,ay+34*s],fill=(255,255,255),outline=(20,5,20),width=ow)
    cx2,cy2=ax+48*s,ay-58*s
    dr.ellipse([cx2-46*s,cy2-46*s,cx2+46*s,cy2+46*s],fill=(226,26,140),outline=(20,5,20),width=ow)
    sparkle(dr,cx2,cy2,22*s,(255,255,255))
    dr.ellipse([gx-85*s,gy-105*s,gx+85*s,gy+85*s],fill=(255,255,255))
    dr.rectangle([gx-85*s,gy,gx+85*s,gy+85*s],fill=(255,255,255))
    for sx in (-56,0,56):
        dr.ellipse([gx+sx-58*s,gy+45*s,gx+sx+58*s,gy+105*s],fill=(255,255,255))
    dr.arc([gx-85*s,gy-105*s,gx+85*s,gy+85*s],180,360,fill=(20,5,20),width=ow)
    dr.line([(gx-85*s,gy-10*s),(gx-85*s,gy+60*s)],fill=(20,5,20),width=ow)
    dr.line([(gx+85*s,gy-10*s),(gx+85*s,gy+60*s)],fill=(20,5,20),width=ow)
    for sx in (-56,0,56):
        dr.arc([gx+sx-58*s,gy+45*s,gx+sx+58*s,gy+105*s],0,180,fill=(20,5,20),width=ow)
    sparkle(dr,gx-38*s,gy-30*s,22*s,(20,5,20))
    sparkle(dr,gx+30*s,gy-40*s,22*s,(20,5,20))
ghost(d,340,880,1.35)
wm=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',58)
d.text((W//2-40,H-130),"make.fun",font=wm,fill=(255,255,255))
sparkle(d,W//2-85,H-100,26,(255,255,255))
im.save('meme.png')
print('ok')

