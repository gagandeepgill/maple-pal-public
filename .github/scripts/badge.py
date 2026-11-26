"""Draw the README's live badges: badge.py <flagged> <total> <out.svg> for the VirusTotal
result, or badge.py version <tag> <out.svg> for the latest release.
Same glass style as the other badges in docs/badges. No third-party packages."""
import sys

REGULAR = {' ': 3.5, '!': 4.41, '"': 5.06, '#': 9.22, '$': 7.0, '%': 10.45, '&': 8.58, "'": 3.03, '(': 4.3, ')': 4.3, '*': 5.5, '+': 9.22, ',': 3.5, '-': 3.97, '.': 3.5, '/': 3.7, '0': 7.0, '1': 7.0, '2': 7.0, '3': 7.0, '4': 7.0, '5': 7.0, '6': 7.0, '7': 7.0, '8': 7.0, '9': 7.0, ':': 3.7, ';': 3.7, '<': 9.22, '=': 9.22, '>': 9.22, '?': 5.84, '@': 11.0, 'A': 7.53, 'B': 7.55, 'C': 7.69, 'D': 8.47, 'E': 6.95, 'F': 6.33, 'G': 8.53, 'H': 8.27, 'I': 3.25, 'J': 3.25, 'K': 7.22, 'L': 6.12, 'M': 9.48, 'N': 8.23, 'O': 8.66, 'P': 6.64, 'Q': 8.66, 'R': 7.64, 'S': 6.98, 'T': 6.72, 'U': 8.05, 'V': 7.53, 'W': 10.88, 'X': 7.53, 'Y': 6.72, 'Z': 7.53, '[': 4.3, '\\': 3.7, ']': 4.3, '^': 9.22, '_': 5.5, '`': 5.5, 'a': 6.73, 'b': 6.98, 'c': 6.05, 'd': 6.98, 'e': 6.77, 'f': 3.88, 'g': 6.98, 'h': 6.97, 'i': 3.06, 'j': 3.06, 'k': 6.38, 'l': 3.06, 'm': 10.72, 'n': 6.97, 'o': 6.73, 'p': 6.98, 'q': 6.98, 'r': 4.52, 's': 5.73, 't': 4.31, 'u': 6.97, 'v': 6.52, 'w': 9.0, 'x': 6.52, 'y': 6.52, 'z': 5.78, '{': 7.0, '|': 3.7, '}': 7.0, '~': 9.22}
BOLD = {' ': 3.83, '!': 5.02, '"': 5.73, '#': 9.22, '$': 7.66, '%': 11.02, '&': 9.59, "'": 3.38, '(': 5.03, ')': 5.03, '*': 5.75, '+': 9.22, ',': 4.17, '-': 4.56, '.': 4.17, '/': 4.02, '0': 7.66, '1': 7.66, '2': 7.66, '3': 7.66, '4': 7.66, '5': 7.66, '6': 7.66, '7': 7.66, '8': 7.66, '9': 7.66, ':': 4.41, ';': 4.41, '<': 9.22, '=': 9.22, '>': 9.22, '?': 6.38, '@': 11.0, 'A': 8.52, 'B': 8.39, 'C': 8.08, 'D': 9.12, 'E': 7.52, 'F': 7.52, 'G': 9.03, 'H': 9.2, 'I': 4.09, 'J': 4.09, 'K': 8.53, 'L': 7.02, 'M': 10.95, 'N': 9.2, 'O': 9.34, 'P': 8.06, 'Q': 9.34, 'R': 8.47, 'S': 7.92, 'T': 7.5, 'U': 8.94, 'V': 8.52, 'W': 12.14, 'X': 8.48, 'Y': 7.97, 'Z': 7.97, '[': 5.03, '\\': 4.02, ']': 5.03, '^': 9.22, '_': 5.5, '`': 5.5, 'a': 7.42, 'b': 7.88, 'c': 6.52, 'd': 7.88, 'e': 7.45, 'f': 4.78, 'g': 7.88, 'h': 7.83, 'i': 3.77, 'j': 3.77, 'k': 7.31, 'l': 3.77, 'm': 11.47, 'n': 7.83, 'o': 7.56, 'p': 7.88, 'q': 7.88, 'r': 5.42, 's': 6.55, 't': 5.27, 'u': 7.83, 'v': 7.17, 'w': 10.16, 'x': 7.09, 'y': 7.17, 'z': 6.41, '{': 7.83, '|': 4.02, '}': 7.83, '~': 9.22}
SHIELD = '<path d="M6.5 0 12 2.2v4C12 9.5 9.7 12 6.5 13 3.3 12 1 9.5 1 6.2v-4zm2.6 4.1L5.8 7.4 4 5.6 3 6.6l2.8 2.8 4.3-4.3z"/>'


def width(text, table):
    return sum(table.get(c, 7.0) for c in text)


TAG = '<path d="M1 1h5.2L12 6.8 7.3 11.5 1.5 5.7zM3.6 3.6a1 1 0 1 0 .01 0z" fill-rule="evenodd"/>'


def badge(flagged, total):
    if total <= 0:
        value, accent = 'scanned every release', '#6fd69a'
    else:
        # Clean reads as engines passed: "61 / 61 clean". Otherwise say how many flagged it.
        value = f'{total} / {total} clean' if flagged == 0 else f'{flagged} of {total} flagged'
        accent = '#6fd69a' if flagged == 0 else '#ffbf5e' if flagged <= 2 else '#ff7a6b'
    return draw('VirusTotal', value, accent, SHIELD)


def draw(label, value, accent, icon):
    h, pad, isz = 28, 11, 13
    lw, vw = width(label, REGULAR), width(value, BOLD)
    x_label = pad + isz + 7
    x_value = x_label + lw + 6
    w = round(x_value + vw + pad + 2)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}: {value}"><title>{label}: {value}</title>
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a3546"/><stop offset="1" stop-color="#18202c"/></linearGradient>
<linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="{(h-1)/2}" fill="url(#g)" stroke="{accent}" stroke-opacity=".55"/>
<rect x="1.5" y="1.5" width="{w-3}" height="{h/2-1}" rx="{(h-3)/2}" fill="url(#s)"/>
<g transform="translate({pad} {(h-isz)/2})" fill="{accent}">{icon}</g>
<g font-family="Verdana,DejaVu Sans,Geneva,sans-serif" font-size="11" dominant-baseline="central">
<text x="{x_label}" y="{h/2+.5}" fill="#b9c4d3" textLength="{lw:.1f}" lengthAdjust="spacingAndGlyphs">{label}</text>
<text x="{x_value}" y="{h/2+.5}" fill="{accent}" font-weight="700" textLength="{vw:.1f}" lengthAdjust="spacingAndGlyphs">{value}</text></g></svg>
'''


if __name__ == '__main__':
    if sys.argv[1] == 'version':
        svg = draw('Latest', sys.argv[2], '#8fc4ff', TAG)
    else:
        svg = badge(int(sys.argv[1]), int(sys.argv[2]))
    with open(sys.argv[3], 'w', encoding='utf-8', newline='\n') as file:
        file.write(svg)
