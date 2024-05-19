import os;
import sys;
import shutil

component = os.environ['COMPONENT']
print("Selected component: " + str(component))

variant = os.environ['VARIANT_TYPE']
print("Selected variant: " + str(variant))

configFile = "" 
if (variant == "LINUX"):
  configFile = "Linux_Config.js"
elif (variant == "MAC"):
  configFile = "Mac_Config.js"
else:
  configFile = "Windows_Config.js"

print("-> Current working directory: " + str(os.getcwd()))
src = os.path.join(os.getcwd(), "components", component, "configs", configFile)
dst = os.path.join(os.getcwd(), "components", component, "VariantConfig.js")

#clean destination file if already exist
if(os.path.exists(dst)):
  os.remove(dst)

shutil.copyfile(src, dst)
print("-> Variant config is successfully prepared")

print("-> Executing C-Preprocessor")
os.system("c-preprocessor ./components/" + component + "/package.json ./components/" + component + "/package.json")
os.system("c-preprocessor ./components/" + component + "/src/Main.ts ./components/" + component + "/src/Main.ts")
os.system("c-preprocessor ./components/" + component + "/src/test/Main.test.ts ./components/" + component + "/src/test/Main.test.ts")

print("-> Cleanup successfully performed")
os.remove(dst)
