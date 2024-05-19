import * as fs from "fs";
import * as path from "path";
import * as chalk from "chalk";
#include "../VariantConfig.js"

export function Main (subStr: string): string {
// command: c-preprocessor Main.ts Main.ts
let moduleType;

#if "VARIANT" == "MAC"
moduleType = "MAC"
console.log("*** Mac platform -->" + subStr + " ***");
#elif "VARIANT" == "LINUX"
moduleType = "LINUX"
console.log("*** Linux platform -->" + subStr + " ***");
#else
moduleType = "WINDOWS"
console.log("*** Windows platform --> " + subStr + " ***");
#endif
return moduleType;
}
