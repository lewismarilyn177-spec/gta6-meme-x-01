#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1080
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 255))
draw = ImageDraw.Draw(img)

def load_font(size):
    return ImageFont.truetype(FONT_PATH, size)

def draw_vertical_gradient(draw, width, height, colors):
    for y in range(height):
        t = y / (height - 1)
        if t < 0.5:
            t2 = t * 2
            c1, c2 = colors[0], colors[1]
        else:
            t2 = (t - 0.5) * 2
            c1, c2 = colors[1], colors[2]
        r = int(c1[0] * (1 - t2) + c2[0] * t2)
        g = int(c1[1] * (1 - t2) + c2[1] * t2)
        b = int(c1[2] * (1 - t2) + c2[2] * t2)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

deep_purple = (30, 10, 60)
magenta = (180, 0, 180)
hot_pink = (255, 50, 150)
pale_yellow = (255, 225, 150)
coin_magenta_pure = (226, 26, 140, 255)
dark_panel = (20, 10, 30, 230)
panel_outline = (255, 50, 150, 255)
white = (255, 255, 255, 255)
pink_text = (255, 100, 180, 255)
progress_fill = (255, 50, 150, 255)
progress_bg = (40, 20, 60, 255)
near_black = (20, 20, 20, 255)
ghost_white = (255, 255, 255, 255)
ocean_magenta = (180, 0, 130, 255)
wave_light = (220, 80, 180, 255)
coin_magenta = (255, 50, 180, 255)

draw_vertical_gradient(draw, WIDTH, HEIGHT, [deep_purple, magenta, hot_pink])

ocean_top = int(HEIGHT * 0.68)

sun_radius = 130
sun_cx = WIDTH // 2
sun_cy = ocean_top
sun_bbox = [sun_cx - sun_radius, sun_cy - sun_radius, sun_cx + sun_radius, sun_cy + sun_radius]
draw.ellipse(sun_bbox, fill=pale_yellow)

for scan in range(-sun_radius, sun_radius, 6):
    y = sun_cy + scan
    dx = int((sun_radius ** 2 - (y - sun_cy) ** 2) ** 0.5)
    draw.line([(sun_cx - dx, y), (sun_cx + dx, y)], fill=magenta)

draw.rectangle([0, ocean_top, WIDTH, HEIGHT], fill=ocean_magenta)
for w in range(ocean_top, HEIGHT, 12):
    draw.line([(0, w), (WIDTH, w)], fill=wave_light, width=2)

def draw_palm(x_base, trunk_height=350):
    trunk_top = HEIGHT - 100
    trunk_bottom = trunk_top - trunk_height
    draw.rectangle([x_base - 8, trunk_bottom, x_base + 8, trunk_top], fill=near_black)
    for angle in range(-60, 61, 30):
        import math
        rad = math.radians(angle)
        fx = x_base + int(math.sin(rad) * 120)
        fy = trunk_bottom + int(math.cos(rad) * 120)
        draw.line([(x_base, trunk_bottom), (fx, fy)], fill=near_black, width=6)

draw_palm(80)
draw_palm(WIDTH - 80)

panel_padding = 30
panel_height = 220
panel_rect = [panel_padding, panel_padding, WIDTH - panel_padding, panel_padding + panel_height]
draw.rounded_rectangle(panel_rect, radius=24, fill=dark_panel, outline=panel_outline, width=4)

title_font = load_font(56)
subtitle_font = load_font(32)
progress_font = load_font(24)

title_text = "GRAND THEFT AUTO VI"
subtitle_text = "Downloading... 13 years remaining"

title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
title_w = title_bbox[2] - title_bbox[0]
draw.text((WIDTH // 2 - title_w // 2, panel_padding + 24), title_text, font=title_font, fill=white)

sub_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
sub_w = sub_bbox[2] - sub_bbox[0]
draw.text((WIDTH // 2 - sub_w // 2, panel_padding + 96), subtitle_text, font=subtitle_font, fill=pink_text)

bar_x = panel_padding + 60
bar_y = panel_padding + 150
bar_w = WIDTH - 2 * panel_padding - 120
bar_h = 36
draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=10, fill=progress_bg, outline=panel_outline, width=2)
fill_w = int(bar_w * 0.95)
draw.rounded_rectangle([bar_x, bar_y, bar_x + fill_w, bar_y + bar_h], radius=10, fill=progress_fill)
progress_text = '95%  stuck at "Installing rockstar servers"'
pt_bbox = draw.textbbox((0, 0), progress_text, font=progress_font)
pt_w = pt_bbox[2] - pt_bbox[0]
draw.text((bar_x + (bar_w - pt_w) // 2, bar_y + 6), progress_text, font=progress_font, fill=white)

caption_font = load_font(36)
caption_text = "me on Nov 19, 2026:"
cap_bbox = draw.textbbox((0, 0), caption_text, font=caption_font)
cap_w = cap_bbox[2] - cap_bbox[0]
draw.text((WIDTH // 2 - cap_w // 2, 8), caption_text, font=caption_font, fill=white)

ghost_x = 100
ghost_y = HEIGHT - 320
ghost_w = 220
ghost_h = 280

dome_h = int(ghost_h * 0.6)
dome_bbox = [ghost_x, ghost_y, ghost_x + ghost_w, ghost_y + dome_h * 2]
scallop_y = ghost_y + dome_h
scallop_r = ghost_w // 6
bump_cx1 = ghost_x + scallop_r
bump_cx2 = ghost_x + ghost_w // 2
bump_cx3 = ghost_x + ghost_w - scallop_r

import math

def sparkle_points(cx, cy, r):
    pts = []
    for i in range(8):
        angle = math.radians(i * 45)
        radius = r if i % 2 == 0 else r * 0.3
        pts.append((cx + int(math.cos(angle) * radius), cy + int(math.sin(angle) * radius)))
    return pts

# Ghost body - dome with clean outline
points = []
for angle in range(180, 361):
    rad = math.radians(angle)
    px = ghost_x + ghost_w // 2 + int(math.cos(rad) * ghost_w // 2)
    py = ghost_y + dome_h + int(math.sin(rad) * dome_h)
    points.append((px, py))
draw.polygon(points, fill=ghost_white, outline=near_black, width=12)

# Ghost skirt bumps - white filled ellipses with thin near-black arc outline on lower half
for cx in [bump_cx1, bump_cx2, bump_cx3]:
    # White filled ellipse (full)
    draw.ellipse([cx - scallop_r, scallop_y - scallop_r, cx + scallop_r, scallop_y + scallop_r], fill=ghost_white)
    # Thin near-black arc on lower half only (10px wide)
    draw.arc([cx - scallop_r, scallop_y - scallop_r, cx + scallop_r, scallop_y + scallop_r], 0, 180, fill=near_black, width=10)

head_cx = ghost_x + ghost_w // 2
head_cy = ghost_y + int(dome_h * 0.55)

# Eyes - four-pointed sparkle stars (8 vertices)
eye_y = head_cy - 10
eye_size = 22
for ex in [head_cx - 35, head_cx + 35]:
    draw.polygon(sparkle_points(ex, eye_y, eye_size), fill=near_black)

arm_x = ghost_x + ghost_w - 5
arm_y = head_cy + 50
draw.line([(arm_x, arm_y), (arm_x + 85, arm_y - 30)], fill=ghost_white, width=16)

coin_cx = arm_x + 95
coin_cy = arm_y - 40
coin_r = 48
draw.ellipse([coin_cx - coin_r, coin_cy - coin_r, coin_cx + coin_r, coin_cy + coin_r], fill=coin_magenta_pure, outline=near_black, width=6)
# Coin star - sparkle shape, white, ~26px
draw.polygon(sparkle_points(coin_cx, coin_cy, 26), fill=white)

wordmark_font = load_font(48)
wordmark_text = "make.fun"
wm_bbox = draw.textbbox((0, 0), wordmark_text, font=wordmark_font)
wm_w = wm_bbox[2] - wm_bbox[0]
wm_x = WIDTH - wm_w - 60
wm_y = HEIGHT - 100
sparkle_x = wm_x - 50
sparkle_y = wm_y + 15
sparkle_s = 18
draw.polygon(sparkle_points(sparkle_x, sparkle_y, sparkle_s), fill=white)
draw.text((wm_x, wm_y), wordmark_text, font=wordmark_font, fill=white)

img.save("/root/makefun/gta6-meme-x-01-entry/meme.png")
print("Saved meme.png")