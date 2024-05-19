"""
The Facade design pattern is a structural pattern that provides a simplified interface to a complex subsystem.
By using a Facade, you can reduce the complexity of a system for its clients and make the subsystem easier to use.

Here's an example of how to implement the Facade pattern in Python:

Example: Home Theater System
Imagine you have a home theater system with various components such as a DVD player, projector, amplifier, and lights.
Each component has its own interface and must be operated in a specific sequence to watch a movie.
The Facade pattern simplifies this process.
"""


class DVDPlayer:
    def on(self):
        print("DVD Player is on.")

    def play(self, movie):
        print(f"Playing movie '{movie}'.")

    def stop(self):
        print("Stopping the movie.")

    def off(self):
        print("DVD Player is off.")


class Projector:
    def on(self):
        print("Projector is on.")

    def wide_screen_mode(self):
        print("Projector in wide screen mode.")

    def off(self):
        print("Projector is off.")


class Amplifier:
    def on(self):
        print("Amplifier is on.")

    def set_volume(self, level):
        print(f"Amplifier volume set to {level}.")

    def off(self):
        print("Amplifier is off.")


class Lights:
    def dim(self, level):
        print(f"Lights dimmed to {level}% brightness.")


class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, amplifier, lights):
        self.dvd_player = dvd_player
        self.projector = projector
        self.amplifier = amplifier
        self.lights = lights

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.lights.dim(10)
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amplifier.on()
        self.amplifier.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting movie theater down...")
        self.dvd_player.stop()
        self.dvd_player.off()
        self.amplifier.off()
        self.projector.off()
        self.lights.dim(100)


if __name__ == "__main__":
    # Create subsystem components
    dvd_player = DVDPlayer()
    projector = Projector()
    amplifier = Amplifier()
    lights = Lights()

    # Create the Facade
    home_theater = HomeTheaterFacade(dvd_player, projector, amplifier, lights)

    # Watch a movie
    home_theater.watch_movie("Inception")
    print("\n")
    # End the movie
    home_theater.end_movie()
