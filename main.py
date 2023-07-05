from PIL import Image
import numpy as np

img = Image.open('img.jpg').convert('L')

matrice = np.array(img)

print(matrice[0, 0])
print(len(matrice))
hist = []
k = 0
while k < 256:
    h = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if (k == matrice[i, j]):
                h = h + 1
    hist.insert(k, h)
    k = k + 1



def WBG(hist,matrice):
#Calculate Weight Background
    m1 = (len(matrice) **2)
    Lwb = []
    Lwb.insert(0, 0)
    k = 1

    while k < 256:
        w=0

        for i in range(k):
            w = w + hist[i]
        wb = w / m1
        Lwb.insert(k, wb)

        k = k + 1
    return Lwb
#Calculate Mean Background
    Lmb = []
    Lmb.insert(0, 0)
    k = 1
    mb=0


    while k < 256:
       m2 = 0
       j=0

       for i in range(k):
          m2 = m2 + (i*hist[i])
          j=j+hist[i]
       if j!=0:
          mb = m2 / j

       Lmb.insert(k,mb)

       k = k + 1
#Calculate Variance Background
    Lvb = []
    Lvb.insert(0, 0)
    k = 1
    vb=0
    while k < 256:
       v = 0
       j=0

       for i in range(k):
          v = v + (((i-Lmb[k])**2)*hist[i])
          j=j+hist[i]

       if j!=0:
          vb = v / j

       Lvb.insert(k,vb)

       k = k + 1
def WFG(hist, matrice):
#Calculate Weight Foreground
   m3 = (len(matrice) ** 2)
   Lwf = []
   k = 0

   while k < 256:
      w = 0

      for i in range(k, 255):
         w = w + hist[i]
      wf = w / m3
      Lwf.insert(k, wf)

      k = k + 1
   return Lwf
#Calculate Mean Foreground
   Lmf = []
   k = 0
   mbf=0
   while k < 256:
      mf = 0
      j=0

      for i in range(k, 255):
         mf = mf + (i*hist[i])
         j = j + hist[i]
      if j != 0:
          mbf = mf / j

      Lmf.insert(k,mbf)

      k = k + 1
#Calculate Variance Foreground
   Lvf = []
   k = 0
   vbf=0
   while k < 256:
      v = 0
      j = 0

      for i in range(k,255):
         v = v + (((i-Lmf[k])**2)*hist[i])
         j = j + hist[i]

      if j!=0:
         vbf = v / j

      Lvf.insert(k,vbf)

      k = k + 1

def BINARIZATION(Lwb,Lvb,Lwf,Lvf):
#Calculate Within Class Variance
    LBINARIZATION=[]
    m=0
    for i in range (0,255):

        r = Lwb[i]
        n = Lwf[i]
        g = Lvb[i]
        s = Lvf[i]
        m=(r*g)+(n*s)


        LBINARIZATION.insert(i,m)
    se=min(LBINARIZATION)
    seuil=LBINARIZATION.index(se)
    print("seuil=",seuil)
#Binarization de l'image
    for i in range (len(matrice)):
        for j in range (len(matrice)):
            if ((matrice[i,j]) >= seuil ):
                matrice[i,j]=255
            else:
                matrice[i,j]=0
    print(matrice)
    image=Image.fromarray(matrice)
    image.save("new image.jpg")
    image.show()


BINARIZATION(Lwb=WBG(hist,matrice) ,Lvb=WBG(hist,matrice) ,Lwf=WFG(hist, matrice),Lvf=WFG(hist, matrice))