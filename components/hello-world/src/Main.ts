#include "../VariantConfig.js"

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
  const msgString = "***" + variant + " platform --> Hello-World ***"
  return msgString;
}

/*
  Display's the message string
*/
export function DisplayMsg (messageString: string): void {
  console.log(messageString);
}
