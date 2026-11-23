"""Flat 2D explainer Reel (owner 23 Nov format): family checks in with Rizstay, orders from the room, order arrives.
All drawing is original vector-style shapes; the product is shown only as animated UI (ui_anim.py)."""
import json, math, os, subprocess, sys
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(__file__)); import ui_anim
W,H,FPS=1080,1920,30
FD="/home/claude/ep_family/fonts/"; FB="/home/claude/sutrixa-instagram-media/brand/"
def dev(s): return ImageFont.truetype(FD+"Mukta-ExtraBold.ttf",s)
def lat(s): return ImageFont.truetype(FB+"fonts/Montserrat-ExtraBold.ttf",s)
CREAM=(247,236,222); PEACH=(244,214,186); SUN=(246,176,120); GREEN=(36,73,59); TERRA=(217,102,59); INK=(40,34,30); WOOD=(150,95,60); WOOD2=(120,74,46)
LOGO=Image.open(FB+"logo.png").convert("RGBA"); LOGO=LOGO.resize((110,int(110*LOGO.height/LOGO.width)))
# ---------------- timeline
D=json.load(open("vo/durs.json")); L={l[0]:l for l in json.load(open("lines.json"))}
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
# speech activity per line (for mouth movement)
ACT={}
for k in D:
    a,sr=sf.read(f"vo/{k}.wav"); a=a if a.ndim==1 else a.mean(1); hop=sr//FPS
    ACT[k]=[float(np.sqrt((a[i:i+hop]**2).mean())) for i in range(0,len(a),hop)]
SC=[  # (scene, start, end, [(line, at)], label)
 ("outside",0.0,8.8,[("n1",0.4),("rohan1",5.0)],None),
 ("desk",8.8,13.0,[("priya",9.2)],None),
 ("ui_checkin",13.0,20.6,[("n2",13.2)],"चेक-इन · गेस्ट कोड"),
 ("room",20.6,24.6,[("ananya",20.9)],None),
 ("ui_order",24.6,28.4,[("n3",24.8)],"रूम सर्विस · फ़ोन से"),
 ("ui_kitchen",28.4,32.6,[("n4",28.6)],"किचन · लाइव ऑर्डर"),
 ("door",32.6,35.8,[("kabir",33.0)],None),
 ("balcony",35.8,40.3,[("rohan2",36.1)],None),
 ("end",40.3,45.0,[("n5",40.6)],None)]
TOTAL=45.0
SPEAKER={"rohan1":"rohan","rohan2":"rohan","priya":"priya","ananya":"ananya","kabir":"kabir"}
def talking(who,t):
    for s in SC:
        for ln,at in s[3]:
            if SPEAKER.get(ln)==who and at<=t<at+D[ln]:
                i=int((t-at)*FPS); v=ACT[ln][min(i,len(ACT[ln])-1)]; return min(1,v*12)
    return 0
def line_at(t):
    for s in SC:
        for ln,at in s[3]:
            if at-0.05<=t<at+D[ln]+0.35: return ln
# ---------------- characters
SKIN={"rohan":(196,138,98),"ananya":(210,156,118),"kabir":(205,150,110),"priya":(214,162,124),"waiter":(186,128,90)}
def person(d,who,x,feet,s=1.0,t=0.0,sit=False,arm_up=0.0,hold=None,flip=False):
    tk=talking(who,t); bob=math.sin(t*2.4+x)*3*s
    kid=who=="kabir"; s2=s*(0.62 if kid else 1.0)
    hh=int(70*s2); body_h=int(200*s2); leg=int(170*s2) if not sit else int(60*s2)
    top=feet-leg-body_h-2*hh+bob
    shirt={"rohan":(52,98,170),"ananya":(225,110,60),"kabir":(244,196,60),"priya":(128,30,48),"waiter":(250,250,250)}[who]
    pants={"rohan":(70,70,82),"ananya":(60,52,60),"kabir":(50,90,170),"priya":(50,40,48),"waiter":(40,40,44)}[who]
    sk=SKIN[who]; cx=x
    # legs
    lw=int(26*s2)
    if sit:
        d.rounded_rectangle([cx-50*s2,feet-leg-10*s2,cx+70*s2,feet-leg+30*s2],12,fill=pants)
        d.rounded_rectangle([cx+40*s2,feet-leg,cx+68*s2,feet],10,fill=pants)
    else:
        for dx in (-22,22): d.rounded_rectangle([cx+dx*s2-lw/2,feet-leg+bob,cx+dx*s2+lw/2,feet],10,fill=pants)
        for dx in (-22,22): d.rounded_rectangle([cx+dx*s2-lw/2-6*s2,feet-12*s2,cx+dx*s2+lw/2+10*s2,feet+4*s2],8,fill=INK)
    # body
    bw=int(118*s2); by0=feet-leg-body_h+bob
    d.rounded_rectangle([cx-bw/2,by0,cx+bw/2,by0+body_h],int(40*s2),fill=shirt)
    if who=="ananya": d.polygon([(cx-bw/2+8,by0+10),(cx-bw/2+34,by0),(cx+bw/2-6,by0+body_h-20),(cx+bw/2-30,by0+body_h-6)],fill=(246,232,206))
    if who=="waiter": d.rounded_rectangle([cx-bw/2+14,by0+30,cx+bw/2-14,by0+body_h],20,fill=(30,30,34))
    if who=="priya": d.polygon([(cx-18*s2,by0),(cx,by0+50*s2),(cx+18*s2,by0)],fill=(250,250,250))
    # arms
    aw=int(24*s2)
    d.rounded_rectangle([cx-bw/2-aw+6,by0+18*s2,cx-bw/2+6,by0+170*s2],12,fill=shirt if who!="waiter" else (250,250,250))
    if arm_up>0:
        ang=arm_up; ex,ey=cx+bw/2+60*s2*ang,by0+30*s2-110*s2*ang
        d.line([cx+bw/2-6,by0+30*s2,ex,ey],fill=shirt if who!="waiter" else (250,250,250),width=aw)
        d.ellipse([ex-16*s2,ey-16*s2,ex+16*s2,ey+16*s2],fill=sk)
    else:
        d.rounded_rectangle([cx+bw/2-6,by0+18*s2,cx+bw/2+aw-6,by0+170*s2],12,fill=shirt if who!="waiter" else (250,250,250))
    for hx in (cx-bw/2-aw/2+6, cx+bw/2+aw/2-6):
        if arm_up>0 and hx>cx: continue
        d.ellipse([hx-15*s2,by0+160*s2,hx+15*s2,by0+190*s2],fill=sk)
    # neck + head
    hy=by0-2*hh+12*s2
    d.rectangle([cx-14*s2,by0-24*s2,cx+14*s2,by0+4],fill=sk)
    d.ellipse([cx-hh,hy,cx+hh,hy+2*hh],fill=sk)
    hair=(30,24,22)
    if who in("rohan","waiter","kabir"):
        d.chord([cx-hh-2,hy-8*s2,cx+hh+2,hy+hh*1.1],180,360,fill=hair)
    if who=="rohan": d.chord([cx-hh+6,hy+hh*0.9,cx+hh-6,hy+2*hh+10*s2],0,180,fill=(60,44,36))
    if who=="ananya":
        d.rounded_rectangle([cx-hh-10*s2,hy-6*s2,cx+hh+10*s2,hy+2*hh+60*s2],int(60*s2),fill=hair)
        d.ellipse([cx-hh,hy+8*s2,cx+hh,hy+2*hh],fill=sk); d.chord([cx-hh,hy-4*s2,cx+hh,hy+hh*0.9],180,360,fill=hair)
    if who=="priya":
        d.ellipse([cx-28*s2,hy-36*s2,cx+28*s2,hy+16*s2],fill=hair); d.chord([cx-hh-2,hy-4*s2,cx+hh+2,hy+hh],180,360,fill=hair)
    # face
    ey=hy+hh*1.05
    for ex in (-22,22): d.ellipse([cx+ex*s2-6*s2,ey-7*s2,cx+ex*s2+6*s2,ey+7*s2],fill=INK)
    my=hy+hh*1.45; mo=tk*14*s2
    if mo>2: d.ellipse([cx-12*s2,my-3*s2,cx+12*s2,my+mo],fill=(120,40,40))
    else: d.arc([cx-16*s2,my-12*s2,cx+16*s2,my+8*s2],20,160,fill=INK,width=max(3,int(4*s2)))
    if hold=="phone": d.rounded_rectangle([cx+bw/2-4,by0+120*s2,cx+bw/2+40*s2,by0+190*s2],8,fill=INK)
    if hold=="cup":
        d.rounded_rectangle([cx+bw/2-6,by0+130*s2,cx+bw/2+34*s2,by0+175*s2],8,fill=(250,250,250))
        for k in range(3): d.arc([cx+bw/2+k*10*s2,by0+80*s2-k*4,cx+bw/2+(k*10+20)*s2,by0+120*s2-k*4],200,340,fill=(255,255,255),width=3)
    if hold=="tray":
        tx0,ty=cx+bw/2-20,by0+110*s2
        d.rounded_rectangle([tx0,ty,tx0+150*s2,ty+16*s2],8,fill=(190,190,196))
        d.rounded_rectangle([tx0+18*s2,ty-60*s2,tx0+50*s2,ty],6,fill=(255,255,255)); d.rectangle([tx0+18*s2,ty-60*s2,tx0+50*s2,ty-50*s2],fill=(230,230,236))
        for k in (70,110): d.rounded_rectangle([tx0+k*s2,ty-34*s2,tx0+(k+30)*s2,ty],6,fill=(200,120,70))
# ---------------- scenes
def sky(d): 
    for y in range(0,1250,10):
        p=y/1250; c=tuple(int(a+(b-a)*p) for a,b in zip((248,200,160),(250,232,212))); d.rectangle([0,y,W,y+10],fill=c)
def tree(d,x,y,r): d.rectangle([x-10,y,x+10,y+220],fill=(110,74,50)); d.ellipse([x-r,y-r,x+r,y+r],fill=(92,150,110))
def outside(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); sky(d)
    d.ellipse([720,200,940,420],fill=SUN)
    d.rectangle([150,520,930,1150],fill=(246,236,220)); d.rectangle([150,520,930,560],fill=(236,222,200))
    d.rounded_rectangle([250,440,830,530],14,fill=GREEN); f=lat(46); s="ARANYA RETREAT"; d.text(((W-d.textlength(s,font=f))/2,460),s,font=f,fill=(240,222,190))
    for r in range(3):
        for c in range(4): d.rectangle([210+c*180,620+r*170,320+c*180,730+r*170],fill=(196,222,228))
    d.rounded_rectangle([470,1010,610,1150],20,fill=WOOD)
    tree(d,90,900,110); tree(d,1000,880,120)
    d.rectangle([0,1150,W,1290],fill=(222,196,170)); 
    for x in range(0,W,120): d.rectangle([x+20,1215,x+80,1225],fill=(250,240,230))
    d.rectangle([0,1290,W,H],fill=GREEN)
    cx=int(-420+540*ease(lt/2.0))
    d.rounded_rectangle([cx,1060,cx+420,1190],40,fill=(214,64,48)); d.rounded_rectangle([cx+80,990,cx+320,1080],40,fill=(214,64,48))
    d.rounded_rectangle([cx+110,1005,cx+200,1070],12,fill=(200,226,236)); d.rounded_rectangle([cx+214,1005,cx+300,1070],12,fill=(200,226,236))
    for wx in (cx+90,cx+330): d.ellipse([wx-42,1150,wx+42,1234],fill=INK); d.ellipse([wx-18,1174,wx+18,1210],fill=(200,200,200))
    if lt>2.0:
        p=ease((lt-2.0)/0.6); off=int(60*(1-p))
        person(d,"ananya",560+off,1240,0.95,t); person(d,"kabir",680+off,1240,1.0,t,arm_up=0.6 if lt>3 else 0)
        person(d,"rohan",820+off,1240,1.0,t)
        d.rounded_rectangle([900+off,1130,980+off,1240],14,fill=(120,80,60))
    return im
def interior(d,floor=1180):
    d.rectangle([0,0,W,floor],fill=(246,232,214)); d.rectangle([0,floor,W,1290],fill=(214,180,148)); d.rectangle([0,1290,W,H],fill=GREEN)
def desk(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); interior(d)
    d.rounded_rectangle([90,240,390,760],150,fill=(200,224,232)); d.rectangle([90,400,390,760],fill=(200,224,232))
    d.line([620,0,620,300],fill=(150,120,90),width=4); d.ellipse([590,300,650,360],fill=(248,196,140))
    person(d,"priya",330,1180,1.05,t,arm_up=0.35 if lt>2.4 else 0)
    d.rounded_rectangle([80,880,620,1190],16,fill=WOOD); d.rectangle([80,880,620,910],fill=WOOD2)
    d.rounded_rectangle([110,812,410,868],12,fill=GREEN); f=lat(34); s="RECEPTION"; d.text((260-d.textlength(s,font=f)/2,820),s,font=f,fill=(240,222,190))
    d.polygon([(450,790),(600,790),(580,880),(470,880)],fill=(60,60,66))
    person(d,"ananya",720,1230,0.95,t); person(d,"kabir",820,1230,1.0,t); person(d,"rohan",950,1230,1.0,t)
    return im
def room(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); interior(d,1150)
    d.rectangle([600,260,960,700],fill=(196,224,232)); d.rectangle([560,230,640,760],fill=TERRA); d.rectangle([920,230,1000,760],fill=TERRA)
    d.rounded_rectangle([60,760,640,1060],30,fill=(250,246,240)); d.rounded_rectangle([60,700,140,1060],20,fill=WOOD)
    d.rounded_rectangle([160,820,320,880],24,fill=(255,255,255)); d.rectangle([60,960,640,1060],fill=(235,214,190))
    person(d,"ananya",380,1080,0.95,t,sit=True,hold="phone")
    jump=abs(math.sin(lt*5))*70
    person(d,"kabir",560,1010-jump,1.0,t,arm_up=0.8)
    return im
def door(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im); interior(d)
    d.rectangle([140,300,620,1180],fill=WOOD2); d.rectangle([170,330,590,1180],fill=(250,238,214))
    p=ease(lt/0.6); d.polygon([(590,330),(590+int(-300*p),360),(590+int(-300*p),1150),(590,1180)],fill=WOOD)
    person(d,"waiter",380,1180,1.0,t,hold="tray")
    person(d,"kabir",780,1220,1.0,t,arm_up=0.9)
    return im
def balcony(t,lt):
    im=Image.new("RGB",(W,H)); d=ImageDraw.Draw(im)
    for y in range(0,1290,10):
        p=y/1290; c=tuple(int(a+(b-a)*p) for a,b in zip((240,150,110),(250,214,170))); d.rectangle([0,y,W,y+10],fill=c)
    d.ellipse([620,520,900,800],fill=(250,200,120))
    for i,x in enumerate(range(-50,W,230)): d.ellipse([x,760-(i%2)*60,x+320,1080],fill=(120,150,120))
    d.rectangle([0,960,W,1290],fill=(214,180,148)); d.rectangle([0,1290,W,H],fill=GREEN)
    d.rectangle([0,930,W,950],fill=(250,246,240))
    for x in range(20,W,70): d.rectangle([x,950,x+14,1160],fill=(250,246,240))
    d.rounded_rectangle([260,1000,560,1060],20,fill=WOOD); d.rounded_rectangle([280,1060,310,1230],8,fill=WOOD2); d.rounded_rectangle([510,1060,540,1230],8,fill=WOOD2)
    person(d,"rohan",400,1230,1.05,t,sit=True,hold="cup")
    return im
def end(t,lt):
    im=Image.new("RGB",(W,H),(10,18,40)); d=ImageDraw.Draw(im)
    g=Image.new("RGB",(W,H),(10,18,40)); gd=ImageDraw.Draw(g); gd.ellipse([140,420,940,1200],fill=(30,70,140)); g=g.filter(ImageFilter.GaussianBlur(160)); im=g
    p=ease(lt/0.8); lg=Image.open(FB+"logo.png").convert("RGBA"); s=int(520*(0.85+0.15*p)); lg=lg.resize((s,int(s*lg.height/lg.width)))
    a=lg.split()[3].point(lambda v:int(v*p)); lg.putalpha(a); im=im.convert("RGBA"); im.alpha_composite(lg,((W-lg.width)//2,560)); im=im.convert("RGB"); d=ImageDraw.Draw(im)
    f=lat(60); s="Rizstay"; d.text(((W-d.textlength(s,font=f))/2,1130),s,font=f,fill=(255,255,255))
    f=lat(34); s="restaurant.rizstay.com"; d.text(((W-d.textlength(s,font=f))/2,1215),s,font=f,fill=(255,206,64))
    return im
UI={"ui_checkin":("checkin",0.0),"ui_order":("order",0.0),"ui_kitchen":("kitchen",0.0)}
def frame(t):
    for name,a,b,lines,label in SC:
        if a<=t<b: break
    lt=t-a
    if name in UI: im=getattr(ui_anim,UI[name][0])(lt+0.2)
    else: im=globals()[name](t,lt)
    # slow push-in on every scene so the picture is always moving (no frozen stretches)
    z=1.0+0.07*(lt/max(b-a,0.1)); cw,ch=W/z,H/z; ox=(W-cw)/2+8*math.sin(t*0.9); oy=(H-ch)*0.35+6*math.cos(t*0.7)
    im=im.crop((int(ox),int(oy),int(ox+cw),int(oy+ch))).resize((W,H),Image.BICUBIC)
    im=im.convert("RGBA"); d=ImageDraw.Draw(im)
    if label:
        f=dev(44); tw=d.textlength(label,font=f); d.rounded_rectangle([60,200,60+tw+90,276],38,fill=(255,255,255)); d.ellipse([86,228,106,248],fill=TERRA); d.text((122,206),label,font=f,fill=INK)
    ln=line_at(t)
    if ln:
        who=L[ln][3]; txt=L[ln][4]; f=dev(50); fn=dev(50)
        pre="" if who=="Narrator" else who+": "
        words=(pre+txt).split(); rows=[]; cur=""
        for w in words:
            tt=(cur+" "+w).strip()
            if d.textlength(tt,font=f)>880 and cur: rows.append(cur); cur=w
            else: cur=tt
        rows.append(cur); lh=66; bh=len(rows)*lh+44; y0=1330
        bw=max(d.textlength(r,font=f) for r in rows)+70
        d.rounded_rectangle([(W-bw)/2,y0,(W+bw)/2,y0+bh],26,fill=(28,46,38,235))
        for i,r in enumerate(rows):
            x=(W-d.textlength(r,font=f))/2; y=y0+18+i*lh
            if i==0 and pre:
                d.text((x,y),pre,font=f,fill=(255,206,64)); x+=d.textlength(pre,font=f); r=r[len(pre):]
            d.text((x,y),r,font=f,fill=(255,255,255))
    # logo every frame (owner rule)
    pill=Image.new("RGBA",(LOGO.width+28,LOGO.height+28),(0,0,0,0)); ImageDraw.Draw(pill).rounded_rectangle([0,0,pill.width-1,pill.height-1],22,fill=(0,0,0,90))
    im.alpha_composite(pill,(W-LOGO.width-64,70)); im.alpha_composite(LOGO,(W-LOGO.width-50,84))
    return im.convert("RGB")
if __name__=="__main__":
    out=sys.argv[1]; tmp="/home/claude/ep_family/frames"; os.makedirs(tmp,exist_ok=True)
    only=sys.argv[2:] 
    if only:
        for ts in only: frame(float(ts)).save(f"/tmp/claude-0/fr_{ts}.jpg",quality=90)
        sys.exit()
    for i in range(int(TOTAL*FPS)): frame(i/FPS).save(f"{tmp}/f{i:05d}.jpg",quality=92)
    # audio: voice lines at offsets + soft pad bed
    sr=24000; mix=np.zeros(int(TOTAL*sr)+sr)
    for name,a,b,lines,label in SC:
        for ln,at in lines:
            v,_=sf.read(f"vo/{ln}.wav"); i=int(at*sr); mix[i:i+len(v)]+=v
    tt=np.arange(len(mix))/sr; bed=sum(np.sin(2*np.pi*f*tt) for f in (196,246.9,293.7))*0.012*(0.6+0.4*np.sin(2*np.pi*tt/8))
    sf.write("/home/claude/ep_family/mix.wav",(mix+bed)[:int(TOTAL*sr)],sr)
    subprocess.run(["ffmpeg","-v","error","-y","-framerate",str(FPS),"-i",f"{tmp}/f%05d.jpg","-i","/home/claude/ep_family/mix.wav",
        "-af","loudnorm=I=-14:TP=-1.5:LRA=11","-c:v","libx264","-pix_fmt","yuv420p","-crf","19","-c:a","aac","-b:a","160k","-ar","44100","-shortest",out],check=True)
    print("wrote",out)
