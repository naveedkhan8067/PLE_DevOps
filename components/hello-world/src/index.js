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