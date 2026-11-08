# SPDX-FileCopyrightText: © 2026 David Galperin
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

# Must match DEBOUNCE_BITS in src/project.v (2**16 clock cycles).
DEBOUNCE_CYCLES = 1 << 16
SETTLE_CYCLES = 20


async def press_step(dut):
    """Press and release the step button, allowing the debouncer to settle."""
    dut.ui_in.value = 0x01
    await ClockCycles(dut.clk, DEBOUNCE_CYCLES + SETTLE_CYCLES)
    dut.ui_in.value = 0x00
    await ClockCycles(dut.clk, DEBOUNCE_CYCLES + SETTLE_CYCLES)


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 ns (100 MHz in simulation).
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 5)

    assert dut.uo_out.value == 0x00
    assert dut.uio_out.value == 0x00
    assert dut.uio_oe.value == 0x00

    dut._log.info("Test candle sequence")
    for day in range(1, 9):
        await press_step(dut)
        expected = (1 << day) - 1
        dut._log.info(f"Day {day}: uo_out = 0x{int(dut.uo_out.value):02x}")
        assert dut.uo_out.value == expected

    dut._log.info("Ninth press resets all candles")
    await press_step(dut)
    assert dut.uo_out.value == 0x00

    dut._log.info("Tenth press starts a new cycle at candle 1")
    await press_step(dut)
    assert dut.uo_out.value == 0x01

    dut._log.info("Reset clears the candles")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)
    assert dut.uo_out.value == 0x00

    dut._log.info("Short button glitch is ignored")
    dut.ui_in.value = 0x01
    await ClockCycles(dut.clk, 100)
    dut.ui_in.value = 0x00
    await ClockCycles(dut.clk, DEBOUNCE_CYCLES + SETTLE_CYCLES)
    assert dut.uo_out.value == 0x00

    dut._log.info("Done")
