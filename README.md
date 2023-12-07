# pests.py - Python'daki basit zararlılar

## Pests Nedir?
Pests temel olarak iş parçacıklı sunucuları etkileyen bir HTTP Hizmet Reddi saldırısıdır. Bu şekilde çalışır:

1. Çok sayıda HTTP isteği yapmaya başlarız.
2. Bağlantıları açık tutmak için başlıkları periyodik olarak (her ~15 saniyede bir) göndeririz.
3. Sunucu bunu yapmadığı sürece bağlantıyı asla kapatmayız. Sunucu bir bağlantıyı kapatırsa, aynı şeyi yapmaya devam ederek yeni bir bağlantı oluştururuz.

Bu, sunucunun iş parçacığı havuzunu tüketir ve sunucu diğer kişilere yanıt veremez.

## Alıntı

Bu çalışmayı yararlı bulduysanız lütfen şu şekilde alıntı yapın:


```bibtex
  title = "Pests",
  author = "Pomerd",
  journal = "github.com",
  year = "2022",
  url = "https://github.com/Pomerd/pests"
}
```

## Nasıl kurulur ve çalıştırılır?

Git deposunu kopyalayabilir veya **pip** kullanarak kurabilirsiniz. İşte bunu nasıl çalıştıracağınız.

* `git clone https://github.com/Pomerd/pests`
* `cd pests`
* `python3 pests.py example.com`

Pests.py'yi kurmak ve çalıştırmak için gereken tek şey bu.

Pip yerine git kullanarak klonlamak istiyorsanız bunu şu şekilde yapabilirsiniz.

* `git klonu https://github.com/Pomerd/pests`
* 'cd pests'
* `python3 pests.py example.com'

### SOCKS5 proxy desteği

Bununla birlikte, bağlantı için IP adresiniz üzerinden doğrudan bağlantı yerine SOCKS5 proxy kullanmak amacıyla '-x' seçeneğini kullanmayı planlıyorsanız, 'PySocks' kitaplığını (veya ' çorap kütüphanesi) de mevcuttur. [`PySocks`](https://github.com/Anorov/PySocks), GitHub kullanıcısı @Anorov tarafından hazırlanan [`SocksiPy`](http://socksipy.sourceforge.net/) yazılımının bir çatalıdır ve tarafından kolayca kurulabilir. yukarıdaki "pip" komutuna "PySocks"u ekleyerek veya bu şekilde tekrar çalıştırarak:

* `sudo pip3 install PySocks`

Daha sonra SOCKS5 desteğini etkinleştirmek için '-x' seçeneğini ve standart 'dan farklıysa SOCKS5 proxy ana bilgisayarını ve bağlantı noktasını belirtmek için '--proxy-host' ve '--proxy-port' seçeneğini kullanabilirsiniz. 127.0.0.1:8080`.

## Yapılandırma seçenekleri
Zararlıların davranışlarını komut satırıyla değiştirmek mümkündür
argümanlar. Güncel bir yardım belgesi almak için şunu çalıştırın:
'zararlılar -h'.

* -p, --port
* * Web sunucusu bağlantı noktası, genellikle 80
* -s, --sockets
* * Testte kullanılacak soket sayısı
* -v, --verbose
* * Günlüğe kaydetmeyi artırır (terminaldeki çıkış)
* -ua, --randuseragents
* * Her istekte kullanıcı aracılarını rastgele seçer
* -x, --useproxy
* * Bağlantı için SOCKS5 proxy kullanın
* --https
* * İstekler için HTTPS kullanın
* --sleeptime
* * Gönderilen her başlık arasında uyku süresi

## Lisans
Kod MIT Lisansı kapsamında lisanslanmıştır.
