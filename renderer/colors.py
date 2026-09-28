from enum import StrEnum
from dataclasses import dataclass


"""
            Palette
                │
                ▼
            Renderer
        /           \
        /            \
        ▼            ▼
Console-Renderer  MiniLibX-Renderer
    │              │
    ▼              ▼
ANSI/ASCII       pixels
"""

class ColorType(StrEnum):
    """Types of colors used to render the maze."""

    END = "end"
    WALL = "wall"
    SEED = "seed"
    OUTER = "outer"
    FLOOR = "floor"
    START = "start"
    BACKGROUND = "background"


@dataclass(frozen=True)
class MazePalette:
    """Color palette used to render a maze."""

    name: str
    wall: str
    seed: str
    outer: str
    floor: str
    background: str
    end: str
    start: str

    def get(self, color_type: ColorType) -> str:
        """Return the hexadecimal color for a given color type."""
        return getattr(self, color_type.value)


# ============================================================
# DARK MAZE_THEMES
# ============================================================
# Opcion Oscura 1 -> Una estética muy "42 / hacker / terminal"
MIDNIGHT_CYBER_PALETTE = MazePalette(
    name="Midnight Cyber",
    background="#0B1020",
    outer="#151B2E",
    floor="#111827",
    wall="#00E5FF",
    seed="#7C3AED",
    start="#22C55E",
    end="#F59E0B",
)

# Opcion Oscura 2 -> Más minimalista, con verde tipo terminal.
# Esta puede quedar muy bien en MiniLibX, especialmente sobre fondo casi negro.
OBSIDIAN_NEON_PALETTE = MazePalette(
    name="Obsidian Neon",
    background="#09090B",
    outer="#18181B",
    wall="#22C55E",
    floor="#111113",
    seed="#F59E0B",
    start="#06B6D4",
    end="#EF4444",
)


# ============================================================
# LIGHT / VIVID MAZE_THEMES
# ============================================================
# Opcion Clara/viva 1 -> Una paleta clara, limpia y bastante profesional.
# Muy buena opción si quieres que el laberinto sea extremadamente legible.
"""
Fondo       → blanco
Borde       → gris claro
Paredes     → azul
Suelo       → blanco
42          → cyan
Inicio      → verde
Salida      → rojo
"""
ARCTIC_42_PALETTE = MazePalette(
    name="Arctic 42",
    background="#F8FAFC",
    outer="#E2E8F0",
    floor="#FFFFFF",
    wall="#2563EB",
    seed="#06B6D4",
    start="#16A34A",
    end="#DC2626",
)

# Opcion Clara/viva 2 -> Más colorida y llamativa.
# Tiene bastante personalidad sin perder legibilidad.
"""

🟧 paredes
🟨 fondo
🟪 42
🟩 inicio
🟥 salida

"""
SOLAR_POP_PALETTE = MazePalette(
    name="Solar Pop",
    background="#FFF7ED",
    outer="#FED7AA",
    floor="#FFFBEB",
    wall="#EA580C",
    seed="#7C3AED",
    start="#16A34A", end="#DC2626",
)


# ============================================================
# CREATIVE MAZE_THEMES
# ============================================================
# Opcion Intermedia/Creativa 1 -> azul/cyan
# Esta sería una de mis favoritas para MiniLibX.
# Con fondo oscuro y paredes cyan puede quedar muy espectacular.
OCEAN_42_PALETTE = MazePalette(
    name="Ocean 42",
    background="#071E26",
    outer="#0B3C49",
    floor="#0F172A",
    wall="#22D3EE",
    seed="#38BDF8",
    start="#2DD4BF",
    end="#FB7185",
)

# Opcion Intermedia/Creativa 2(retro/neón) -> Es una estética muy "Cyberpunk / Synthwave"
"""
Fondo       → violeta muy oscuro
Borde       → púrpura
Paredes     → rosa neón
Suelo       → violeta
42          → púrpura brillante
Inicio      → turquesa
Salida      → naranja
"""
SYNTHWAVE_42_PALETTE = MazePalette(
    name="Synthwave 42",
    background="#120A1F",
    outer="#2A1638",
    floor="#1B1030",
    wall="#FF2BD6",
    seed="#7C3AED",
    start="#00F5D4",
    end="#FF6B35",
)


MAZE_THEMES: dict[str, MazePalette] = {
    "ocean": OCEAN_42_PALETTE,
    "solar": SOLAR_POP_PALETTE,
    "arctic": ARCTIC_42_PALETTE,
    "obsidian": OBSIDIAN_NEON_PALETTE,
    "synthwave": SYNTHWAVE_42_PALETTE,
    "midnight": MIDNIGHT_CYBER_PALETTE,
}


def get_maze_theme(name: str) -> MazePalette:
    """Return a palette by its identifier."""
    try:
        return MAZE_THEMES[name.lower()]
    except KeyError:
        available = ", ".join(MAZE_THEMES)
        raise ValueError(
            f"Unknown palette '{name}'. "
            f"Available maze_themes: {available}"
        )


def list_maze_themes() -> list[str]:
    """Return the identifiers of all available maze_themes."""
    return list(MAZE_THEMES)