
class Camera:
    def camera_feature(self):
        print("Camera Available")

class MusicPlayer:
    def music_feature(self):
        print("Music Player Available")

class Smartphone(Camera, MusicPlayer):
    def smart_feature(self):
        print("Smartphone Features Enabled")

s = Smartphone()
s.camera_feature()
s.music_feature()
s.smart_feature()

