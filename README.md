# ZelPy

This is a "work in progress" SNES-style MOBA in [PyGame](https://www.pygame.org/) and [Pykka](https://www.pykka.org/en/latest/).

I implement the actor-based single-threaded model of multiplayer game engine design as described in these books: https://leanpub.com/u/nobugs

# Installation

```
cd server
pip install -r requirements.txt
cd ../client
pip install -r requirements.txt
```

# Running

```
python3 server.py &
cd ../client
python3 client.py username 0.0.0.0 0
```
