# Instagram Login Bot

Bu basit Python uygulaması, Selenium kütüphanesi kullanılarak Instagram hesabınıza otomatik olarak giriş yapar ve takipçilerinizi listeleyerek çıktılarını alır. Bu uygulamayı kullanarak, Instagram hesabınızın takipçilerini görmek için manuel olarak çaba sarf etmek zorunda kalmazsınız. Otomatik olarak takipçilerinizin listesini alabilir ve dilediğiniz şekilde kullanabilirsiniz.

## Gereksinimler

Bu uygulamanın çalışması için aşağıdaki gereksinimleri sağlamalısınız:

- Python 3.x
- Selenium kütüphanesi
- Chrome web tarayıcısı ve ChromeDriver

## Kurulum

1. Projeyi bilgisayarınıza klonlayın veya zip olarak indirin.
2. Gerekli Python kütüphanelerini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırın: 

-  #### pip install selenium

3. ChromeDriver'ı [buradan](https://sites.google.com/a/chromium.org/chromedriver/downloads) indirin ve sisteminize uygun şekilde kurun.
4. `getUser.py` dosyasında Instagram hesabınızın kullanıcı adı ve şifresini girin.

## Kullanım

1. getUser.py dosyasi içerisine giriş bilgilerini giriniz.
2. Terminal veya komut istemcisinde uygulamanın bulunduğu dizine gidin.
3. Python dosyasını çalıştırın:

-  #### python instagram_takipci_alma.py

4. Uygulama Instagram hesabınıza otomatik olarak giriş yapacak ve takipçi listesini alacak.
5. Takipçi listesi terminalde görüntülenecektir.

## Notlar

- Bu uygulamanın doğru çalışabilmesi için Instagram hesabınızın gizlilik ayarlarının "Hesabım" bölümünde "Hesabımı Gizle" seçeneğinin kapalı olduğundan emin olun.
- Bu uygulamayı kullanırken hesabınızın güvenliğini sağlamak için Instagram'un izin verdiği oturum açma sıklığını aşmayın. Aksi takdirde Instagram hesabınız askıya alınabilir veya geçici olarak engellenebilir.
#### Bu uygulama eğitim ve öğrenme amaçları için oluşturulmuştur ve kullanımıyla ilgili herhangi bir sorumluluk kabul edilmez.

----

# Instagram Login Bot

This simple Python application logs into your Instagram account using the Selenium library and retrieves your followers by listing them out. With this application, you won't need to manually make efforts to see your Instagram followers. You can automatically retrieve and utilize the list of your followers as needed.

## Requirements

To run this application, you need to meet the following requirements:

- Python 3.x
- Selenium library
- Chrome web browser and ChromeDriver

## Installation

1. Clone the project to your computer or download it as a zip file.
2. Install the required Python libraries by running the following command in your terminal or command prompt:

-  #### pip install selenium

3. Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and install it according to your system.
4. Enter your Instagram username and password in the `getUser.py` file.

## Usage

1. Enter login information in getUser.py file.
2. Navigate to the directory where the application is located in your terminal or command prompt.
3. Run the Python file:

-  #### python instagram_takipci_alma.py

4. The application will automatically log into your Instagram account and retrieve the list of followers.
5. The follower list will be displayed in the terminal.

## Notes

- Ensure that the privacy settings of your Instagram account under the "Account" section have "Private Account" turned off for this application to function correctly.
- While using this application, do not exceed the login frequency allowed by Instagram to ensure the security of your account. Otherwise, your Instagram account may be suspended or temporarily blocked.
#### This application is created for educational and learning purposes, and no responsibility is accepted for its usage.

