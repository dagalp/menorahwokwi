![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/fpga/badge.svg)

# Menorah Tiny Tapeout Project

- [Read the documentation for project](docs/info.md)

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper
than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## About this design

This project is a Verilog implementation of a Hanukkiah (menorah) day counter.
The central shamash candle is always on, and each press of the step button lights
one more of the eight candles from right to left. Pressing the button after all
eight candles are lit clears them so the cycle can restart.

- `ui[0]`: step button (debounced)
- `uo[0]`-`uo[7]`: candles 1-8, with `uo[0]` rightmost
- `clk`: 50 MHz design clock
- `rst_n`: active-low reset

The shamash is not controlled by the chip; it is tied on externally.

## Verilog project setup

1. Add your Verilog files to the `src` folder.
2. Edit [info.yaml](info.yaml) and update `source_files` and `top_module` if you
   add or rename files.
3. Edit [docs/info.md](docs/info.md) to describe the project.
4. Run the cocotb tests in `test` with `make -B`.

The GitHub action builds the ASIC files using LibreLane.

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)

## What next?

- [Submit your design to the next shuttle](https://app.tinytapeout.com/).
- Share your project on your social network of choice:
  - LinkedIn [#tinytapeout](https://www.linkedin.com/search/results/content/?keywords=%23tinytapeout) [@TinyTapeout](https://www.linkedin.com/company/100708654/)
  - Mastodon [#tinytapeout](https://chaos.social/tags/tinytapeout) [@matthewvenn](https://chaos.social/@matthewvenn)
  - X (formerly Twitter) [#tinytapeout](https://twitter.com/hashtag/tinytapeout) [@tinytapeout](https://twitter.com/tinytapeout)
  - Bluesky [@tinytapeout.com](https://bsky.app/profile/tinytapeout.com)
