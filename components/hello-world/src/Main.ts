#include "../VariantConfig.js"
const chalk=require("chalk");

/*
  It provides the variant type
*/
export function GetVariantType (): string {
  let variantType;
  #if "VARIANT" == "MAC"
  variantType = "Mac"
  #elif "VARIANT" == "LINUX"
  variantType = "Linux"
  #else
  variantType = "Windows"
  #endif
  return variantType;
}

/*
  Creates the message string
*/
export function CreateMsgString (): string {
  const variant = GetVariantType();
  const msgString = "*** " + variant + " platform --> Hello-World Naveed***"
  return msgString;
}

/*
  Display's the colored message string
*/
export function DisplayMsg (messageString: string): void {
  #if "VARIANT" == "MAC"
  console.log(chalk.yellow(messageString));
  #elif "VARIANT" == "LINUX"
  console.log(chalk.red(messageString));
  #else
  console.log(chalk.green(messageString));
  #endif
}
