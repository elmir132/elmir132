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
  <style>
    .run {{ fill:none; stroke:#eafffb; stroke-width:3; stroke-linejoin:round; stroke-linecap:round; stroke-dasharray:55 945; stroke-dashoffset:0; animation:run 4.2s linear infinite; }}
    .run.glow {{ stroke:{TEAL}; stroke-width:9; opacity:.65; }}
    .run.echo {{ opacity:.45; animation-delay:-2.1s; }}
    @keyframes run {{ to {{ stroke-dashoffset:-1000; }} }}
    .cta {{ animation:pulse 2.8s ease-in-out infinite; }}
    .arrow {{ animation:nudge 2.8s ease-in-out infinite; }}
    @keyframes pulse {{ 0%,100% {{ stroke-opacity:.45; }} 50% {{ stroke-opacity:1; }} }}
    @keyframes nudge {{ 0%,100% {{ transform:translate(0,0); }} 50% {{ transform:translate(3px,-3px); }} }}
    @media (prefers-reduced-motion: reduce) {{ .run {{ animation:none; opacity:0; }} .cta, .arrow {{ animation:none; }} }}
  </style>
  <path d="{path}" fill="none" stroke="{TEAL}" stroke-width="5" opacity=".55" filter="url(#glow)"/>
  <path d="{path}" fill="none" stroke="{TEAL}" stroke-width="2.4" stroke-linejoin="round"/>
  <path class="run glow" pathLength="1000" d="{path}" filter="url(#glow)"/>
  <path class="run" pathLength="1000" d="{path}"/>
  <path class="run echo" pathLength="1000" d="{path}"/>
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
  <text x="58" y="252" font-family="{SANS}" font-size="17" fill="{DIM}">to RAG assistants and live voice agents.</text>
  <g transform="translate(58 270)">
    <rect class="cta" width="176" height="32" rx="16" fill="{PANEL}" stroke="{TEAL}" stroke-opacity=".7"/>
    <text x="18" y="21" font-family="{MONO}" font-size="13.5" fill="{TEAL}">elmirabd.me</text>
    <g class="arrow"><path d="M138 21 L150 9 M141 9 H150 V18" fill="none" stroke="{TEAL}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>
  </g>
</svg>
'''
    write("banner.svg", svg)


def tiles(name, label, items):
    """A row of stat tiles. items = [(value, caption)]."""
    pad, gap, h = 12, 8, 78
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
        ("ML and AI", ["TensorFlow", "TensorFlow Lite Micro", "PyTorch", "Gemini", "RAG"]),
        ("Backend and data", ["FastAPI", "Flask", "MongoDB Atlas", "PostgreSQL", "SQLite", "vector search"]),
        ("Infra", ["Docker", "systemd", "DigitalOcean"]),
        ("Hardware", ["ESP32-S3", "BLE", "MQTT"]),
    ]
    fs, ph, gap, label_w, row_h, top = 13, 30, 10, 172, 46, 22
    width, parts = 1000, []
    for i, (name, items) in enumerate(rows):
        y = top + i * row_h
        dot = TEAL if i % 2 == 0 else AMBER
        parts.append(f'<rect x="22" y="{y + 9}" width="4" height="14" rx="2" fill="{dot}"/>'
                     f'<text x="36" y="{y + 20}" font-family="{SANS}" font-size="14" font-weight="600" fill="{MUTED}">{esc(name)}</text>')
        x = label_w
        for it in items:
            w = len(it) * fs * MONO_W + 28
            parts.append(f'<g transform="translate({x:.0f} {y})"><rect width="{w:.0f}" height="{ph}" rx="15" fill="{PANEL}" stroke="{LINE}"/>'
                         f'<text x="14" y="20" font-family="{MONO}" font-size="{fs}" fill="{TEXT}">{esc(it)}</text></g>')
            x += w + gap
    height = top + len(rows) * row_h + 4
    desc = "; ".join(f"{n}: {', '.join(i)}" for n, i in rows)
    write("stack.svg", f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{esc(desc)}">'
          f'<rect width="{width}" height="{height}" rx="14" fill="{BG}" stroke="{LINE}"/>' + "".join(parts) + "</svg>\n")


# Small icons drawn as vector paths on a 20 x 20 grid, so they stay sharp and need no image files.
GITHUB_MARK = ("M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 "
               "0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 "
               "0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12"
               "-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66"
               "-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 "
               "0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z")


def icon(kind, color):
    """Return SVG for one 20 x 20 icon, drawn in the given colour."""
    stroke = f'fill="none" stroke="{color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
    if kind == "linkedin":
        return (f'<rect width="20" height="20" rx="4" fill="{color}"/>'
                f'<circle cx="5.9" cy="6" r="1.45" fill="{PANEL}"/><rect x="4.7" y="8.5" width="2.4" height="7" fill="{PANEL}"/>'
                f'<path d="M9 8.5h2.3v1c.5-.75 1.35-1.2 2.35-1.2 1.9 0 2.65 1.25 2.65 3.1v4.1h-2.4v-3.6c0-.9-.3-1.5-1.1-1.5'
                f'-.9 0-1.4.6-1.4 1.6v3.5H9z" fill="{PANEL}"/>')
    if kind == "github":
        return f'<path transform="scale(1.25)" fill="{color}" fill-rule="evenodd" d="{GITHUB_MARK}"/>'
    if kind == "site":
        return (f'<circle cx="10" cy="10" r="8.2" {stroke}/><ellipse cx="10" cy="10" rx="3.6" ry="8.2" {stroke}/>'
                f'<path d="M1.8 10h16.4M3.2 5.6h13.6M3.2 14.4h13.6" {stroke}/>')
    if kind == "email":
        return (f'<rect x="1.5" y="3.8" width="17" height="12.4" rx="2.2" {stroke}/>'
                f'<path d="M2.2 5.2 10 11.2l7.8-6" {stroke}/>')
    if kind == "paper":
        return (f'<path d="M5 1.6h7l4 4v12.8H5z" {stroke}/><path d="M12 1.6v4h4" {stroke}/>'
                f'<path d="M7.6 9.6h5.8M7.6 12.4h5.8M7.6 15.2h3.6" {stroke}/>')
    return ""


def link(name, label, sub, accent, kind):
    w = int(max(len(label) * 8.4, len(sub) * 7.2) + 96)
    write(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="56" viewBox="0 0 {w} 56" role="img" aria-label="{esc(label)}: {esc(sub)}">'
          f'<rect x=".5" y=".5" width="{w - 1}" height="55" rx="12" fill="{PANEL}" stroke="{LINE}"/>'
          f'<rect x="0" y="14" width="4" height="28" rx="2" fill="{accent}"/>'
          f'<g transform="translate(20 18)">{icon(kind, accent)}</g>'
          f'<text x="54" y="26" font-family="{SANS}" font-size="15" font-weight="600" fill="{TEXT}">{esc(label)}</text>'
          f'<text x="54" y="44" font-family="{MONO}" font-size="12" fill="{MUTED}">{esc(sub)}</text></svg>\n')


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    banner()
    stack()
    tiles("stat-ble.svg", "99.68 percent accuracy, 260 times smaller, 4.62 KB model",
          [("99.68%", "test accuracy"), ("260×", "smaller model"), ("4.62 KB", "on ESP32-S3")])
    tiles("stat-hermes.svg", "6 model tiers with automatic fallback, 20 tests",
          [("6", "model tiers"), ("auto", "fallback"), ("20", "tests")])
    tiles("stat-advocate.svg", "On 20 scripted lines: 0.90 precision and 1.00 recall",
          [("0.90", "precision"), ("1.00", "recall"), ("20", "scripted lines")])
    tiles("stat-rental.svg", "59 source documents, 500 addresses, 9 cities",
          [("59", "source documents"), ("500", "addresses"), ("9", "cities")])
    tiles("stat-streetscript.svg", "1st place, team of 4, 165 tests",
          [("1st", "place"), ("4", "person team"), ("165", "tests")])
    tiles("stat-chronicle.svg", "MongoDB Atlas Vector Search, 2 bugs found by live testing",
          [("Atlas", "vector search"), ("2", "bugs caught live")])
    tiles("stat-firedrill.svg", "Claude Haiku 4.5 on Bedrock: 8 of 8 double refunds without the guardrail, 0 of 8 with it, 32 runs in total",
          [("8/8", "unsafe, no guard"), ("0/8", "unsafe, guarded"), ("32", "total runs")])
    tiles("stat-scanner.svg", "87 percent detection accuracy across more than 150 test applications",
          [("87%", "detection accuracy"), ("150+", "test apps")])
    link("link-linkedin.svg", "LinkedIn", "in/elmirabd", TEAL, "linkedin")
    link("link-github.svg", "Repositories", "github.com/elmir132", AMBER, "github")
    link("link-site.svg", "Website", "elmirabd.me", AMBER, "site")
    link("link-email.svg", "Email", "ea488@cornell.edu", TEAL, "email")
    link("link-paper.svg", "Paper", "CEUR-WS Vol-4278", AMBER, "paper")
    print("built:", ", ".join(sorted(os.listdir(OUT))))
