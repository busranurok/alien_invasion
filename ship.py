import pygame
class Ship:
    """Gemiyi yönetecek bir sınıf."""

    def __init__(self, ai_game):
        """Gemiyi başlat ve başlangıç konumunu belirle."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Gemiyi yükle ve dikdörtgenini al.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Her gemiyi ekranın alt merkezinde başlat.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Gemiyi mevcut konumunda çiz."""
        self.screen.blit(self.image, self.rect)
