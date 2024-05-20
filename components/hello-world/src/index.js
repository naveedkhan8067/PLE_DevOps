const displayMsg = require("./Main").DisplayMsg;
const msgString = require("./Main").CreateMsgString;

/*
  Main function
*/
function main() {
  const msg = msgString();
  displayMsg(msg);
}

main();

