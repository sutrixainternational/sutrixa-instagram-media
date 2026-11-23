"""Flat 2D family Reel v2 (owner 23 Nov: better animation, real music, built to go viral)."""
import json, math, os, subprocess, sys
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(__file__)); import ui_anim
W,H,FPS=1080,1920,30
FD="/home/claude/ep_family/fonts/"; FB="/home/claude/sutrixa-instagram-media/brand/"
def dev(s): return ImageFont.truetype(FD+"Mukta-ExtraBold.ttf",s)
def lat(s): return ImageFont.truetype(FB+"fonts/Montserrat-ExtraBold.ttf",s)
INK=(40,34,30); GREEN=(36,73,59); TERRA=(217,102,59); WOOD=(150,95,60); WOOD2=(120,74,46); YEL=(255,206,64)
LOGO=Image.open(FB+"logo.png").convert("RGBA"); LOGO=LOGO.resize((110,int(110*LOGO.height/LOGO.width)))
D=json.load(open("vo2/durs.json")); L={l[0]:l for l in json.load(open("lines2.json"))}
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def easeio(x): x=max(0,min(1,x)); return x*x*(3-2*x)
ACT={}
for k in D:
    a,sr=sf.read(f"vo2/{k}.wav"); a=a if a.ndim==1 else a.mean(1); hop=sr//FPS
    ACT[k]=[float(np.sqrt((a[i:i+hop]**2).mean())) for i in range(0,len(a),hop)]
SC=[("car",0.0,3.0,[("k1",0.2)],None),
    ("arrive",3.0,5.8,[("r1",3.45)],None),
    ("desk",5.8,8.9,[("p1",6.05)],None),
    ("ui_checkin",8.9,11.4,[("n1",9.1)],"चेक-इन: 1 मिनट"),
    ("room",11.4,14.2,[("a1",11.65)],None),
    ("ui_order",14.2,16.8,[],"कमरे से ऑर्डर"),
    ("ui_kitchen",16.8,19.4,[("n2",17.0)],"सीधा किचन में"),
    ("door",19.4,22.6,[("k2",20.7)],None),
    ("payoff",22.6,26.4,[("r2",22.85)],None),
    ("end",26.4,28.0,[],None)]
TOTAL=28.0
SPK={"k1":"kabir","k2":"kabir","r1":"rohan","r2":"rohan","p1":"priya","a1":"ananya"}
def talking(who,t):
    for s in SC:
        for ln,at in s[3]:
            if SPK.get(ln)==who and at<=t<at+D[ln]:
                i=int((t-at)*FPS); return min(1,ACT[ln][min(i,len(ACT[ln])-1)]*11)
    return 0
def speaking_now(who,t):
    for s in SC:
        for ln,at in s[3]:
            if SPK.get(ln)==who and at<=t<at+D[ln]: return True
    return False
def line_at(t):
    for s in SC:
        for ln,at in s[3]:
            if at-0.05<=t<at+D[ln]+0.3: return ln
SKIN={"rohan":(196,138,98),"ananya":(210,156,118),"kabir":(205,150,110),"priya":(214,162,124),"waiter":(186,128,90)}
SHIRT={"rohan":(52,98,170),"ananya":(225,110,60),"kabir":(244,196,60),"priya":(128,30,48),"waiter":(250,250,250)}
PANTS={"rohan":(70,70,82),"ananya":(60,52,60),"kabir":(50,90,170),"priya":(50,40,48),"waiter":(40,40,44)}
def person(d,who,x,feet,s=1.0,t=0.0,sit=False,arm=None,hold=None,walk=None,mood="smile",lean=0):
    tk=talking(who,t); spk=speaking_now(who,t)
    kid=who=="kabir"; s2=s*(0.62 if kid else 1.0)
    bob=(abs(math.sin(walk*math.pi))*10*s2 if walk is not None else math.sin(t*2.6+x*0.01)*3*s2)
    hh=int(70*s2); body_h=int(200*s2); leg=int(170*s2) if not sit else int(60*s2)
    sk=SKIN[who]; sh=SHIRT[who]; pa=PANTS[who]; cx=x+lean
    lw=int(26*s2)
    if sit:
        d.rounded_rectangle([cx-50*s2,feet-leg-10*s2,cx+75*s2,feet-leg+30*s2],12,fill=pa)
        d.rounded_rectangle([cx+45*s2,feet-leg,cx+73*s2,feet],10,fill=pa)
    else:
        for k,dx in enumerate((-22,22)):
            sw=(math.sin(walk*math.pi*2+k*math.pi)*30*s2) if walk is not None else 0
            fx=cx+dx*s2+sw; d.line([cx+dx*s2,feet-leg-bob+10,fx,feet],fill=pa,width=lw)
            d.rounded_rectangle([fx-lw/2-6*s2,feet-12*s2,fx+lw/2+12*s2,feet+4*s2],8,fill=INK)
    bw=int(118*s2); by0=feet-leg-body_h-bob
    d.rounded_rectangle([cx-bw/2,by0,cx+bw/2,by0+body_h],int(40*s2),fill=sh)
    if who=="ananya": d.polygon([(cx-bw/2+8,by0+10),(cx-bw/2+34,by0),(cx+bw/2-6,by0+body_h-20),(cx+bw/2-30,by0+body_h-6)],fill=(246,232,206))
    if who=="waiter": d.rounded_rectangle([cx-bw/2+14,by0+30,cx+bw/2-14,by0+body_h],20,fill=(30,30,34))
    if who=="priya": d.polygon([(cx-18*s2,by0),(cx,by0+50*s2),(cx+18*s2,by0)],fill=(250,250,250))
    aw=int(24*s2); armc=sh if who!="waiter" else (250,250,250)
    # arm angles (radians from straight down); gesture while speaking
    la=0.15; ra=0.15
    if walk is not None: la=0.15+0.35*math.sin(walk*math.pi*2); ra=0.15-0.35*math.sin(walk*math.pi*2)
    if spk and not kid: ra=1.1+0.35*math.sin(t*7)
    if arm=="up": ra=2.6+0.25*math.sin(t*9)
    if arm=="both": ra=2.5+0.3*math.sin(t*9); la=-2.5-0.3*math.sin(t*9+1)
    if arm=="tummy": la=-0.9; ra=0.9
    for side,ang in ((-1,la),(1,ra)):
        sx=cx+side*(bw/2-8); sy=by0+26*s2; ln=150*s2
        ex=sx+side*math.sin(abs(ang))*ln*(1 if ang>=0 else 1); ey=sy+math.cos(ang)*ln
        if side==-1: ex=sx-math.sin(abs(ang))*ln
        d.line([sx,sy,ex,ey],fill=armc,width=aw); d.ellipse([ex-15*s2,ey-15*s2,ex+15*s2,ey+15*s2],fill=sk)
        if side==1 and hold=="phone": d.rounded_rectangle([ex-14*s2,ey-50*s2,ex+20*s2,ey+6*s2],7,fill=INK)
        if side==1 and hold=="cup":
            d.rounded_rectangle([ex-4,ey-40*s2,ex+34*s2,ey+4],8,fill=(250,250,250))
            for k in range(3):
                yy=ey-60*s2-((t*40+k*20)%60)*s2; xx=ex+14*s2+8*math.sin(t*4+k)
                d.ellipse([xx-6*s2,yy-6*s2,xx+6*s2,yy+6*s2],fill=(255,255,255,))
        if side==1 and hold=="tray":
            tx0,ty=ex-40*s2,ey-30*s2
            d.rounded_rectangle([tx0,ty,tx0+170*s2,ty+16*s2],8,fill=(190,190,196))
            d.rounded_rectangle([tx0+20*s2,ty-62*s2,tx0+52*s2,ty],6,fill=(255,255,255))
            for k in (78,120): d.rounded_rectangle([tx0+k*s2,ty-36*s2,tx0+(k+32)*s2,ty],6,fill=(200,120,70))
            for k in range(2):
                yy=ty-50*s2-((t*40+k*25)%50)*s2; d.ellipse([tx0+(92+k*42)*s2-5,yy-5,tx0+(92+k*42)*s2+5,yy+5],fill=(255,255,255))
    hy=by0-2*hh+12*s2
    d.rectangle([cx-14*s2,by0-24*s2,cx+14*s2,by0+4],fill=sk)
    d.ellipse([cx-hh,hy,cx+hh,hy+2*hh],fill=sk)
    hair=(30,24,22)
    if who in("rohan","waiter","kabir"): d.chord([cx-hh-2,hy-8*s2,cx+hh+2,hy+hh*1.1],180,360,fill=hair)
    if who=="rohan": d.chord([cx-hh+6,hy+hh*0.9,cx+hh-6,hy+2*hh+10*s2],0,180,fill=(60,44,36))
    if who=="ananya":
        d.rounded_rectangle([cx-hh-10*s2,hy-6*s2,cx+hh+10*s2,hy+2*hh+60*s2],int(60*s2),fill=hair)
        d.ellipse([cx-hh,hy+8*s2,cx+hh,hy+2*hh],fill=sk); d.chord([cx-hh,hy-4*s2,cx+hh,hy+hh*0.9],180,360,fill=hair)
    if who=="priya":
        d.ellipse([cx-28*s2,hy-36*s2,cx+28*s2,hy+16*s2],fill=hair); d.chord([cx-hh-2,hy-4*s2,cx+hh+2,hy+hh],180,360,fill=hair)
    ey=hy+hh*1.05; blink=((t+x*0.003)%3.3)<0.12
    for ex in (-22,22):
        if blink: d.line([cx+ex*s2-7*s2,ey,cx+ex*s2+7*s2,ey],fill=INK,width=max(3,int(4*s2)))
        else: d.ellipse([cx+ex*s2-6*s2,ey-7*s2,cx+ex*s2+6*s2,ey+7*s2],fill=INK)
    if mood=="pout": 
        for ex in (-22,22): d.line([cx+ex*s2-10*s2,ey-16*s2+(4 if ex<0 else -4)*s2,cx+ex*s2+10*s2,ey-16*s2+(-4 if ex<0 else 4)*s2],fill=INK,width=4)
    my=hy+hh*1.45; mo=tk*14*s2
    if mo>2: d.ellipse([cx-12*s2,my-3*s2,cx+12*s2,my+mo],fill=(120,40,40))
    elif mood=="pout": d.arc([cx-14*s2,my,cx+14*s2,my+18*s2],200,340,fill=INK,width=4)
    elif mood=="wow": d.ellipse([cx-10*s2,my-4*s2,cx+10*s2,my+16*s2],fill=(120,40,40))
    else: d.arc([cx-16*s2,my-12*s2,cx+16*s2,my+8*s2],20,160,fill=INK,width=max(3,int(4*s2)))
def ground(d,top,color): d.rectangle([0,top,W,1290],fill=color); d.rectangle([0,1290,W,H],fill=GREEN)
def tree(d,x,y,r): d.rectangle([x-10,y,x+10,y+220],fill=(110,74,50)); d.ellipse([x-r,y-r,x+r,y+r],fill=(92,150,110))
def car_side(d,cx,cy,t,moving):
    d.rounded_rectangle([cx,cy,cx+440,cy+130],40,fill=(214,64,48)); d.rounded_rectangle([cx+80,cy-72,cx+330,cy+20],40,fill=(214,64,48))
    d.rounded_rectangle([cx+110,cy-56,cx+205,cy+10],12,fill=(200,226,236)); d.rounded_rectangle([cx+219,cy-56,cx+310,cy+10],12,fill=(200,226,236))
    for wx in (cx+95,cx+345):
        d.ellipse([wx-44,cy+90,wx+44,cy+178],fill=INK); d.ellipse([wx-20,cy+114,wx+20,cy+154],fill=(200,200,200))
        a=t*(25 if moving else 0)
        for k in range(3): ang=a+k*2.09; d.line([wx,cy+134,wx+18*math.cos(ang),cy+134+18*math.sin(ang)],fill=INK,width=4)
def car(t,lt):
    im=Image.new("RGB",(W,H),(246,232,214)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([60,260,1020,860],60,fill=(170,200,214))
    for i in range(6):   # scenery rushing past
        x=int((i*360-lt*900)%1800)-300; tree(d,x,560,90); 
    d.rectangle([60,760,1020,860],fill=(205,180,150))
    d.rounded_rectangle([40,240,1040,880],70,outline=(90,90,100),width=40)
    d.rectangle([0,880,W,1290],fill=(80,70,72)); d.rounded_rectangle([60,980,1020,1290],40,fill=(110,96,96))
    d.rectangle([0,1290,W,H],fill=GREEN)
    jig=math.sin(lt*20)*4
    person(d,"ananya",330,1180+jig,1.0,t,sit=True)
    person(d,"kabir",700,1210+jig,1.25,t,sit=True,mood="pout",arm="tummy")
    return im
def arrive(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im)
    for y in range(0,1250,10):
        p=y/1250; d.rectangle([0,y,W,y+10],fill=tuple(int(a+(b-a)*p) for a,b in zip((248,200,160),(250,232,212))))
    d.ellipse([740,180,940,380],fill=(246,176,120))
    d.rectangle([150,520,930,1150],fill=(246,236,220)); d.rounded_rectangle([250,440,830,530],14,fill=GREEN)
    f=lat(46); s="ARANYA RETREAT"; d.text(((W-d.textlength(s,font=f))/2,460),s,font=f,fill=(240,222,190))
    for r in range(3):
        for c in range(4): d.rectangle([210+c*180,620+r*170,320+c*180,730+r*170],fill=(196,222,228))
    tree(d,90,900,110); tree(d,1000,880,120)
    d.rectangle([0,1150,W,1290],fill=(222,196,170)); d.rectangle([0,1290,W,H],fill=GREEN)
    p=ease(lt/0.7); cx=int(-500+600*p); moving=lt<0.7
    if moving:
        for k in range(5): d.line([cx-40-k*60,1080+k*18,cx-200-k*60,1080+k*18],fill=(255,255,255),width=6)
    car_side(d,cx,1040,t,moving)
    if 0.6<lt<1.3:
        for k in range(4): r=20+(lt-0.6)*90; d.ellipse([cx-30-k*40-r,1200-r*0.5,cx-30-k*40+r,1200+r*0.5],fill=(230,214,196))
    if lt>0.9:
        w=min(1,(lt-0.9)/0.6); x=640+int(140*w)
        person(d,"rohan",x,1250,1.05,t,walk=(lt*2.2 if w<1 else None))
    return im
def interior(d,floor=1180): d.rectangle([0,0,W,floor],fill=(246,232,214)); ground(d,floor,(214,180,148))
def desk(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); interior(d)
    d.rounded_rectangle([90,240,390,760],150,fill=(200,224,232)); d.rectangle([90,400,390,760],fill=(200,224,232))
    d.line([660,0,660,300],fill=(150,120,90),width=4); d.ellipse([630,300,690,360],fill=(248,196,140))
    person(d,"priya",330,1180,1.05,t,arm="up" if 1.2<lt<1.8 else None)
    d.rounded_rectangle([80,880,620,1190],16,fill=WOOD); d.rectangle([80,880,620,910],fill=WOOD2)
    d.rounded_rectangle([110,812,410,868],12,fill=GREEN); f=lat(34); s="RECEPTION"; d.text((260-d.textlength(s,font=f)/2,820),s,font=f,fill=(240,222,190))
    d.polygon([(450,790),(600,790),(580,880),(470,880)],fill=(60,60,66))
    # bell ding ring
    if lt<0.5: r=20+lt*200; d.ellipse([520-r,740-r,520+r,740+r],outline=(255,206,64),width=6)
    d.pieslice([495,850,545,900],180,360,fill=(220,180,60))
    person(d,"ananya",720,1230,0.95,t); person(d,"kabir",820,1230,1.0,t,mood="pout"); person(d,"rohan",950,1230,1.0,t)
    return im
def room(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); interior(d,1150)
    d.rectangle([600,260,960,700],fill=(196,224,232)); d.rectangle([560,230,640,760],fill=TERRA); d.rectangle([920,230,1000,760],fill=TERRA)
    d.rounded_rectangle([60,760,660,1060],30,fill=(250,246,240)); d.rounded_rectangle([60,700,140,1060],20,fill=WOOD); d.rectangle([60,960,660,1060],fill=(235,214,190))
    person(d,"ananya",360,1080,0.95,t,sit=True,hold="phone")
    jump=abs(math.sin(lt*6))*80
    person(d,"kabir",580,1000-jump,1.1,t,arm="both" if lt<1.5 else "tummy",mood="pout" if lt<1.8 else "wow")
    if lt>1.9:   # phone ping
        p=ease((lt-1.9)/0.3); r=int(90*p); d.rounded_rectangle([300-r*2,600-r//2,300+r*2,600+r//2],30,fill=(255,255,255))
        if p>0.8: f=dev(40); s="ऑर्डर भेजा ✓".replace("✓",""); d.text((300-d.textlength(s,font=f)/2,578),s,font=f,fill=GREEN)
    return im
def door(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); interior(d)
    d.rectangle([520,300,1000,1180],fill=WOOD2); d.rectangle([550,330,970,1180],fill=(250,238,214))
    if lt<0.6:   # knock knock
        for k in range(2):
            if lt>k*0.25: f=lat(60); d.text((540+k*240,230+k*30),"KNOCK!",font=f,fill=TERRA)
    p=ease((lt-0.5)/0.5); d.polygon([(550,330),(550+int(320*p),360),(550+int(320*p),1150),(550,1180)],fill=WOOD) if lt>0.5 else d.rectangle([550,330,970,1180],fill=WOOD)
    if lt>0.8:
        w=ease((lt-0.8)/1.0); x=int(1180-420*w)
        person(d,"waiter",x,1180,1.0,t,hold="tray",walk=(lt*2.2 if w<1 else None))
    person(d,"kabir",300,1220-abs(math.sin(lt*7))*50*(lt>1.2),1.1,t,arm="both" if lt>1.2 else None,mood="wow" if lt>1.0 else "smile")
    return im
def payoff(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); interior(d,1150)
    d.rectangle([600,260,960,700],fill=(196,224,232)); d.rectangle([560,230,640,760],fill=TERRA); d.rectangle([920,230,1000,760],fill=TERRA)
    d.rounded_rectangle([60,760,1020,1060],30,fill=(250,246,240)); d.rectangle([60,960,1020,1060],fill=(235,214,190))
    person(d,"ananya",250,1080,0.95,t,sit=True)
    person(d,"kabir",460,1060,1.1,t,sit=True,hold="cup")
    person(d,"rohan",740,1080,1.05,t,sit=True,hold="cup")
    return im
def end(t,lt):
    g=Image.new("RGB",(W,H),(10,18,40)); gd=ImageDraw.Draw(g); gd.ellipse([140,420,940,1200],fill=(30,70,140)); im=g.filter(ImageFilter.GaussianBlur(160))
    p=ease(lt/0.5); lg=Image.open(FB+"logo.png").convert("RGBA"); s=int(480*(0.85+0.15*p)); lg=lg.resize((s,int(s*lg.height/lg.width)))
    im=im.convert("RGBA"); im.alpha_composite(lg,((W-lg.width)//2,560)); im=im.convert("RGB"); d=ImageDraw.Draw(im)
    f=lat(64); s="Rizstay"; d.text(((W-d.textlength(s,font=f))/2,1110),s,font=f,fill=(255,255,255))
    f=lat(36); s="restaurant.rizstay.com"; d.text(((W-d.textlength(s,font=f))/2,1200),s,font=f,fill=YEL)
    return im
UI={"ui_checkin":("checkin",1.25,0.9),"ui_order":("order",1.35,0.2),"ui_kitchen":("kitchen",1.1,0.3)}
def scene_img(i,t):
    name,a,b,lines,label=SC[i]; lt=t-a
    if name in UI: fn,spd,off=UI[name]; im=getattr(ui_anim,fn)(off+lt*spd)
    else: im=globals()[name](t,lt)
    z=1.0+0.06*easeio(lt/max(b-a,0.1))+0.03*math.exp(-lt*6)   # punch-in at the cut, then slow push
    cw,ch=W/z,H/z; ox=(W-cw)/2+8*math.sin(t*0.9); oy=(H-ch)*0.35
    return im.crop((int(ox),int(oy),int(ox+cw),int(oy+ch))).resize((W,H),Image.BICUBIC)
TR=0.22
def frame(t):
    i=max(k for k,s in enumerate(SC) if s[1]<=t)
    im=scene_img(i,t); lt=t-SC[i][1]
    if i>0 and lt<TR:   # whip-slide transition
        p=easeio(lt/TR); prev=scene_img(i-1,SC[i][1]-0.001)
        c=Image.new("RGB",(W,H)); c.paste(prev.filter(ImageFilter.GaussianBlur(6)),(int(-W*p),0)); c.paste(im.filter(ImageFilter.GaussianBlur(6*(1-p))),(int(W*(1-p)),0)); im=c
    im=im.convert("RGBA"); d=ImageDraw.Draw(im)
    label=SC[i][4]
    if label:
        f=dev(48); tw=d.textlength(label,font=f); pp=ease(lt/0.25); y=200-int(40*(1-pp))
        d.rounded_rectangle([60,y,60+tw+96,y+82],40,fill=(255,255,255)); d.ellipse([88,y+31,110,y+53],fill=TERRA); d.text((126,y+8),label,font=f,fill=INK)
    if i==0:   # hook text
        f=dev(78); s1="हर पापा ने ये सुना है!"; tw=d.textlength(s1,font=f); pp=ease(t/0.2)
        d.rounded_rectangle([(W-tw)/2-36,120,(W+tw)/2+36,250],30,fill=(255,206,64)); d.text(((W-tw)/2,128),s1,font=f,fill=INK)
    if SC[i][0]=="payoff" and lt>1.2:
        f=dev(56); s1="अपने होटल वाले दोस्त को भेजो"; tw=d.textlength(s1,font=f); pp=ease((lt-1.2)/0.3); y=180+int(60*(1-pp))
        d.rounded_rectangle([(W-tw)/2-30,y,(W+tw)/2+30,y+96],28,fill=(255,206,64)); d.text(((W-tw)/2,y+10),s1,font=f,fill=INK)
    ln=line_at(t)
    if ln:
        who=L[ln][3]; txt=L[ln][4]; f=dev(56)
        pre=(who+": ") if who else ""
        words=(pre+txt).split(); rows=[]; cur=""
        for w_ in words:
            tt=(cur+" "+w_).strip()
            if d.textlength(tt,font=f)>900 and cur: rows.append(cur); cur=w_
            else: cur=tt
        rows.append(cur); lh=72; bh=len(rows)*lh+40; y0=1330
        bw=max(d.textlength(r,font=f) for r in rows)+70
        d.rounded_rectangle([(W-bw)/2,y0,(W+bw)/2,y0+bh],26,fill=(20,34,28,240))
        for k,r in enumerate(rows):
            x=(W-d.textlength(r,font=f))/2; y=y0+14+k*lh
            if k==0 and pre: d.text((x,y),pre,font=f,fill=YEL); x+=d.textlength(pre,font=f); r=r[len(pre):]
            d.text((x,y),r,font=f,fill=(255,255,255))
    pill=Image.new("RGBA",(LOGO.width+28,LOGO.height+28),(0,0,0,0)); ImageDraw.Draw(pill).rounded_rectangle([0,0,pill.width-1,pill.height-1],22,fill=(0,0,0,90))
    im.alpha_composite(pill,(W-LOGO.width-64,70)); im.alpha_composite(LOGO,(W-LOGO.width-50,84))
    return im.convert("RGB")
# ---------- sound effects
SR=44100
def sfx_ding(): t=np.arange(int(0.9*SR))/SR; return (np.sin(2*np.pi*1760*t)+0.5*np.sin(2*np.pi*2637*t))*np.exp(-t*5)*0.5
def sfx_pop(): t=np.arange(int(0.18*SR))/SR; f=600+900*t/0.18; return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*20)*0.6
def sfx_knock():
    t=np.arange(int(0.12*SR))/SR; k=(np.sin(2*np.pi*180*t)+0.4*np.random.default_rng(1).normal(0,1,len(t)))*np.exp(-t*45)*0.8
    out=np.zeros(int(0.5*SR)); out[:len(k)]+=k; out[int(0.22*SR):int(0.22*SR)+len(k)]+=k; return out
def sfx_whoosh():
    n=int(0.3*SR); s=np.random.default_rng(2).normal(0,1,n); e=np.sin(np.linspace(0,np.pi,n)); s=np.convolve(s,np.ones(30)/30,'same'); return s*e*0.25
def sfx_brake():
    n=int(0.6*SR); t=np.arange(n)/SR; s=np.random.default_rng(3).normal(0,1,n); s=np.convolve(s,np.ones(6)/6,'same'); return (s*0.25+0.15*np.sin(2*np.pi*(900-300*t)*t))*np.exp(-t*3)
if __name__=="__main__":
    out=sys.argv[1]
    if len(sys.argv)>2:
        for ts in sys.argv[2:]: frame(float(ts)).save(f"/tmp/claude-0/v2_{ts}.jpg",quality=88)
        sys.exit()
    tmp="/home/claude/ep_family/frames2"; os.makedirs(tmp,exist_ok=True)
    for i in range(int(TOTAL*FPS)): frame(i/FPS).save(f"{tmp}/f{i:05d}.jpg",quality=92)
    n=int(TOTAL*SR); vo=np.zeros(n); fx=np.zeros(n)
    def put(arr,sig,at):
        i=int(at*SR); j=min(n,i+len(sig)); arr[i:j]+=sig[:j-i]
    import subprocess as sp
    for s in SC:
        for ln,at in s[3]:
            sp.run(["ffmpeg","-v","error","-y","-i",f"vo2/{ln}.wav","-ar",str(SR),"-ac","1","/tmp/claude-0/_v.wav"],check=True)
            v,_=sf.read("/tmp/claude-0/_v.wav"); put(vo,v,at)
    for s in SC[1:]: put(fx,sfx_whoosh(),s[1]-0.12)
    put(fx,sfx_brake(),3.45); put(fx,sfx_ding(),5.85); put(fx,sfx_pop(),8.9+1.9); put(fx,sfx_pop(),11.4+1.9); put(fx,sfx_pop(),14.2+1.75); put(fx,sfx_pop(),16.8+0.35); put(fx,sfx_knock(),19.45)
    m,msr=sf.read("music.wav"); m=m.mean(1) if m.ndim>1 else m; m=m[:n] if len(m)>=n else np.pad(m,(0,n-len(m)))
    env=np.convolve((np.abs(vo)>0.01).astype(float),np.ones(int(0.25*SR))/int(0.25*SR),'same')   # duck music under voices
    music=m*(0.55-0.33*np.clip(env*3,0,1))
    mix=vo/np.abs(vo).max()*0.9+fx*0.5+music*0.6
    sf.write("/home/claude/ep_family/mix2.wav",mix/np.abs(mix).max()*0.95,SR)
    sp.run(["ffmpeg","-v","error","-y","-framerate",str(FPS),"-i",f"{tmp}/f%05d.jpg","-i","/home/claude/ep_family/mix2.wav",
        "-af","loudnorm=I=-14:TP=-1.5:LRA=11","-c:v","libx264","-pix_fmt","yuv420p","-crf","19","-c:a","aac","-b:a","160k","-ar","44100","-shortest",out],check=True)
    print("wrote",out)
