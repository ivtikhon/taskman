# Taskman

Taskman is a simple program to manage a list of tasks

### Installation instructions

```
git clone https://github.com/ivtikhon/taskman.git

sudo apt-get -y install python3
sudo apt-get -y install python3-pip
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install tabulate
pip3 install flask-testing
```
### Run unit tests
```
python3 tests.py
```

### Usage
```
cd taskman

python3 startsever.py &
```
#### List tasks
```
python3 taskman.py list
```
#### Add a task
```
python3 taskman.py add "Develop Python program" "4/30/20"
```
##### Delete task
```
python3 taskman.py done 4
```

### Examples
```
$ python3 taskman.py list
  Id  Subject                                                    Due date
----  ---------------------------------------------------------  ----------
   3  Migrate SQL databases to cloud                             06/22/2020
   5  Read about class inheritance model in Python               05/17/2020
   6  Collect input from stakeholders for weekly status meeting  04/08/2020
   7  Take a C# training course                                  03/05/2020


$ python3 taskman.py done 5
$ python3 taskman.py list
  Id  Subject                                                    Due date
----  ---------------------------------------------------------  ----------
   3  Migrate SQL databases to cloud                             06/22/2020
   6  Collect input from stakeholders for weekly status meeting  04/08/2020
   7  Take a C# training course                                  03/05/2020

$ python3 taskman.py add "Update environment definition file" "5/13/2020"
$ python3 taskman.py list
  Id  Subject                                                    Due date
----  ---------------------------------------------------------  ----------
   3  Migrate SQL databases to cloud                             06/22/2020
   6  Collect input from stakeholders for weekly status meeting  04/08/2020
   7  Take a C# training course                                  03/05/2020
   8  Update environment definition file                         05/13/2020

```