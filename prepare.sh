cd /
sudo apt-get update
sudo apt-get install --yes --force-yes python3.8-dev git python3-pip python3-venv
sudo git clone https://github.com/studio-ousia/bpr.git
cd /bpr
sudo python3.8 -m pip install --upgrade build
sudo python3.8 -m build
sudo python3.8 -m pip install dist/bpr-0.0.1.tar.gz
sudo python3.8 -m pip install dff[telegram]
sudo python3.8 -m pip install -U coverage
