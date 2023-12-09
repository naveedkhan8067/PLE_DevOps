import os;
import sys;

varient = os.environ['VARIENT_TYPE']
print("Selected varient: " + str(varient))

configFile = "" 
if (varient == "LINUX"):
  configFile = "Linux_Config.js"
elif (varient == "MAC"):
  configFile = "Mac_Config.js"
else:
  configFile = "Windows_Config.js"

print("-> Current working directory: " + str(os.getcwd()))
dst = os.path.join(os.getcwd(), "src", "VarientConfig.js")

#clean destination file if already exist
if(os.path.exists(dst)):
  os.remove(dst)

os.rename(configFile, dst)
print("-> Varient config is successfully prepared")
