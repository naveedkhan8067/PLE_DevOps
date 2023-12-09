import * as fs from "fs";
import * as path from "path";
import * as chalk from "chalk";

export function Main (subStr: string) {
// command: c-preprocessor Main.ts MainoutputFile.ts
#include "VarientConfig.js"
#if "VARIENT" == "MAC"
console.log("*** Mac platform string value: " + subStr + " ***");
#elif "VARIENT" == "LINUX"
console.log("*** Linux platform string value: " + subStr + " ***");
#else
console.log("*** Windows platform string value: " + subStr + " ***");
#endif
}