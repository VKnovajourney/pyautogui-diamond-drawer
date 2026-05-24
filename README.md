# PyAutoGUI Diamond Drawer

A Python automation project using PyAutoGUI to draw concentric diamond patterns in MS Paint.

## Files

- `diamondfunctions.py`
  - Shared drawing engine and utility functions

- `basic_diamond.py`
  - Basic monochrome concentric diamond drawing

- `multicolor_diamond.py`
  - Sequential color-cycling version

- `randomized_diamond.py`
  - Randomized color generative-art version

## Features

- Automated mouse movement
- Dynamic cursor positioning
- Color cycling
- Randomized color selection
- Concentric geometric drawing
- PyAutoGUI fail-safe support

## Installation

```bash
pip install pyautogui
```

## Usage

```bash
python randomized_diamond.py
```

## Safety

Move mouse to top-left corner to trigger PyAutoGUI fail-safe.
