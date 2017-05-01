import subprocess
import json
puppet = json.loads(open("puppet.json").read())
for server in puppet["servers"]:
  subprocess.run(["ssh", "vagrant@%s" %server, 'sudo apt-get update;sudo apt-get install -y python3'])
  #ssh = subprocess.Popen(["ssh", "%s" %server, "python converge_one_box.py"])
