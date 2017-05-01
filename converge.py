import subprocess
import json
puppet = json.loads(open("puppet.json").read())
for server in puppet["servers"]:
  command = open("bootstrap.sh").read().replace("$1", puppet["git"])
  print (command)
  subprocess.run(["ssh", "vagrant@%s" %server, command])
  #ssh = subprocess.Popen(["ssh", "%s" %server, "python converge_one_box.py"])
