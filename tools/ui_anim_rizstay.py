"""Flat animated Rizstay UI (owner 23 Nov: animate the product, never show real website footage)."""
import os, sys, math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
F="/home/claude/sutrixa-instagram-media/brand/fonts/"
def font(n,s): return ImageFont.truetype(F+{"b":"Montserrat-Bold.ttf","x":"Montserrat-ExtraBold.ttf","k":"Montserrat-Black.ttf"}[n],s)
CREAM=(247,236,222); PEACH=(244,214,186); GREEN=(36,73,59); GREEN2=(52,104,84); TERRA=(217,102,59); INK=(40,34,30); GREY=(150,140,130); WHITE=(255,255,255); LINE=(228,220,210); YEL=(255,206,64)
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def bg(d, room=False):
    d.rectangle([0,0,W,H],fill=CREAM)
    d.ellipse([760,120,1000,360],fill=(246,190,140))
    d.rectangle([0,1140,W,1270],fill=PEACH)
    d.rectangle([0,1270,W,H],fill=GREEN)
def rr(d,box,r,fill,outline=None,width=0): d.rounded_rectangle(box,r,fill=fill,outline=outline,width=width)
def tap(d,x,y,p):
    if p<=0 or p>=1: return
    r=30+60*p; a=int(255*(1-p))
    d.ellipse([x-r,y-r,x+r,y+r],outline=(255,255,255),width=6)
    d.ellipse([x-22,y-22,x+22,y+22],fill=(255,255,255))
def phone(d,x0,y0,w,h):
    rr(d,[x0-8,y0+14,x0+w+8,y0+h+30],70,(0,0,0,0)) if False else None
    rr(d,[x0,y0,x0+w,y0+h],64,INK); rr(d,[x0+18,y0+18,x0+w-18,y0+h-18],50,WHITE)
    rr(d,[x0+w//2-80,y0+30,x0+w//2+80,y0+66],18,INK)
    return x0+18,y0+18,x0+w-18,y0+h-18
def tablet(d,x0,y0,w,h):
    rr(d,[x0,y0,x0+w,y0+h],40,INK); rr(d,[x0+22,y0+22,x0+w-22,y0+h-22],24,WHITE)
    return x0+22,y0+22,x0+w-22,y0+h-22
def typed(s,p): n=int(len(s)*max(0,min(1,p))); return s[:n]

def checkin(t):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); bg(d)
    a,b,c,e=tablet(d,90,300,900,830)
    d.text((a+40,b+34),"Rizstay · Front desk",font=font("b",30),fill=GREY)
    d.text((a+40,b+78),"New Check-In",font=font("x",50),fill=INK)
    rows=[("Room","204 · Premium",0.3),("Guest","Rohan Mehta",0.9),("Guests","3",1.5),("Nights","2",1.8)]
    y=b+170
    for lab,val,ts in rows:
        d.text((a+40,y),lab,font=font("b",26),fill=GREY)
        rr(d,[a+40,y+36,c-40,y+96],14,(250,247,243),outline=LINE,width=3)
        d.text((a+62,y+50),typed(val,(t-ts)/0.5),font=font("b",32),fill=INK)
        y+=108
    bp=ease((t-2.5)/0.3); bx0,by0,bx1,by1=a+40,e-120,c-40,e-40
    rr(d,[bx0,by0,bx1,by1],18,GREEN if t<2.9 else GREEN2)
    lab="Check in & create guest code"; f=font("x",32); tw=d.textlength(lab,font=f)
    d.text(((bx0+bx1-tw)/2,by0+22),lab,font=f,fill=WHITE)
    tap(d,(bx0+bx1)//2,(by0+by1)//2,(t-2.7)/0.6)
    if t>3.1:   # guest code card pops up
        p=ease((t-3.1)/0.45); cw,ch=760,380; cx,cy=W//2,720+int(60*(1-p))
        card=Image.new("RGBA",(W,H),(0,0,0,0)); cd=ImageDraw.Draw(card)
        cd.rectangle([0,0,W,1270],fill=(0,0,0,int(90*p)))
        rr(cd,[cx-cw//2,cy-ch//2,cx+cw//2,cy+ch//2],34,(255,255,255,int(255*p)))
        cd.ellipse([cx-46,cy-ch//2+36,cx+46,cy-ch//2+128],fill=GREEN+(int(255*p),))
        cd.line([cx-20,cy-ch//2+84,cx-4,cy-ch//2+100,cx+24,cy-ch//2+66],fill=(255,255,255,int(255*p)),width=10)
        f1=font("b",30); f2=font("k",64); f3=font("b",26)
        for txt,fn,yy,col in [("Checked in · Room 204",f1,cy-ch//2+150,INK),("RZ-204-K7",f2,cy-ch//2+200,TERRA),("Guest code: stay, amenities & room service",f3,cy-ch//2+300,GREY)]:
            tw=cd.textlength(txt,font=fn); cd.text((cx-tw/2,yy),txt,font=fn,fill=col+(int(255*p),))
        im=Image.alpha_composite(im.convert("RGBA"),card).convert("RGB")
    return im

def order(t):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); bg(d)
    a,b,c,e=phone(d,230,250,620,990)
    d.text((a+30,b+70),"Room 204 · Rizstay",font=font("b",24),fill=GREY)
    d.text((a+30,b+104),"Room service",font=font("x",44),fill=INK)
    items=[("Milk (warm)","for kids",0.6),("Masala chai","x2",1.2),("Toothbrush kit","amenity",9)]
    y=b+190; qty=[0,0,0]
    for i,(nm,sub,ts) in enumerate(items):
        q=(1 if t>ts else 0)+(1 if i==1 and t>ts+0.5 else 0)
        rr(d,[a+24,y,c-24,y+150],22,(250,245,238))
        rr(d,[a+44,y+24,a+144,y+124],18,PEACH)
        d.ellipse([a+74,y+54,a+114,y+94],fill=TERRA if i<2 else GREY)
        d.text((a+166,y+34),nm,font=font("x",28),fill=INK); d.text((a+166,y+80),sub,font=font("b",24),fill=GREY)
        bx=c-130
        if q==0: rr(d,[bx,y+50,bx+86,y+100],16,TERRA); d.text((bx+30,y+52),"+",font=font("x",38),fill=WHITE)
        else:
            rr(d,[bx-10,y+50,bx+96,y+100],16,GREEN); d.text((bx+24,y+56),f"x{q}",font=font("x",32),fill=WHITE)
        if i<2: tap(d,bx+43,y+75,(t-ts+0.05)/0.5)
        if i==1: tap(d,bx+43,y+75,(t-ts-0.45)/0.5)
        y+=170
    by0=e-150; rr(d,[a+30,by0,c-30,by0+96],24,GREEN)
    lab="Place order"; f=font("x",36); tw=d.textlength(lab,font=f); d.text(((a+c-tw)/2,by0+26),lab,font=f,fill=WHITE)
    tap(d,(a+c)//2,by0+48,(t-2.4)/0.6)
    if t>2.8:
        p=ease((t-2.8)/0.4); ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
        rr(od,[a+30,b+560-int(40*(1-p)),c-30,b+820-int(40*(1-p))],30,GREEN+(int(250*p),))
        for txt,fn,yy in [("Order sent",font("k",50),b+600),("to the kitchen",font("x",36),b+670),("Room 204 · just now",font("b",26),b+740)]:
            tw=od.textlength(txt,font=fn); od.text(((a+c-tw)/2,yy-int(40*(1-p))),txt,font=fn,fill=(255,255,255,int(255*p)))
        im=Image.alpha_composite(im.convert("RGBA"),ov).convert("RGB")
    return im

def kitchen(t):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); bg(d)
    a,b,c,e=tablet(d,70,330,940,800)
    d.text((a+36,b+30),"Rizstay · Kitchen",font=font("b",28),fill=GREY)
    d.text((a+36,b+70),"Live orders",font=font("x",48),fill=INK)
    d.ellipse([c-200,b+88,c-180,b+108],fill=(80,190,110)); d.text((c-168,b+80),"LIVE",font=font("x",28),fill=(80,170,100))
    # existing order cards
    def card(x,y,w,h,title,lines,status,col,glow=0):
        if glow: rr(d,[x-8,y-8,x+w+8,y+h+8],26,(255,214,120))
        rr(d,[x,y,x+w,y+h],22,(250,245,238),outline=LINE,width=3)
        d.text((x+26,y+22),title,font=font("x",32),fill=INK)
        yy=y+74
        for ln in lines: d.text((x+26,yy),ln,font=font("b",26),fill=(90,80,72)); yy+=40
        rr(d,[x+26,y+h-66,x+26+d.textlength(status,font=font("x",24))+36,y+h-22],16,col)
        d.text((x+44,y+h-60),status,font=font("x",24),fill=WHITE)
    cw=(c-a-36*3)//2
    card(a+36,b+170,cw,300,"Table 3",["Paneer tikka x1","Butter naan x2"],"Preparing",TERRA)
    p=ease((t-0.5)/0.5); x=c-36-cw; y=b+170-int(260*(1-p))
    if t>0.5:
        st="NEW · just now" if t<2.6 else "On the way"
        card(x,y,cw,300,"Room 204",["Milk (warm) x1","Masala chai x2"],st,(200,70,50) if t<2.6 else GREEN, glow=1 if 0.9<t<2.6 and int(t*4)%2==0 else 0)
    card(a+36,b+510,cw,220,"Table 7",["Masala dosa x2"],"Ready",GREEN)
    if t>2.3: tap(d,x+100,y+300-44,(t-2.3)/0.6)
    return im

def render(fn,dur,out):
    tmp=out+".d"; os.makedirs(tmp,exist_ok=True)
    for i in range(int(dur*FPS)): globals()[fn](i/FPS).save(f"{tmp}/f{i:04d}.jpg",quality=92)
    subprocess.run(["ffmpeg","-v","error","-y","-framerate",str(FPS),"-i",f"{tmp}/f%04d.jpg","-c:v","libx264","-pix_fmt","yuv420p","-crf","18",out],check=True)
    subprocess.run(["rm","-rf",tmp])
if __name__=="__main__":
    for fn in ["checkin","order","kitchen"]: render(fn,7.0,f"/home/claude/sutrixa-instagram-media/shots/anim/rz_{fn}.mp4")
