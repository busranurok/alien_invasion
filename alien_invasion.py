#Oyuncu çıkış yaptığında oyundan çıkmak için sys modülündeki araçlar kullanılır.
import sys
import pygame
from settings import Settings
from ship import Ship

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
        
        self.settings = Settings()
        #1200 piksel genişlik, 800 piksel yükseklik demeti.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        
    def run_game(self):
        """Oyun için ana döngüyü başlat"""
        while True:
            self._check_events()
            self._update_screen()
        
    #Python' da, baştaki tek _ (alt tire) yardımcı metodu belirler.
    def _check_events(self):
        """Klavye ve fare olaylarına yanıt ver."""
        #Klavye ve fare olaylarını gözle.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        """Ekrandaki resimleri güncelle ve yeni ekrana dön."""
            #Döngüden her geçişte ekranı yeniden çizdir.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            #En son çizilen ekranı görünür yap.
            pygame.display.flip()
            
if __name__ == "__main__":
    #Bir oyun örneği oluştur ve oyunu çalıştır.
    ai = AlienInvasion()
    ai.run_game()
