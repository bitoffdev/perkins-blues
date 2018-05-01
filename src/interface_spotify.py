import spotipy
import spotipy.util as util

import time
import colorsys

from controller_proxy import Controller
from solid_animation import SolidAnimation

def colorpack(color):
    return sum(int(color[i] * 0xff) << (16 - 8*i) for i in range(3))

class SpotifyPlayback:
    __slots__ = "track_id", "track_adjusted_start", "track_name", "beats"

    def set_playback(self, playback_json):
        self.track_id = playback_json["item"]["id"]
        self.track_name = playback_json["item"]["name"]
        # json["timestamp"] is actually when the song started, adjusted if the
        # song was paused
        self.track_adjusted_start = playback_json["timestamp"] * 0.001
        # self.track_adjusted_start = (playback_json["timestamp"] \
        #         - playback_json["progress_ms"]) * 0.001
        # print("Timestamp:", playback_json["timestamp"])
        # print("ADJ:", self.track_adjusted_start)


    def set_analysis(self, analysis_json):
        self.beats = analysis_json["beats"]

    def get_progress(self):
        """
        :return: the number of seconds into the current track
        """
        return time.time() - self.track_adjusted_start

    def get_beat_start(self, index):
        """
        :return: start time of beat in seconds since the epoch
        """
        return self.track_adjusted_start + self.beats[index]["start"]

class SpotifyInterface:
    SCOPE = 'user-read-playback-state user-read-currently-playing'
    def __init__(self):
        self.playback = SpotifyPlayback()
        self.control = Controller("localhost", 8000)
        self.checked_beats = 0 # integer index
        self.current_hue = 0 # float from 0 - 1
    def auth(self,username):
        self.token = util.prompt_for_user_token(username, self.SCOPE,
            client_id='95acf39e73ce4425ac9743edb89ab9be',
            client_secret='71a013e9ee0d481887baa8e8f95bc6a9',
            redirect_uri='http://localhost/callback')
        if not self.token:
            raise "Could not get token for user %s"%username
        self.sp = spotipy.Spotify(auth=self.token)
    def reset(self):
        self.playback = SpotifyPlayback()
        self.update_playback()
        self.update_analysis()
        self.checked_beats = 0 # integer index
        self.current_hue = 0 # float from 0 - 1
    def update_playback(self):
        print("Requesting current track...")
        playback_json = self.sp._get("https://api.spotify.com/v1/me/player/currently-playing")
        self.playback.set_playback(playback_json)
    def update_analysis(self):
        print("Requesting track analysis...")
        analysis_json = self.sp.audio_analysis(self.playback.track_id)
        self.playback.set_analysis(analysis_json)
    def current_beat(self):
        while self.checked_beats >= len(self.playback.beats):
            print("Song ended...")
            self.reset()
        return self.playback.get_beat_start(self.checked_beats)

    def update_lights(self):
        # progress = self.playback.get_progress()
        # print("Progress:", progress)

        # case: beat index is lagging behind track progress by more than a second
        # while progress > self.playback.beats[self.checked_beats]["start"] - 1.0:
        while time.time() > self.current_beat() - 1.0:
            self.checked_beats += 1

        # case: add beat animations to controller
        while time.time() >= self.current_beat() - 5.0:
            start = self.current_beat()
            stop = start + self.playback.beats[self.checked_beats]["duration"] * 0.9
            confidence = self.playback.beats[self.checked_beats]["confidence"]
            self.current_hue = (self.current_hue + confidence * 0.5) % 1
            color = colorpack(colorsys.hsv_to_rgb(self.current_hue, 1.0, confidence))
            self.control.add_animation(SolidAnimation(start, stop, 0.0, 1.0, color))
            self.checked_beats += 1

def main():
    interface = SpotifyInterface()
    print("Authorizing with Spotify...")
    interface.auth("elliospizzaman")
    interface.reset()
    # print("Requesting current track...")
    # interface.update_playback()
    # print("Requesting track analysis...")
    # interface.update_analysis()
    print("Starting loop...")
    while True:
        interface.update_lights()
        time.sleep(3)

main()
