// create 20 buttons to display on the page
// They shoud be made inside the div with id="button-container  "

const buttonContainer = document.getElementById("button-container");
buttonContainer.innerHTML = "";
for (let i = 1; i <= 20; i++) {
    const button = document.createElement("button");
    button.id = i.toString();
    button.innerText = `Button#${i}`;
    button.addEventListener("click", () => {
      alert(`${i}`);
    });
    buttonContainer.appendChild(button);
}

Vanilla JS: Button in Bunch

> button-in-bunch@0.0.0 test

> jest --ci --testResultsProcessor=jest-junit

FAIL test/test.js

  ● Test suite failed to run

    TypeError: Cannot convert undefined or null to object

        at Function.getPrototypeOf (<anonymous>)

       5 | import {fireEvent, getByTestId} from "@testing-library/dom"

       6 | import "@testing-library/jest-dom/extend-expect"

    >  7 | import jsdom, {JSDOM} from "jsdom"

         | ^

       8 | import path from "path"

       9 |

      10 | const BASE = path.resolve(__dirname, "../src")

      at Object.getPrototypeOf (node_modules/jsdom/lib/jsdom/living/generated/utils.js:34:39)

      at Object.require (node_modules/jsdom/lib/api.js:11:18)

      at Object.require (test/test.js:7:1)

Test Suites: 1 failed, 1 total

Tests:       0 total

Snapshots:   0 total

Time:        1.509 s

Ran all test suites.