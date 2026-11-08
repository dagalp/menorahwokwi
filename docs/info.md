<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This is a Verilog implementation of a Hanukkiah (menorah) day counter.

The step button is `ui[0]`. A two-stage synchronizer and a 16-bit counter
debounce the button, so a valid press is accepted only after the input has been
stable for about 1.3 ms at the 50 MHz design clock.

Each accepted press shifts one more `1` into an 8-bit thermometer-coded register.
The register drives `uo[7:0]`, where `uo[0]` is candle 1 (rightmost) and
`uo[7]` is candle 8 (leftmost). Pressing the button repeatedly therefore lights
the candles from right to left, one per press:

| Press | Lit candles | `uo[7:0]` |
| --- | --- | --- |
| 0 (reset) | none | `0000_0000` |
| 1 | 1 | `0000_0001` |
| 2 | 1-2 | `0000_0011` |
| 3 | 1-3 | `0000_0111` |
| 4 | 1-4 | `0000_1111` |
| 5 | 1-5 | `0001_1111` |
| 6 | 1-6 | `0011_1111` |
| 7 | 1-7 | `0111_1111` |
| 8 | 1-8 | `1111_1111` |
| 9 | none (cycle restarts) | `0000_0000` |

The central shamash candle is always lit. It is not controlled by the chip;
connect it directly to the LED supply through its current-limiting resistor.

`rst_n` clears the candle register and the debounce logic. The bidirectional
pins are unused and are driven low with their output enables disabled.

## How to test

In simulation, run the cocotb test from the `test` directory:

```sh
cd test
make -B
```

The test resets the design, verifies all eight candle states, checks that the
ninth press clears the candles and the tenth press starts a new cycle, checks
`rst_n`, and verifies that a short button glitch is ignored.

On hardware, connect LEDs (with current-limiting resistors) from `uo[0]` through
`uo[7]` to ground, with `uo[0]` on the right and `uo[7]` on the left. Connect the
step button to `ui[0]`, apply a 50 MHz clock to `clk` (the debounce time assumes
this frequency), and press the button once to light candle 1, twice for candles
1-2, and so on. Press a ninth time to clear the candles and start over.

## External hardware

Eight LEDs with current-limiting resistors for candles 1-8, plus the shamash
LED and its resistor tied permanently on. One momentary pushbutton on `ui[0]`.
No other external hardware is required.
