import pygame
import os

class PygameMediaPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((300, 100))
        pygame.display.set_caption("Python Media Player")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.playing = False

    def load_music(self, music_file):
        pygame.mixer.music.load(music_file)

    def play_music(self):
        pygame.mixer.music.play()
        self.playing = True

    def pause_music(self):
        pygame.mixer.music.pause()
        self.playing = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False

    def display_text(self, text):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.fill((0, 0, 0))
        self.screen.blit(text_surface, (50, 30))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.playing:
                            self.play_music()
                            self.display_text("Playing")
                        else:
                            self.pause_music()
                            self.display_text("Paused")
                    elif event.key == pygame.K_s:
                        self.stop_music()
                        self.display_text("Stopped")

            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    player = PygameMediaPlayer()
    music_file = "monaco.mp3"  # Provide the path to your music file
    if os.path.exists(music_file):
        player.load_music(music_file)
        player.display_text("Press SPACE to Play/Pause, S to Stop")
        player.run()
    else:
        print("Music file not found!")
