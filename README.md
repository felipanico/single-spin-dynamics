# single-spin-dynamics
Simple magnetization for a single spin

# Environment (needs virtualenv)

- Run in terminal: `source .venv/bin/activate`

# install requirements

```
pip install numpy
pip install math
pip install matplotlib
```

# Fix plot graph in wsl2

- Install xLaunch

- Disable "Native opengl"

- Enable "Disable access control"

- Run in terminal: `export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0`

# Running program

- Run in terminal `python magnetization.py`
