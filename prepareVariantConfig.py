import os;
import sys;
import shutil

def main(): 
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
  componetPath = os.path.join(os.getcwd(), "components", component)
  src = os.path.join(componetPath, "configs", configFile)
  dst = os.path.join(componetPath, "VariantConfig.js")

  #clean destination file if already exist
  if(os.path.exists(dst)):
    os.remove(dst)

  shutil.copyfile(src, dst)
  print("-> Variant config is successfully prepared")

  print("-> Executing C-Preprocessor")
  processPaths = getPathsToProcess(component, componetPath)

  for file in processPaths:
    os.system("c-preprocessor " + str(file) + " " + str(file))

  print("-> Cleanup successfully performed")
  os.remove(dst)

def getPathsToProcess(component, componetPath):
  pathsList = []
  excludes = ["node_modules", "configs", "lib", "VariantConfig.js"]

  #Get list of paths
  for root, dirs, files in os.walk(componetPath):
    dirs[:] = [d for d in dirs if d not in excludes]
    for fileName in files:
      pathsList.append( os.path.join( root[len(componetPath):], fileName ))

  #prepare paths in the required format
  for index in range(len(pathsList)):
    if pathsList[index].startswith("\\"):
      pathsList[index] = pathsList[index][1:]
    pathsList[index] = os.path.join("components", component, pathsList[index]).replace("\\","/")

  return pathsList
    
if __name__=="__main__": 
  main() 
