import * as fs from "fs";
import * as path from "path";
import * as chalk from "chalk";
#include "../../../VariantConfig.js"

export function Main (subStr: string): string {
// command: c-preprocessor Main.ts Main.ts
let moduleType;

#if "VARIANT" == "MAC"
moduleType = "MAC"
console.log("*** Mac platform string value: " + subStr + " ***");
#elif "VARIANT" == "LINUX"
moduleType = "LINUX"
console.log("*** Linux platform string value: " + subStr + " ***");
#else
moduleType = "WINDOWS"
console.log("*** Windows platform string value: " + subStr + " ***");
#endif
return moduleType;
}