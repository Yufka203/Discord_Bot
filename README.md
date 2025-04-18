Kedi Sınıflandırıcı Discord Botu
Bu proje, kullanıcıların yüklediği görsellerdeki kedilerin yavru mu yoksa yaşlı mı olduğunu yapay zeka ile tahmin eden bir Discord botudur. Görsel sınıflandırma için Keras kullanılmıştır.

📦 Gereksinimler
Python 3.8 veya üzeri bir sürüm ile birlikte aşağıdaki Python kütüphaneleri gereklidir:

discord.py

tensorflow

keras

pillow

numpy

Gerekli kütüphaneleri yüklemek için terminalde şu komutu çalıştırabilirsiniz:

bash
Copy
Edit
pip install discord.py tensorflow keras pillow numpy
📁 Proje Yapısı
Projede yer alan dosyalar şunlardır:

bot.py : Discord botunun ana dosyasıdır.

model.py : Yapay zeka modelini çalıştıran sınıflandırma fonksiyonunu içerir.

keras_model.h5 : Eğitilmiş görsel sınıflandırma model dosyasıdır.

labels.txt : Modelin sınıflandırma çıktılarında kullandığı sınıf isimlerini içerir (örneğin: "0 yaşlı", "1 yavru").

🚀 Botu Çalıştırma
Öncelikle bir Discord botu oluşturun ve token’ınızı alın. Ardından bot.py dosyasının en altındaki bot.run("token") satırını kendi token’ınızla değiştirin. Örnek:

python
Copy
Edit
bot.run("senin-token-buraya")
Sonrasında aşağıdaki komutla botu başlatabilirsiniz:

bash
Copy
Edit
python bot.py
💬 Komutlar
$hello
Bot basit bir karşılama mesajı gönderir.

$check
Bu komutla birlikte bir görsel yüklerseniz, bot bu görseldeki kedinin yavru mu yoksa yaşlı mı olduğunu tahmin eder.

Kullanım Örneği:
Kullanıcı:

bash
Copy
Edit
$check
(ve bir kedi fotoğrafı yükler)
Bot:

yaml
Copy
Edit
Tahmin: Yavru
Güven skoru: 94.56%
Bu minik bir yavru kedi gibi görünüyor! 😺
📌 Notlar
Görseller .jpg, .jpeg veya .png formatında olmalıdır.

Görsel otomatik olarak 224x224 boyutuna getirilir ve modele uygun hale getirilir.

labels.txt dosyasındaki her satır bir sınıfı temsil eder (örneğin: "0 yaşlı", "1 yavru").

🔐 Güvenlik Önerisi
Discord bot token’ınızı doğrudan kod içerisine yazmak yerine .env dosyasında saklamanız önerilir. Örnek:

.env dosyasına şunu yazın:

ini
Copy
Edit
DISCORD_TOKEN=senin-token-buraya
Ardından bot.py içine şu satırları ekleyin:

python
Copy
Edit
from dotenv import load_dotenv
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))
Böylece token bilgisi gizli kalır ve kodunuz daha güvenli olur.

🐍 Lisans
Bu proje MIT lisansı ile açık kaynak olarak sunulmuştur. Dilediğiniz gibi kullanabilir, değiştirebilir veya geliştirebilirsiniz.

❤️ Teşekkürler
Bu proje Python, Discord API ve Keras kullanılarak geliştirilmiştir. Kedileri sevenler ve yapay zeka meraklıları için hazırlanmıştır. 😻
