echo "Updating"
apt-get update > install.log
apt-get -y install python &>> install.log
apt-get -y install python3 &>> install.log
pip install os &>> install.log
pip install colorama &>> install.log
pip install random &>> install.log
chmod 777 *
echo "Installed"
