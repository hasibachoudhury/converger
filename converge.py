import subprocess
import json
puppet = json.loads(open("puppet.json").read())
for server in puppet["servers"]:
  subprocess.run(["ssh", "vagrant@%s" %server, "%s %s" %(open(bootstrap.sh).read().replace("$1", puppet["git"]))])
  #ssh = subprocess.Popen(["ssh", "%s" %server, "python converge_one_box.py"])
