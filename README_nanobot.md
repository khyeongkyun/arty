# Setup
1. RaspberryPI Boot image
2. [nanobot](https://github.com/HKUDS/nanobot) setup
   ```
   arty@canvastalk.local:~ $ git clone https://github.com/HKUDS/nanobot.git
   arty@canvastalk.local:~ $ python3 -m venv venv
   arty@canvastalk.local:~ $ source venv/bin/activate
   ```
   ```
   (venv) arty@canvastalk.local:~ $ cd nanobot
   (venv) arty@canvastalk.local:~ $ pip install -e .
   (venv) arty@canvastalk.local:~ $ nanobot --version
   🐈 nanobot v0.1.4.post3
   ```
3. [ollama](https://ollama.com) setup
   ```
   arty@canvastalk.local:~ $ curl -fsSL https://ollama.com/install.sh | sh
   arty@canvastalk.local:~ $ ollama --version
   ollama version is 0.17.7
   ```
   ```
   arty@canvastalk.local:~ $ ollama run qwen3.5:0.8b
   ...(TODO:)
   ```
