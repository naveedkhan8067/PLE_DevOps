import * as fs from "fs";
import * as path from "path";
import { expect } from "chai";
import * as rimraf from "rimraf";
import { Main } from "../Main";
#include "../VariantConfig.js"

describe("Hello-World Component Tests", async () => {
  it("Get required module type", async () => {
    var msgStr = "Hello World";
    const moduleType = Main(msgStr);

    #if "VARIANT" == "MAC"
    expect(moduleType).to.equal("MAC");
    #elif "VARIANT" == "LINUX"
    expect(moduleType).to.equal("LINUX");
    #else
    expect(moduleType).to.equal("WINDOWS");
    #endif
  });
  });