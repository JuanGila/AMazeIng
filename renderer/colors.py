from dataclasses import dataclass
from enum import StrEnum


"""
            Palette
                │
                ▼
            Renderer
        /           \
        /            \
        ▼            ▼
ConsoleRenderer  MlxRenderer
    │              │
    ▼              ▼
ANSI/ASCII       pixels
"""

class ColorType(StrEnum):
    """Types of colors used to render the maze."""

    BACKGROUND = "background"
    OUTER = "outer"
    FLOOR = "floor"
    WALL = "wall"
    LOGO = "logo"
    START = "start"
    END = "end"


@dataclass(frozen=True)
class Palette:
    """Color palette used to render a maze."""

    name: str
    background: str
    outer: str
    floor: str
    wall: str
    logo: str
    start: str
    end: str

    def get(self, color_type: ColorType) -> str:
        """Return the hexadecimal color for a given color type."""
        return getattr(self, color_type.value)


# ============================================================
# DARK PALETTES
# ============================================================
# Opcion Oscura 1 -> Una estética muy "42 / hacker / terminal"
"""
/* Background */
#define COLOR_BG       0x0B1020

/* Outer cells / border */
#define COLOR_OUTER    0x151B2E

/* Internal walls */
#define COLOR_WALL     0x00E5FF

/* Maze floor */
#define COLOR_FLOOR    0x111827

/* 42 */
#define COLOR_42       0x7C3AED

/* Start / End */
#define COLOR_START    0x22C55E
#define COLOR_END      0xF59E0B
"""
MIDNIGHT_CYBER = Palette(
    name="Midnight Cyber",
    background="#0B1020",
    outer="#151B2E",
    floor="#111827",
    wall="#00E5FF",
    logo="#7C3AED",
    start="#22C55E",
    end="#F59E0B",
)


"""
Opcion Oscura 2 -> Más minimalista, con verde tipo terminal.

Esta puede quedar muy bien en MiniLibX, especialmente sobre fondo casi negro.
#define COLOR_BG       0x09090B
#define COLOR_OUTER    0x18181B
#define COLOR_WALL     0x22C55E
#define COLOR_FLOOR    0x111113
#define COLOR_42       0xF59E0B
#define COLOR_START    0x06B6D4
#define COLOR_END      0xEF4444

"""
OBSIDIAN_NEON = Palette(
    name="Obsidian Neon",
    background="#09090B",
    outer="#18181B",
    floor="#111113",
    wall="#22C55E",
    logo="#F59E0B",
    start="#06B6D4",
    end="#EF4444",
)


# ============================================================
# LIGHT / VIVID PALETTES
# ============================================================
"""
Opcion Clara/viva 1 -> Una paleta clara, limpia y bastante profesional.

Muy buena opción si quieres que el laberinto sea extremadamente legible.

Fondo       → blanco
Borde       → gris claro
Paredes     → azul
Suelo       → blanco
42          → cyan
Inicio      → verde
Salida      → rojo

#define COLOR_BG       0xF8FAFC
#define COLOR_OUTER    0xE2E8F0
#define COLOR_WALL     0x2563EB
#define COLOR_FLOOR    0xFFFFFF
#define COLOR_42       0x06B6D4
#define COLOR_START    0x16A34A
#define COLOR_END      0xDC2626
"""
ARCTIC_42 = Palette(
    name="Arctic 42",
    background="#F8FAFC",
    outer="#E2E8F0",
    floor="#FFFFFF",
    wall="#2563EB",
    logo="#06B6D4",
    start="#16A34A",
    end="#DC2626",
)

"""
Opcion Clara/viva 2 -> Más colorida y llamativa.

Tiene bastante personalidad sin perder legibilidad.

🟧 paredes
🟨 fondo
🟪 42
🟩 inicio
🟥 salida


#define COLOR_BG       0xFFF7ED
#define COLOR_OUTER    0xFED7AA
#define COLOR_WALL     0xEA580C
#define COLOR_FLOOR    0xFFFBEB
#define COLOR_42       0x7C3AED
#define COLOR_START    0x16A34A
#define COLOR_END      0xDC2626
"""
SOLAR_POP = Palette(
    name="Solar Pop",
    background="#FFF7ED",
    outer="#FED7AA",
    floor="#FFFBEB",
    wall="#EA580C",
    logo="#7C3AED",
    start="#16A34A",
    end="#DC2626",
)


# ============================================================
# CREATIVE PALETTES
# ============================================================
"""
Opcion Intermedia/Creativa 1 -> azul/cyan

Esta sería una de mis favoritas para MiniLibX.
Con fondo oscuro y paredes cyan puede quedar muy espectacular.

#define COLOR_BG       0x071E26
#define COLOR_OUTER    0x0B3C49
#define COLOR_WALL     0x22D3EE
#define COLOR_FLOOR    0x0F172A
#define COLOR_42       0x38BDF8
#define COLOR_START    0x2DD4BF
#define COLOR_END      0xFB7185

"""
OCEAN_42 = Palette(
    name="Ocean 42",
    background="#071E26",
    outer="#0B3C49",
    floor="#0F172A",
    wall="#22D3EE",
    logo="#38BDF8",
    start="#2DD4BF",
    end="#FB7185",
)

"""
Opcion Intermedia/Creativa 2(retro/neón) -> Es una estética muy "Cyberpunk / Synthwave"

Fondo       → violeta muy oscuro
Borde       → púrpura
Paredes     → rosa neón
Suelo       → violeta
42          → púrpura brillante
Inicio      → turquesa
Salida      → naranja


#define COLOR_BG       0x120A1F
#define COLOR_OUTER    0x2A1638
#define COLOR_WALL     0xFF2BD6
#define COLOR_FLOOR    0x1B1030
#define COLOR_42       0x7C3AED
#define COLOR_START    0x00F5D4
#define COLOR_END      0xFF6B35
"""
SYNTHWAVE_42 = Palette(
    name="Synthwave 42",
    background="#120A1F",
    outer="#2A1638",
    floor="#1B1030",
    wall="#FF2BD6",
    logo="#7C3AED",
    start="#00F5D4",
    end="#FF6B35",
)


# ============================================================
# PALETTE REGISTRY
# ============================================================

PALETTES: dict[str, Palette] = {
    "midnight": MIDNIGHT_CYBER,
    "obsidian": OBSIDIAN_NEON,
    "arctic": ARCTIC_42,
    "solar": SOLAR_POP,
    "ocean": OCEAN_42,
    "synthwave": SYNTHWAVE_42,
}


def get_palette(name: str) -> Palette:
    """Return a palette by its identifier."""

    try:
        return PALETTES[name.lower()]
    except KeyError:
        available = ", ".join(PALETTES)
        raise ValueError(
            f"Unknown palette '{name}'. "
            f"Available palettes: {available}"
        )


def list_palettes() -> list[str]:
    """Return the identifiers of all available palettes."""
    return list(PALETTES)