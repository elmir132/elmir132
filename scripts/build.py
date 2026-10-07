"""Generate the SVG artwork used by README.md. Run: python3 scripts/build.py

Pure standard library. Every number shown comes from the project READMEs linked in the profile.
"""
import math
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
BG, PANEL, LINE = "#0d1117", "#161b22", "#30363d"
TEXT, MUTED, DIM = "#e6edf3", "#9fb0c3", "#6b7c90"
TEAL, AMBER = "#2dd4bf", "#f5a524"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
MONO_W = 0.602  # width of one monospace glyph, in em


def write(name, svg):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(svg)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def wave(x0, x1, y, bursts, step=2):
    """A flat line with damped oscillating bursts, like packets on a scope."""
    pts = []
    for x in range(x0, x1 + 1, step):
        v = 0.0
        for c, w, amp, period in bursts:
            v += amp * math.exp(-(((x - c) / w) ** 2)) * math.sin(2 * math.pi * (x - c) / period)
        pts.append(f"{x},{y - v:.1f}")
    return "M" + " L".join(pts)


def banner():
    path = wave(690, 1230, 168, [(790, 30, 46, 22), (960, 38, 64, 24), (1120, 26, 34, 20)])
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="320" viewBox="0 0 1280 320" role="img" aria-label="Elmir Abdullaiev, AI and backend engineer, M.Eng. Computer Science at Cornell Tech. From a 4.62 KB model on a microcontroller to an assistant serving live users.">
  <defs>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="#21262d"/></pattern>
    <linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="{BG}" stop-opacity="1"/><stop offset=".55" stop-color="{BG}" stop-opacity="0"/></linearGradient>
    <filter id="glow" x="-10%" y="-40%" width="120%" height="180%"><feGaussianBlur stdDeviation="4"/></filter>
  </defs>
  <rect width="1280" height="320" rx="18" fill="{BG}"/>
  <rect width="1280" height="320" rx="18" fill="url(#dots)"/>
  <rect width="1280" height="320" rx="18" fill="url(#fade)"/>
  <rect x=".5" y=".5" width="1279" height="319" rx="17.5" fill="none" stroke="{LINE}"/>
  <line x1="690" y1="168" x2="1230" y2="168" stroke="#21262d" stroke-width="1" stroke-dasharray="4 6"/>
  <path d="{path}" fill="none" stroke="{TEAL}" stroke-width="5" opacity=".55" filter="url(#glow)"/>
  <path d="{path}" fill="none" stroke="{TEAL}" stroke-width="2.4" stroke-linejoin="round"/>
  <g font-family="{MONO}" font-size="13" fill="{DIM}">
    <text x="690" y="82">BLE advertising packets</text>
    <text x="690" y="270">ESP32-S3 · 4.62 KB model · inference 0.9 ms</text>
  </g>
  <g transform="translate(1034 62)">
    <rect width="196" height="30" rx="15" fill="{PANEL}" stroke="{AMBER}" stroke-opacity=".6"/>
    <circle cx="16" cy="15" r="4.5" fill="{AMBER}"/>
    <text x="30" y="20" font-family="{MONO}" font-size="13" fill="{AMBER}">classified in 0.9 ms</text>
  </g>
  <text x="56" y="132" font-family="{SANS}" font-size="56" font-weight="700" fill="{TEXT}" letter-spacing="-1">Elmir Abdullaiev</text>
  <text x="58" y="178" font-family="{SANS}" font-size="23" fill="{MUTED}">AI / backend engineer · M.Eng. CS, Cornell Tech</text>
  <text x="58" y="228" font-family="{SANS}" font-size="17" fill="{DIM}">From a 4.62 KB model on a microcontroller</text>
  <text x="58" y="252" font-family="{SANS}" font-size="17" fill="{DIM}">to an assistant serving live users.</text>
  <rect x="58" y="274" width="64" height="4" rx="2" fill="{TEAL}"/>
</svg>
'''
    write("banner.svg", svg)


def tiles(name, label, items):
    """A row of stat tiles. items = [(value, caption)]."""
    pad, gap, h = 16, 10, 78
    widths = [max(len(v) * 15.5, len(c) * 7.6 * 0.95) + 2 * pad for v, c in items]
    total = int(sum(widths) + gap * (len(items) - 1))
    x, parts = 0.0, []
    for (v, c), w in zip(items, widths):
        parts.append(
            f'<g transform="translate({x:.0f} 0)"><rect width="{w:.0f}" height="{h}" rx="10" fill="{PANEL}" stroke="{LINE}"/>'
            f'<text x="{pad}" y="38" font-family="{SANS}" font-size="26" font-weight="700" fill="{TEAL}">{esc(v)}</text>'
            f'<text x="{pad}" y="60" font-family="{MONO}" font-size="12" fill="{MUTED}">{esc(c)}</text></g>')
        x += w + gap
    write(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="{h}" viewBox="0 0 {total} {h}" role="img" aria-label="{esc(label)}">' + "".join(parts) + "</svg>\n")


def stack():
    rows = [
        ("Languages", ["Python", "TypeScript / JavaScript", "C / C++", "SQL"]),
        ("ML", ["TensorFlow", "TensorFlow Lite Micro", "PyTorch"]),
        ("Backend and data", ["FastAPI", "Flask", "MongoDB Atlas", "PostgreSQL", "SQLite", "vector search"]),
        ("Infra", ["Docker", "systemd", "DigitalOcean"]),
        ("Hardware", ["ESP32-S3", "BLE", "MQTT"]),
    ]
    fs, ph, gap, label_w, row_h, top = 13, 30, 10, 150, 46, 22
    width, parts = 1000, []
    for i, (name, items) in enumerate(rows):
        y = top + i * row_h
        parts.append(f'<text x="22" y="{y + 20}" font-family="{SANS}" font-size="14" font-weight="600" fill="{MUTED}">{esc(name)}</text>')
        x = label_w
        for it in items:
            w = len(it) * fs * MONO_W + 28
            parts.append(f'<g transform="translate({x:.0f} {y})"><rect width="{w:.0f}" height="{ph}" rx="15" fill="{PANEL}" stroke="{LINE}"/>'
                         f'<text x="14" y="20" font-family="{MONO}" font-size="{fs}" fill="{TEXT}">{esc(it)}</text></g>')
            x += w + gap
    height = top + len(rows) * row_h
    desc = "; ".join(f"{n}: {', '.join(i)}" for n, i in rows)
    write("stack.svg", f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{esc(desc)}">'
          f'<rect width="{width}" height="{height}" rx="14" fill="{BG}" stroke="{LINE}"/>' + "".join(parts) + "</svg>\n")


def link(name, label, sub, accent):
    w = int(max(len(label) * 8.4, len(sub) * 7.2) + 64)
    write(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="56" viewBox="0 0 {w} 56" role="img" aria-label="{esc(label)}: {esc(sub)}">'
          f'<rect x=".5" y=".5" width="{w - 1}" height="55" rx="12" fill="{PANEL}" stroke="{LINE}"/>'
          f'<rect x="0" y="14" width="4" height="28" rx="2" fill="{accent}"/>'
          f'<text x="22" y="26" font-family="{SANS}" font-size="15" font-weight="600" fill="{TEXT}">{esc(label)}</text>'
          f'<text x="22" y="44" font-family="{MONO}" font-size="12" fill="{MUTED}">{esc(sub)}</text></svg>\n')


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    banner()
    stack()
    tiles("stat-ble.svg", "99.68 percent accuracy, 260 times smaller, 4.62 KB model, 0.9 ms inference",
          [("99.68%", "test accuracy"), ("260×", "smaller model"), ("4.62 KB", "on ESP32-S3"), ("0.9 ms", "inference")])
    tiles("stat-hermes.svg", "6 model tiers with automatic fallback",
          [("6", "model tiers"), ("auto", "fallback")])
    tiles("stat-chronicle.svg", "MongoDB Atlas Vector Search, 2 bugs found by live testing",
          [("Atlas", "vector search"), ("2", "bugs caught live")])
    tiles("stat-scanner.svg", "87 percent detection accuracy across more than 150 test applications",
          [("87%", "detection accuracy"), ("150+", "test apps")])
    link("link-linkedin.svg", "LinkedIn", "in/elmirabd", TEAL)
    link("link-site.svg", "Website", "elmirabd.me", AMBER)
    link("link-email.svg", "Email", "ea488@cornell.edu", TEAL)
    link("link-paper.svg", "Paper", "CEUR-WS Vol-4278", AMBER)
    print("built:", ", ".join(sorted(os.listdir(OUT))))
