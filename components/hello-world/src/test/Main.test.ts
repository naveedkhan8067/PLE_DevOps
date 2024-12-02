#include "../../VariantConfig.js"

import { expect } from "chai";
import { CreateMsgString, GetVariantType, DisplayMsg } from "../Main";

describe("Hello-World Component Tests", async () => {
  it("verify variant and message string", async () => {
    const variantType = GetVariantType();
    const msgString = CreateMsgString();

    #if "VARIANT" == "MAC"
    expect(variantType).to.equal("Mac");
    expect(msgString).to.equal("*** Mac platform --> Hello-World Naveed***");
    #elif "VARIANT" == "LINUX"
    expect(variantType).to.equal("Linux");
    expect(msgString).to.equal("*** Linux platform --> Hello-World Naveed***");
    #else
    expect(variantType).to.equal("Windows");
    expect(msgString).to.equal("*** Windows platform --> Hello-World Naveed***");
    #endif
    DisplayMsg(msgString);
  });
  });
