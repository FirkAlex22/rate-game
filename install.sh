echo "Updating"
apt-get update > install.log
apt-get -y install python &>> install.log
apt-get -y install python3 &>> install.log
pip install os &>> install.log
pip install colorama &>> install.log
pip install random &>> install.log
pip2 install os &>> install.log
pip2 install colorama &>> install.log
pip2 install random &>> install.log
pip3 install os &>> install.log
pip3 install colorama &>> install.log
pip3 install random &>> install.loghmod 777 *
echo "Installed"
