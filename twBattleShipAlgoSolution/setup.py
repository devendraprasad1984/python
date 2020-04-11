import subprocess
import os
# runcommand="pip install -r requirements.txt --no-index --find-links file:///tmp/packages"
runcommand="pwd| awk '{print $1}'"
curdir=subprocess.Popen(runcommand,shell=True,stdout=subprocess.PIPE).stdout.read()
print(curdir,curdir.decode(),curdir.splitlines())
pwd = os.getcwd()
# print(pwd)
# curdir=""
# p = subprocess.Popen(runcommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# p.communicate()[0]

# runcommand="alias pip=/home/devendra/deven/software/pypy3.6-v7.0.0-linux64/bin/pip3"
# os.popen(runcommand)
# runcommand="alias python=/home/devendra/deven/software/pypy3.6-v7.0.0-linux64/bin/pypy3"
# os.popen(runcommand)

runcommand="which pip3"
pip3_result=subprocess.Popen(runcommand,shell=True,stdout=subprocess.PIPE).stdout.read()
print("pip3 is located at",pip3_result.decode())

runcommand="cd "+str(pwd)
print("running from dir",runcommand)
os.popen(runcommand)
# subprocess.run(runcommand)
os.popen(runcommand)
# runcommand="/home/devendra/deven/software/pypy3.6-v7.0.0-linux64/bin/pip3 install -U -r requirements.txt"
runcommand="pip install -U -r requirements.txt"
# runcommand=pip3_result+" install -U -r requirements.txt"
# runcommand="pip install -U -r requirements.txt"
print("running",runcommand)
# res=os.popen(runcommand).close()
# res=subprocess.Popen(runcommand,shell=True,stdout=subprocess.PIPE).stdout.read()
# print("final run output",res.splitlines())


