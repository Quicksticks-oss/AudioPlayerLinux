import soundcard as sc
import soundfile as sf
import os

class AudioPlayer:
    def __init__(self, device:str=None):
        self.device = None
        if device != None:
            self.initialize_sound_device(device)

    def initialize_sound_device(self, device):
        for s in sc.all_speakers():
            if s.name == device:
                self.device = s

    def create_linux_virtual_output_cable(self, name:str='virtual_audio_output'):
        os.system('pactl load-module module-null-sink sink_name=vspeaker sink_properties=device.description='+name)

    def play_data(self, data:bytes, samplerate:int):
        self.device.play(data, samplerate)

    def play_wav(self, path:str):
        data, samplerate = sf.read(path, dtype='float32')  
        self.play_data(data, samplerate)

if __name__ == '__main__':
    player = AudioPlayer()
    player.create_linux_virtual_output_cable('virtual_audio_output_test')
    player.initialize_sound_device('virtual_audio_output_test')
    player.play_wav('test.wav')
