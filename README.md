# Taskman

Taskman is a simple program to manage a list of tasks

### Installation instructions


git clone https://github.com/ivtikhon/taskman.git

sudo apt-get -y install python3
sudo apt-get -y install python3-pip
sudo pip3 install flask
sudo pip3 install flask-sqlalchemy
sudo pip3 install tabulate

### Usage

cd taskman

python startsever.py &

#### List tasks

python taskman.py list

#### Add a task

python taskman.py add "Develop Python program" "4/30/20"

##### Delete task

python taskman.py done 4

