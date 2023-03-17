#Oyuncu çıkış yaptığında oyundan çıkmak için sys modülündeki araçlar kullanılır.
import sys
import pygame

class AlienInvasion:
    """
    Oyunun değerlerini ve davranışını
    yönetmek için genel bir sınıf.
    """

    def __init__(self):
        """
        Oyunu başlat ve
        oyun kaynaklarını oluştur.
        """
        #İlk değer ataması yapılır.
        pygame.init()
        
        #1200 piksel genişlik, 800 piksel yükseklik demeti.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Oyun için ana döngüyü başlat"""
        while True:
            #Klavye ve fare olaylarını gözle.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #En son çizilen ekranı görünür yap.
            pygame.display.flip()
            
if __name__ == "__main__":
    #Bir oyun örneği oluştur ve oyunu çalıştır.
    ai = AlienInvasion()
    ai.run_game()
