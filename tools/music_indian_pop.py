import numpy as np, soundfile as sf
SR=44100; BPM=118; B=60/BPM; DUR=30.0; N=int(SR*DUR); rng=np.random.default_rng(7)
out=np.zeros((N,2))
def add(sig,t,pan=0.0,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig)); 
    if i>=N: return
    s=sig[:j-i]*g; out[i:j,0]+=s*(1-pan)/1; out[i:j,1]+=s*(1+pan)/1
def env(n,a=0.002,d=0.2):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/d)
def kick():
    n=int(0.35*SR); t=np.arange(n)/SR; f=50+90*np.exp(-t*30); ph=2*np.pi*np.cumsum(f)/SR; return np.sin(ph)*env(n,0.001,0.12)
def clap():
    n=int(0.25*SR); s=rng.normal(0,1,n); 
    from numpy.fft import rfft,irfft
    S=rfft(s); fr=np.fft.rfftfreq(n,1/SR); S[(fr<900)|(fr>5000)]=0; s=irfft(S,n)
    return s/np.abs(s).max()*env(n,0.001,0.06)
def hat(d=0.03):
    n=int(0.08*SR); s=rng.normal(0,1,n); s=np.diff(np.concatenate([[0],s])); return s/np.abs(s).max()*env(n,0.0005,d)
def tabla(f=380,d=0.18,bend=0.0):
    n=int(0.4*SR); t=np.arange(n)/SR; ff=f*(1+bend*np.exp(-t*12)); ph=2*np.pi*np.cumsum(ff)/SR
    return (np.sin(ph)+0.3*np.sin(2.01*ph))*env(n,0.001,d)+0.2*rng.normal(0,1,n)*env(n,0.0005,0.01)
def pluck(f,d=0.6,bright=0.5):
    n=int(d*SR); p=int(SR/f); buf=rng.uniform(-1,1,p); y=np.zeros(n)
    for i in range(n):
        y[i]=buf[i%p]; buf[i%p]=bright*buf[i%p]+(1-bright)*0.996*buf[(i+1)%p] if False else 0.5*(buf[i%p]+buf[(i+1)%p])*0.995
    return y*env(n,0.001,d*0.6)
def bass(f,d):
    n=int(d*SR); t=np.arange(n)/SR; s=np.sin(2*np.pi*f*t)+0.35*np.sin(4*np.pi*f*t); return np.tanh(1.5*s)*env(n,0.004,d*0.7)
def flute(f,d,vib=5.5):
    n=int(d*SR); t=np.arange(n)/SR; ff=f*(1+0.006*np.sin(2*np.pi*vib*t)*np.minimum(1,t/0.15)); ph=2*np.pi*np.cumsum(ff)/SR
    a=np.minimum(1,t/0.03)*np.minimum(1,(d-t)/0.06).clip(0,1)
    return (np.sin(ph)+0.15*np.sin(2*ph)+0.04*rng.normal(0,1,n))*a
note=lambda m:440*2**((m-69)/12)
chords=[(48,[60,64,67]),(43,[59,62,67]),(45,[60,64,69]),(41,[60,65,69])]   # C G Am F
PL={}
def pl(m):
    if m not in PL: PL[m]=pluck(note(m),0.5)
    return PL[m]
K,C,Hh=kick(),clap(),hat()
bars=int(DUR/(4*B))+1
hook=[(0,76,0.5),(0.5,79,0.5),(1,81,0.75),(2,79,0.5),(2.5,76,0.5),(3,74,1.0),(4,72,0.5),(4.5,74,0.5),(5,76,0.75),(6,74,0.5),(6.5,72,0.5),(7,67,1.0)]
for bar in range(bars):
    t0=bar*4*B; root,ch=chords[bar%4]
    for bt in range(4):
        tb=t0+bt*B
        if bt in (0,2): add(K,tb,0,0.9)
        if bt==2 and bar%2: add(K,tb+B*0.75,0,0.5)
        if bt in (1,3): add(C,tb,0,0.35)
        for s in range(4): add(hat(0.02 if s%2 else 0.035),tb+s*B/4,0.3,0.12 if s%2 else 0.18)
        add(tabla(420,0.12),tb+B*0.5,-0.3,0.25); add(tabla(110,0.25,0.6),tb+B*0.75,-0.2,0.35 if bt%2 else 0.0)
        add(bass(note(root),B*0.9),tb,0,0.30); 
        for m in ch: add(pl(m),tb+B*0.5,0.4,0.09)
    if bar>=1:
        for off,m,dl in hook:
            if off<4 and bar%2==1 or off>=4 and bar%2==0 and bar>=2:
                o=off%4; add(flute(note(m+(12 if bar>=8 else 0)),dl*B*0.95),t0+o*B,-0.1,0.16)
# gentle fade in/out
t=np.arange(N)/SR; out*=np.minimum(1,t/0.3)[:,None]*np.minimum(1,(DUR-t)/1.0)[:,None]
out/=np.abs(out).max()*1.05
sf.write("music.wav",out,SR); print("ok")
