const fs = require("fs");
const path = require("path");
const chalk=require("chalk");
const rimraf = require("rimraf");
const commander = require("commander");

const program = new commander.Command("Hello World NPM CLI");
program.option("--displayMsg");
program.option("-g, --green", "Display the message in Green.");
program.option("-r, --red", "Display the message in Red.");

program.parse(process.argv);

if (program.green) {
    console.log(chalk.green("Message was configured to show in green color."));
}

if (program.red) {
    console.log(chalk.red("Message was configured to show in red color."));
}

// ** c-preprocess **
// 1st globally install this package
//command: c-preprocessor index.js outputFile.js
//-------------------------------------------------
// #include "config1.js"

// #if variable1 + variable2 == 5 && defined(MY_CONST)
// console("Multi-condition test")
// #elif "MY_CONST2" == "House"
// console.log("Equality Check Pass")
// #else
// console.log("Default Statement!")
// #endif

// #ifndef MY_CONST3
// console.log("Var is not defined!")
// #else
// console.log("Var is defined!")
// #endif
//-------------------------------------------------
