# ZelPy

This is a "work in progress" SNES-style MOBA in [PyGame](https://www.pygame.org/) and [Pykka](https://www.pykka.org/en/latest/).

I implement the actor-based single-threaded model of multiplayer game engine design as described in these books: https://leanpub.com/u/nobugs

# Requirements

Ensure miniupnpc and SDL2 is installed. On Guix the command is:

```
guix install sdl2 sdl2-gfx sdl2-image sdl2-mixer sdl2-net sdl2-ttf miniupnpc
```

# Installation

```
cd server
pip install -r requirements.txt
cd ../client
CC=gcc pip install -r requirements.txt
```

# Running

```
SDL_VIDEODRIVER="dummy" python3 server.py 0.0.0.0 5005 &
cd ../client
python3 client.py username 0.0.0.0 0 kb
```
