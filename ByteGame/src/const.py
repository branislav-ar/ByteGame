# Ekran
WIDTH = 600
HEIGHT = 600

# Tabla
ROWS = 8
COLS = 8
SQSIZE = WIDTH // COLS

# Figure i stekovi
FULL_STACK = 8
TOTAL_STACKS = (ROWS-2) * (ROWS/2) // FULL_STACK # 3 steka za 8x8 tablu
STACKS_TO_WIN_GAME = TOTAL_STACKS // 2 + 1 # 2 steka za 8x8 tablu
