import os;
import sys;
import json;
import shutil;

def main(): 
  component = os.environ['COMPONENT']
  print("Selected component: " + str(component))

  variant = os.environ['VARIANT_TYPE']
  print("Selected variant: " + str(variant))

  configFile, configPath = getConfigInfo(component, variant)

  print("-> Current working directory: " + str(os.getcwd()))
  componentPath = os.path.join(os.getcwd(), "components", component)
  src = os.path.normpath(os.path.join(os.getcwd(), configPath, configFile))
  dst = os.path.join(componentPath, "VariantConfig.js")

  #verify the existence of variant config file
  if(not os.path.exists(src)):
    print("Config file not found: " + src)
    sys.exit(1)

  #clean destination file if already exist
  if(os.path.exists(dst)):
    os.remove(dst)

  shutil.copyfile(src, dst)
  print("-> Variant config is successfully prepared")

  print("-> Executing C-Preprocessor")
  processPaths = getPathsToProcess(component, componentPath)

  for file in processPaths:
    os.system("c-preprocessor " + str(file) + " " + str(file))

  print("-> Cleanup successfully performed")
  os.remove(dst)

def getPathsToProcess(component, componentPath):
  pathsList = []
  excludesDirs = ["node_modules", "configs", "lib"]
  excludeFiles = ["README.md", "VariantConfig.js"]

  #Get list of paths
  for root, dirs, files in os.walk(componentPath):
    dirs[:] = [d for d in dirs if d not in excludesDirs]
    for fileName in files:
      if fileName not in excludeFiles: pathsList.append( os.path.join( root[len(componentPath):], fileName ))

  #prepare paths in the required format
  for index in range(len(pathsList)):
    if pathsList[index].startswith("\\") or pathsList[index].startswith("/"):
      pathsList[index] = pathsList[index][1:]
    pathsList[index] = os.path.join("components", component, pathsList[index]).replace("\\","/")

  return pathsList
  
def getConfigInfo(component, variant):
  configFile = ""
  configPath = ""
  data = json.load(open("VariantsInfo.json"))

  for component in data[component]:
    if component["variant"] == variant:
      configFile = component["configFile"]
      configPath = component["configPath"]
      break

  if not (configFile) or not (configPath):
      print("Variant information not found in VariantsInfo.json.")
      sys.exit(1)      

  return configFile, configPath

# call main
if __name__=="__main__": 
  main() 
