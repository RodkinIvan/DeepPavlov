cd /
apt update
apt install --yes --force-yes git python3-pip python3-venv
git clone https://github.com/studio-ousia/bpr.git
cd /bpr
echo "############################################"
python3 --version
echo "############################################"
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install dist/bpr-0.0.1.tar.gz
python3 -m pip install dff[telegram]
python3 -m pip install -U coverage

