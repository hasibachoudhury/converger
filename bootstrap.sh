sudo apt-get update
sudo apt-get install -y python3
sudo apt-get install -y git
rm -rf converger
git clone $1
cd converger
python3 converge_one_box.py
