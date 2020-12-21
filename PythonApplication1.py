#Hasan Hüseyin Aygar
#Burdaki kodlar OZ-ENGİNEER youtube kanalındaki "Python ile Görüntü İşleme - OpenCV" video serisini takip ederek yazdım.



import cv2 
import numpy as np








#kus=cv2.imread("C:\\Users\\hasan\\Desktop\\bird.jpg")
#resim=cv2.imread("C:\\Users\\hasan\\Desktop\\ggyifsa.png") #Bu satırda 'resim' adlı değişkenin içine tanımlanan dosya dizinindeki resim dosyasını uzantısını belirterek tanımlamış olduk.
#griresim=cv2.imread("ggyifsagri.png")
#resim2=cv2.imread("C:\\Users\\hasan\\Desktop\\ggyifsa.png",0)  #Bu satırda ',0' kısmındaki sıfır parametresı ile 3 kanal renk kullanımını siyah-beyaz kanal aralığı olarak tanımlamış olduk.
#resim2=cv2.imread("C:\\Users\\hasan\\Desktop\\ggyifsa.png",0) 
#cv2.imwrite("ggyifsagri.png",resim2) #Bu satırda imwrite() fonksiyonu sayesinde yeni bir resim dosyası 2 kısımda yazdırmış olduk.İlk kısımda oluşacak yeni dosyanın adı ve uzantısını tanımladık.İkinci kısımda ise 'resim2' adlı değişkendeki resimi attık.Bu resim dosya programımızın bulunduğu ana dosya dizininden bulunabilirsiniz.
#cv2.imshow("first app",kus) #Bu satırda ilk kısımda açılacak panel başlığını tanımlarız.İkinci kısımda ise yazılan değişkenin içindeki resim panel çıktısında gösterir.
#print(kus) #Print fonksiyonu sayesinde değişkendeki resimin piksel olarak toplamını matris olarak çıktısını ekran yazdırır.


benimresim=cv2.imread("C:\\Users\\hasan\\Desktop\\FB_IMG_1577736206361.jpg") #Bu satırda 'benim resim' adlı değişkenin içine bilgisayarımızdaki verilen dosya dizin adresindeki resimi tanımladık.


#kesit=benimresim[200:300,100:200] #Burda ise 'benimresim' adlı değişkenden belirli aralıklarla görüntü aldık.--->Mantığı: yenideğişken=tanımlıdeğişken[y koordinatı aralığı,x kordinatı aralığı]
#benimresim[200:300,200:300]=kesit #Burda ise 'kesit' adlı değişkeni 'benim resim' adlı değişkende tanımlanan koordinat aralığına atadık.
#cv2.imshow("Belirli kisim",kesit)
#cv2.imshow("Kesiti ekledik",benimresim)

#AYNALAMA İŞLEMLERİ

#aynalananResim=cv2.copyMakeBorder(benimresim,100,100,100,100,cv2.BORDER_REFLECT) #Burda ise 'benimresim' adlı değişkende tanımlı olan resmi cv2 modülününde .copyMakeBorder() metodu ile aynaladık.Bu metod içinde bazı parametreler tanımlandı.
#---> .copyMakeBorder(işlenicek resim,üstten alınacak birim,alttan alınacak birim,soldan alınacak birim,sağdan alınacak birim,cv2 modülündeki yapılacak işlem aynalamayı tanımladık.)
#cv2.imshow("Aynalanmıs Hali",aynalananResim) #Burda ise 'aynalananResim' değişkenini imshow() metodu ile ekrana panel aracılığı ile yazdırdık.

#UZATMA İŞLEMİ
#uzatılanResim=cv2.copyMakeBorder(benimresim,50,50,50,50,cv2.BORDER_REPLICATE)#Burda ise 'benimresim' adlı değişkende tanımlı olan resmi cv2 modülününde .copyMakeBorder() metodu ile uzattık.Bu metod içinde bazı parametreler tanımlandı.
#---> .copyMakeBorder(işlenicek resim,üstten alınacak birim,alttan alınacak birim,soldan alınacak birim,sağdan alınacak birim,cv2 modülündeki yapılacak işlem uzatmayı tanımladık.)
#cv2.imshow("Uzatılmıs Hali",uzatılanResim)

#TEKRAR İŞLEMİ
#tekrarResim=cv2.copyMakeBorder(benimresim,50,50,50,50,cv2.BORDER_WRAP)#Burda ise 'benimresim' adlı değişkende tanımlı olan resmi cv2 modülününde .copyMakeBorder() metodu ile tekrarlattık.Bu metod içinde bazı parametreler tanımlandı.
#---> .copyMakeBorder(işlenicek resim,üstten alınacak birim,alttan alınacak birim,soldan alınacak birim,sağdan alınacak birim,cv2 modülündeki yapılacak işlem tekrarlamayı tanımladık.)
#cv2.imshow("Tekrar Hali",tekrarResim)

#ÇERÇEVE YAPMA İŞLEMİ
#cerceveResim=cv2.copyMakeBorder(benimresim,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,150,120))#Burda ise 'benimresim' adlı değişkende tanımlı olan resmi cv2 modülününde .copyMakeBorder() metodu ile çerçevelettik.Bu metod içinde bazı parametreler tanımlandı.
#---> .copyMakeBorder(işlenicek resim,üstten alınacak birim,alttan alınacak birim,soldan alınacak birim,sağdan alınacak birim,cv2 modülündeki yapılacak işlem tekrarlamayı tanımladık,çerceve rengini tanımladık RGB(RED,GREEN,BLUE) mantığı ile.)
#cv2.imshow("Cerceve Hali",cerceveResim)

#RESİMDE BELİRLİ ALANI DİKDÖRTGEN ŞEKLİNDE ALMA
#cv2.rectangle(benimresim,(300,400),(150,450),[0,0,255],3) #Burda ise dikdörtgene almak için '.rectangle()'kullanılır.
#Mantığı: .rectangle(kullanıcak resmin tanımlı değişkeni,dikdörtgenin sol alt köşesi koordinatı,dikdörgenin sağ üst köşesi koordinatı,dikdörtgen renk değeri (bgr(blue,green,red) mantığı ile),kalınlık)
#cv2.imshow("Belirli alanı alma",benimresim) 


#AĞIRLIK TOPLAMA 
#print(resim[100,200]) #Burda ise 'resim' adlı değişkenin verilen piksel adresindeki((y,x) mantığı ile) pikselin BGR(Blue,Green,Red) karşılığını matrix değerini ekrana yazdırır.
#print(benimresim[200,300])  #Burda ise 'benimresim' adlı değişkenin verilen piksel adresindeki((y,x) mantığı ile) pikselin BGR(Blue,Green,Red) karşılığını matris değerini ekrana yazdırır.
#print(resim[100,200]+benimresim[200,300]) #Burda ise matris değerlerinin toplamını ekrana yazdırıyoruz.

#Burda ise aynı boyuttaki iki resimi belirli mantıkla üst üste ekleyip ekrandan çıktısını alıyoruz.
#toplam=cv2.add(resim,griresim) #AYNI BOYUTTAKİ iki resmi pikselleri üst üste gelicek şekilde ekleyip 'toplam' adlı değişkene atadık.
#agirliklitoplam=cv2.addWeighted(resim,0.7,griresim,0.3,0) #AYNI BOYUTTAKİ resimleri birincisini %70 ikincisini %30 oranında alıp üst üste ekleyip 'agirliklitoplam' adlı değişkene atadık.
#cv2.imshow("Toplanmıs Görüntü",agirliklitoplam)


#RESMİ GRİLEŞTİRME
#resimgri=cv2.cvtColor(benimresim,cv2.COLOR_BGR2GRAY)#Burda ise 'benimresim' adlı değişkeni .cvtColor() fonksiyonu sayesine cv2.COLOR_BGR2GRAY ile grileştirdik.
#cv2.imshow("GRILESTIRILMIS HALI",resimgri)

#GÖRÜNTÜ PİRAMİTLERİ
#Burda ise tanımlanan değişkendeki resmin boyutunu (".pyrUp()" metodu kullanarak) iki katına çıkartıp (yada '.pyrDown()' yapıp yarı oranda küçültebilir)  matris olarak birimsel artışını '.shape()' sayesinde gösterdik.
#manzara=cv2.imread("C:\\Users\\hasan\\Desktop\\images.jpg") #Dosya indisindeki resmi "manzara" adlı değişkene tanımladık.
#ikikatresim=cv2.pyrUp(manzara) #Burda ise "ikikatresim" adlı değişkenin içine ".pyrUp()" metodu sayesinde "manzara" adlı değişkeni 2 katına çıkarıp atadık.
#cv2.imshow("manzara",ikikatresim) #Ekrana çıktısını aldık.
#print(manzara.shape) #"manzara" adlı değişkenin matrisler büyüklüğünü yazdırdık.
#print(ikikatresim.shape) #"ikikatresim" adlı değişkenin matrisler büyüklüğünü yazdırdık.

#rsm=np.zeros((300,300,3),dtype="uint8") #Burda ise numpy kütüphanesi ile (300,300,3) büyüklüğü ve kanlı ile bir görsel oluşturduk sayısal olarak 0-255 aralığı değerinden dolayı uint8 yaptık.
#print(rsm) #"rsm" matris olarak çıktısını ekrana yazdırdık.

#Kameradan Canlı Görüntü Alma
 
 #kamera=cv2.VideoCapture(0)#B satırda ise 'kamera' adlı değişkenin içine cv2 modülünde .VideoCapture() adlı fonksiyonun içine 0 1 2 sayılarını yazarak değişkenin içine kameramızı tanımlıyoruz.0-->Bilgisayarınızın kamerası 1-->Usb deki kamera  2-->ise projenizdeki tanımlı video kameranız.
#while True:  #Bu döngüde ise kamera değerini okuyup .waitKey(milisaniye) olarak tanımladığımız zaman diliminden sürekli fotograf çekerek video oluşur.ord("q") yazmamızdaki amaç döngü düzenli olarak çalışırken içine tanımladığımız harf veya sayıyı kod çalışırken başarsak döndüden çıkılıp program kapanır.
    #ret,goruntu=kamera.read()      
    #cv2.imshow("Kameradan goruntu alma",goruntu)
    #if cv2.waitKey(80) & 0xFF==ord("1"):
      #  break
    #kamera.release()#Yukarıdaki kod yapımızda kameramızı tanımlarken burada ise serbest bırakıyoruz.


#Resim daire matin kutusu oluşturma

#resim=np.zeros((300,300,3),dtype="uint8")
#cv2.line(resim,(0,0),(100,100),(0,0,255),3) #Burda ise line() fonksiyonu ile çizgi çizdik.Sırasıyla (değişken,başlangıç noktası,bitiş noktası,renk(bgr),kalınlık )
#cv2.circle(resim,(150,150),15,(255,0,0),2)#Burda ise circle() fonksiyonu ile daire çizdik.Sırasıyla (değişken,başlangıç noktası,çap uzunluğu,renk(bgr),kalınlık )
#cv2.putText(resim,"Hasan",(70,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),5) #Burda ise putText() fonksiyonu ile yazı çizdik.Sırasıyla (değişken,yazı,başlangıç noktası,yazı tipi,size,renk(bgr),kalınlık )
#cv2.imshow("deneme liste",resim)

#Canlı Görüntüye Şekiller Ekleme

#kamera=cv2.VideoCapture(0) #Burda ise bilgisayarımızdaki tanımlı olan kamerayı belirttik.
#while True:                 #Döngüde ise kameramızı tanımlayıp okuduk alt kısımda ise ekran çıktısı olarak görüntüyü aldık
 #  ret,goruntu=kamera.read()
  # cv2.rectangle(goruntu,(100,100),(200,200),(0,0,255),2)
   #cv2.imshow("Hasan",goruntu)    
    
  # if cv2.waitKey(40) & 0xFF==ord('Q'):    #Burda ise q tuşuna basıldı mı basılmadı onu kontrol edip sürekli görüntü almayı sorgulamış olduk.Görüntü akıcılığını ise waitKey() fonksiyonun içine milisaniye cinsinden girdiğiniz değere göre canlı görüntü çeker.
   #     break            
                           
   #kamera.release()  


   

#benimresim2=benimresim[:,:,2]=255 #Bu satırda ise 'benimresim' adlı değişkende bulunan resme matrix scale değerini en sonda 2 olarak yani BGR(Blue,Green,Red) sıralamasına göre (0-255 arası değer girilebilir) resime efek eklemiş olduk. 
#benimresim[430:470,200:310,2]=255 #Bu satırda ise y ekseninden 430-470 arasını işaretledik x kısmında ise 200-310 arasını işaretleyip oluşan geometrik şekle efek uyguladık. 
#cv2.imshow("Panel Baslik",benimresim) #Bu satırda 'benim resim' adlı değişkeni ekrana yazdırıp ve panel başlığınıda ilk kısımda belirledik.
#benimresim[200,180]=1[255,255,255] #Bu satırda ise verilen konumdaki pikseli matrix olarak bgr değerini girip boyamış olduk.
#print(benimresim[(150,80)]) #Burda ise 'benimresim' adlı değişkende sol üst kısmı referans alarak 150 birim aşağıya 80  birim sağa giderek o konumdaki BGR(Blue,Green,Red) değerinin matrix değerini ekrana yazdırdık.


#print("Resmin boyutu:"+str(benimresim.size)) #Burda 'benimresim' adlı değişkenin boyutunu string olarak yazdırdık.
#print("Resmin özellikleri:"+str(benimresim.shape)) #Burda 'benimresim' adlı değişkenin özelliğini string olarak yazdırdık.
#print("Resmin veri türü:"+str(benimresim.dtype)) #Burda 'benimresim' adlı değişkenin veri türünü string olarak yazdırdık.

#Bu uygulama ile for döngüsü ile çizği şeklinde sıralı konumdaki piksellere yeni renk tanımladık.
#for i in range(100):
#   benimresim[70,i]=[255,255,255]


   
#cv2.imshow("Panel Baslik",benimresim)
    




   


































#cv2.waitKey(0) #Herhangi bir tuşa basana kadar çıktıyı ekranda tutar.
cv2.destroyAllWindows() #Paneldeki çarpı tuşuna basınca arka planda opencv çalışmasını durdurmak içindir.

