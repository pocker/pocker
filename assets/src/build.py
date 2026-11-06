#!/usr/bin/env python3
"""Generate the profile README graphics.

Text is converted to outlines so the SVGs look the same everywhere
(GitHub serves them as <img>, which can't load web fonts).

Usage:
    FONT_DIR=/path/to/ibm-plex python3 assets/src/build.py

FONT_DIR must hold IBM Plex Mono (Regular, Medium, SemiBold) and
IBM Plex Sans Condensed (SemiBold, Bold) as .ttf files, from
https://github.com/google/fonts/tree/main/ofl
"""
import os
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONT_DIR = Path(os.environ.get("FONT_DIR", "fonts"))
OUT = Path(__file__).resolve().parent.parent

THEMES = {
    "light": dict(bg="#F4F1EA", grid="#E4DFD3", ink="#1B1B19", muted="#6E695F",
                  accent="#B9501A", fill="#EADFCF", chip="#1B1B19", chipink="#F4F1EA"),
    "dark": dict(bg="#111210", grid="#1F201D", ink="#E8E4DA", muted="#8E897E",
                 accent="#E27A3E", fill="#2A1E16", chip="#E8E4DA", chipink="#111210"),
}

_fonts = {}


def font(name):
    if name not in _fonts:
        f = TTFont(FONT_DIR / f"{name}.ttf")
        _fonts[name] = (f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm)
    return _fonts[name]


MONO = "IBMPlexMono-Regular"
MONO_MED = "IBMPlexMono-Medium"
MONO_SEMI = "IBMPlexMono-SemiBold"
COND = "IBMPlexSansCondensed-SemiBold"
COND_BOLD = "IBMPlexSansCondensed-Bold"


def text_width(s, fname, size, tracking=0.0):
    f, gs, cmap, upm = font(fname)
    w = sum(f["hmtx"][cmap[ord(c)]][0] for c in s) * size / upm
    return w + tracking * size * max(len(s) - 1, 0)


def text(s, fname, size, x, y, color, anchor="start", tracking=0.0):
    """Return an SVG <path> with the outlines of s, baseline at y."""
    f, gs, cmap, upm = font(fname)
    scale = size / upm
    w = text_width(s, fname, size, tracking)
    if anchor == "middle":
        x -= w / 2
    elif anchor == "end":
        x -= w
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
    cx = x
    for c in s:
        g = cmap[ord(c)]
        gs[g].draw(TransformPen(pen, (scale, 0, 0, -scale, cx, y)))
        cx += f["hmtx"][g][0] * scale + tracking * size
    d = pen.getCommands()
    return f'<path fill="{color}" d="{d}"/>' if d else ""


def grid(w, h, t, step=24):
    dots = []
    for gx in range(step, w, step):
        for gy in range(step, h, step):
            dots.append(f"M{gx} {gy}h0.01")
    return (f'<path d="{"".join(dots)}" stroke="{t["grid"]}" stroke-width="2.2" '
            f'stroke-linecap="round"/>')


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')


# ---------------------------------------------------------------- header

LEFT_PINS = ["JAVA", "KOTLIN", "TYPESCRIPT", "PYTHON", "C/C++"]
RIGHT_PINS = ["SPRING", "REACT", "K8S", "AWS", "ESP32"]


def header(t):
    W, H = 1200, 420
    b = [f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>', grid(W, H, t)]

    # frame + title block rules, like a datasheet page
    b.append(f'<path d="M40 64H1160M40 372H1160" stroke="{t["ink"]}" stroke-width="1.5"/>')
    b.append(text("DATASHEET  DS-POCKER", MONO_MED, 13, 40, 48, t["ink"], tracking=0.08))
    b.append(text("REV 2026.11", MONO, 13, 1160, 48, t["muted"], "end", tracking=0.08))
    b.append(text("FIG. 1  PINOUT, TOP VIEW", MONO, 12, 1160, 398, t["muted"], "end", tracking=0.08))
    b.append(text("GITHUB.COM/POCKER", MONO, 12, 40, 398, t["muted"], tracking=0.08))

    # name block
    b.append(text("David", COND_BOLD, 96, 36, 180, t["ink"], tracking=-0.01))
    b.append(text("Szendrei", COND_BOLD, 96, 36, 268, t["ink"], tracking=-0.01))
    b.append(f'<rect x="40" y="296" width="28" height="4" fill="{t["accent"]}"/>')
    b.append(text("LEAD SOFTWARE ENGINEER", MONO_SEMI, 16, 40, 330, t["ink"], tracking=0.06))
    b.append(text("12+ YEARS  /  HUNGARY", MONO, 14, 40, 354, t["muted"], tracking=0.06))

    # chip
    cx, cy, cw, ch = 760, 106, 210, 228
    pitch = 40
    first = cy + 34
    pin_len = 26
    for i, name in enumerate(LEFT_PINS):
        y = first + i * pitch
        b.append(f'<rect x="{cx - pin_len}" y="{y - 5}" width="{pin_len}" height="10" '
                 f'fill="none" stroke="{t["ink"]}" stroke-width="1.5"/>')
        b.append(f'<path d="M{cx - pin_len - 14} {y}H{cx - pin_len - 4}" stroke="{t["muted"]}" stroke-width="1"/>')
        b.append(text(name, MONO_MED, 14, cx - pin_len - 22, y + 5, t["ink"], "end", tracking=0.04))
    for i, name in enumerate(RIGHT_PINS):
        y = first + i * pitch
        x2 = cx + cw
        b.append(f'<rect x="{x2}" y="{y - 5}" width="{pin_len}" height="10" '
                 f'fill="none" stroke="{t["ink"]}" stroke-width="1.5"/>')
        b.append(f'<path d="M{x2 + pin_len + 4} {y}H{x2 + pin_len + 14}" stroke="{t["muted"]}" stroke-width="1"/>')
        b.append(text(name, MONO_MED, 14, x2 + pin_len + 22, y + 5, t["ink"], tracking=0.04))
    b.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="4" fill="{t["chip"]}"/>')
    # notch + pin-1 dot
    b.append(f'<path d="M{cx + cw / 2 - 16} {cy}a16 16 0 0 0 32 0z" fill="{t["bg"]}"/>')
    b.append(f'<circle cx="{cx + 18}" cy="{cy + 18}" r="4" fill="{t["accent"]}"/>')
    # numbers on top of chip body need to be drawn after body
    nums = []
    for i in range(5):
        y = first + i * pitch
        nums.append(text(str(i + 1), MONO, 11, cx + 12, y + 4, t["chipink"]))
        nums.append(text(str(10 - i), MONO, 11, cx + cw - 12, y + 4, t["chipink"], "end"))
    b.extend(nums)
    b.append(text("DS-1", COND_BOLD, 34, cx + cw / 2, cy + ch / 2 + 2, t["chipink"], "middle", tracking=0.02))
    b.append(text("BACKEND / CLOUD", MONO, 10.5, cx + cw / 2, cy + ch / 2 + 26, t["chipink"], "middle", tracking=0.06))
    b.append(text("CI/CD / FIRMWARE", MONO, 10.5, cx + cw / 2, cy + ch / 2 + 42, t["chipink"], "middle", tracking=0.06))
    b.append(text("HU 2014", MONO, 10.5, cx + cw / 2, cy + ch - 18, t["chipink"], "middle", tracking=0.06))
    return svg(W, H, "".join(b), "David Szendrei, Lead Software Engineer")


# ---------------------------------------------------------------- timing

START, END = 2014.0, 2027.0
NOW = 2026 + 10 / 12

SIGNALS = [
    # label, sub-label, start, end (None = ongoing), caption on the high part
    ("CHECKOUT", "large-scale e-commerce", 2020.0, None, "monolith to service, tech lead"),
    ("GAMES", "real-time multiplayer", 2019.0, 2020.0, "architect"),
    ("SMART_HOME", "alarm + IoT platform", 2017.0, 2019.0, "lead dev"),
    ("EARLIER", "eHealth, research, agri", 2014.0, 2020.0, "eHealth infra, rehab + HR pilots"),
    ("OSS_BLE", "wine / proton", 2026 + 9 / 12, 2026 + 9 / 12, "GE-Proton #817 merged, Oct 2026"),
]


def timing(t):
    W, H = 1200, 450
    left, right = 250, 1150
    top, row_h, amp = 96, 62, 22

    def X(year):
        return left + (year - START) / (END - START) * (right - left)

    b = [f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>', grid(W, H, t)]
    b.append(f'<path d="M40 52H1160" stroke="{t["ink"]}" stroke-width="1.5"/>')
    b.append(text("FIG. 2  TIMING DIAGRAM, 2014 TO NOW", MONO_MED, 13, 40, 36, t["ink"], tracking=0.08))

    # year ticks
    axis_y = top + row_h * len(SIGNALS) + 6
    for yr in range(2014, 2027):
        x = X(yr)
        b.append(f'<path d="M{x:.1f} {top - 18}V{axis_y}" stroke="{t["grid"]}" stroke-width="1" '
                 f'stroke-dasharray="2 4"/>')
        if yr % 2 == 0 or yr == 2026:
            b.append(text(str(yr), MONO, 12, x, axis_y + 22, t["muted"], "middle"))
    nx = X(NOW)
    b.append(f'<path d="M{nx:.1f} {top - 24}V{axis_y}" stroke="{t["accent"]}" stroke-width="1.5"/>')
    b.append(text("NOW", MONO_SEMI, 11, nx, top - 30, t["accent"], "middle", tracking=0.08))

    for i, (name, sub, s, e, cap) in enumerate(SIGNALS):
        base = top + i * row_h + amp + 14
        hi = base - amp
        xs, xe = X(s), X(e if e else NOW)
        b.append(text(name, MONO_SEMI, 14, 40, base - 6, t["ink"], tracking=0.04))
        b.append(text(sub, MONO, 11.5, 40, base + 10, t["muted"]))
        slope = 5
        if s == e:  # single event: draw a narrow pulse
            xe = xs + 8
            slope = 1.5
        fill_d = f"M{xs:.1f} {base}L{xs + slope:.1f} {hi}H{xe - (0 if e is None else slope):.1f}" \
                 f"L{xe:.1f} {base}Z" if e else \
                 f"M{xs:.1f} {base}L{xs + slope:.1f} {hi}H{xe:.1f}V{base}Z"
        b.append(f'<path d="{fill_d}" fill="{t["fill"]}"/>')
        if e:
            d = (f"M{left} {base}H{xs:.1f}L{xs + slope:.1f} {hi}H{xe - slope:.1f}"
                 f"L{xe:.1f} {base}H{right}")
        else:
            d = f"M{left} {base}H{xs:.1f}L{xs + slope:.1f} {hi}H{xe:.1f}"
        b.append(f'<path d="{d}" fill="none" stroke="{t["ink"]}" stroke-width="2" '
                 f'stroke-linejoin="round"/>')
        if e is None:
            b.append(f'<path d="M{xe:.1f} {hi}H{right - 8}" stroke="{t["accent"]}" stroke-width="2" '
                     f'stroke-dasharray="4 4"/>')
            b.append(f'<path d="M{right - 10} {hi - 5}l8 5-8 5" fill="none" stroke="{t["accent"]}" '
                     f'stroke-width="2"/>')
        width = xe - xs
        cw = text_width(cap, MONO, 11.5)
        if cw + 16 < width:
            b.append(text(cap, MONO, 11.5, xs + 12, hi + 15, t["ink"]))
        else:
            b.append(text(cap, MONO_MED, 11.5, xs - 10, hi + 4, t["accent"], "end"))

    b.append(text("HIGH = ACTIVE", MONO, 11, 1160, 36, t["muted"], "end", tracking=0.08))
    return svg(W, H, "".join(b),
               "Career timeline: research and eHealth 2014-2017, smart home 2017-2019, "
               "games framework 2019-2020, checkout platform 2020-now, BLE for Proton merged 2026")


if __name__ == "__main__":
    for name, t in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(header(t))
        (OUT / f"timing-{name}.svg").write_text(timing(t))
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
