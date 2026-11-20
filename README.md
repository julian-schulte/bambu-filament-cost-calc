# Bambu Filament Cost Calculator // V1.0

### Calculate the ACTUAL costs of your print

---

#### Current Implementation:

- Calculate your total printing costs incl. labor and energy costs
- add buffers and profit margins to your liking

#### Roadmap:

- **V1.1**
  - Input Validation & Sanity Checks: Prevent crashes on invalid inputs (e.g., commas instead of dots, text inputs, negative numbers, or zero models per plate) using reusable validation helpers.
- **V2.0**
  - .3mf File Parser: Automatically extract filament usage, print time, and object count directly from sliced Bambu Studio .gcode.3mf files.
- **V2.1**
  - Local Presets & Workflow Automation:** Save default rates (electricity, printer wattage, margins, filament prices) in a local config.json and support drag-and-drop or folder watching for exported slicer files.
- **V3.0**
  - User Interface: Add a lightweight web or desktop GUI on top of the modular calculation engine.

#### Usage:

- Run main.py and enter your data

> **Disclaimer:** 100% hand-crafted, organic, free-range human code. I'm a Python beginner learning the ropes from scratch—no AI copy-pasting involved. So if your Claude agent starts hyperventilating about non-optimal patterns, tell it to take a deep breath. It works, and I actually understand every line of it.

<3 
