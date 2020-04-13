# Kitty hints processor for selecting text

This is a [custom
processor](https://sw.kovidgoyal.net/kitty/kittens/hints.html#completely-customizing-the-matching-and-actions-of-the-kitten)
for the [hints kitten](https://sw.kovidgoyal.net/kitty/kittens/hints.html) in
the [kitty terminal emulator](https://sw.kovidgoyal.net/kitty/) which allows
you to select text.

## Installation

Place the `hints_selection.py` file in the same directory as `kitty.conf`.

Map a key to launch the hints kitten with this processor. E.g. for using
`kitty_mod+d` to select words add this to `kitty.conf`:

```
map kitty_mod+d kitten hints --type word --multiple --customize-processing hints_selection.py
```

## Usage

This is used just like the standard hints kitten. After you have finished
choosing the hints, a selection which covers those hints will be set.
