print("halo semua")

import pygame
pygame.init()

lebar_scene = 500
tinggi_scene = 500
judul = "PING PONG SIMULATOR"
warna_belakang = (0, 255, 4)
GAME_RUN = True
GAME_FINISH = False
gambar_bola = "Ping-Pong_ball.png"
gambar_papan = "Papan.png"

scene = pygame.display.set_mode((le

bar_scene, tinggi_scene))
scene.fill(warna_belakang)
pygame.display.set_caption(judul)
FPS = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
        self.lebar = lebar
        self.tinggi = tinggi
        self.gambar = pygame.transform.scale(pygame.image.load(gambar), (self.lebar, self.tinggi))
        self.kecepatan = kecepatan
        self.rect = self.gambar.get_rect()
        self.rect.x = x
        self.rect.y = y
    def tampil(self):
        scene.blit(self.gambar,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def p_kiri(self):
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_q] and self.rect.y>0: 
            self.rect.y -= self.kecepatan
        elif tombol[pygame.K_a] and self.rect.y<tinggi_scene-self.tinggi: 
            self.rect.y += self.kecepatan
    def p_kanan(self):
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_w] and self.rect.y>0: 
            self.rect.y -= self.kecepatan
        elif tombol[pygame.K_s] and self.rect.y<tinggi_scene-self.tinggi: 
            self.rect.y += self.kecepatan

player_kiri = Player(gambar=gambar_papan, x=10, y=10,
                    lebar=30, tinggi=100, kecepatan=10)
player_kanan = Player(gambar=gambar_papan, x=400, y=10,
                    lebar=30, tinggi=100, kecepatan=10)
bola = GameSprite(gambar=gambar_bola, x=200, y=200,
                 lebar=50, tinggi=50, kecepatan=2)

while GAME_RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_RUN = False

    if GAME_FINISH == False:
        scene.fill(warna_belakang)
        player_kiri.tampil()
        player_kanan.tampil()
        bola.tampil()
        player_kiri.p_kiri()
        player_kanan.p_kanan()

    FPS.tick(60)
    pygame.display.update()