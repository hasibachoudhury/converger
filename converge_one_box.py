import subprocess
import json

# Bootstrapping
subprocess.run(["bootstrap.sh"])

config = json.loads("converge_one_box_config.json")

# Install/Uninstall all packages
for package in config["packages"]:
  subprocess.run("sudo apt-get install %s" %package)

# Stop existing services if running
for service in config["services"]:
  subprocess.run(["./%s/stop.sh" %service])

# Start services
for service in config["services"]:
  subprocess.run(["./%s/start.sh" %service])
