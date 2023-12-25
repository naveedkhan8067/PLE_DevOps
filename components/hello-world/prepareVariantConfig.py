import os;
import sys;
import shutil

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
dst = os.path.join(os.getcwd(), "src", "VariantConfig.js")

#clean destination file if already exist
if(os.path.exists(dst)):
  os.remove(dst)

shutil.copyfile(configFile, dst)
print("-> Variant config is successfully prepared")

print("-> Executing C-Preprocessor")
os.system("c-preprocessor package.json package.json")
os.system("c-preprocessor ./src/Main.ts ./src/Main.ts")
os.system("c-preprocessor ./src/test/Main.test.ts ./src/test/Main.test.ts")

print("-> Cleanup successfully performed")
os.remove(dst)
