"""
Generate brand-new product images without branding.
Creates bags, cake boxes, and gift boxes with similar dimensions and colors.
"""

from PIL import Image, ImageDraw, ImageFilter, ImageOps
import random
import os

# Ensure images directory exists
os.makedirs('images', exist_ok=True)

# Image dimensions (approximate based on original sizes)
STANDARD_WIDTH = 800
STANDARD_HEIGHT = 600

# Color palettes for different product types
BAG_COLORS = [
    {'main': (220, 80, 80), 'accent': (180, 40, 40), 'light': (255, 150, 150)},      # Red
    {'main': (80, 150, 220), 'accent': (40, 100, 180), 'light': (150, 200, 255)},    # Blue
    {'main': (220, 180, 80), 'accent': (180, 140, 40), 'light': (255, 220, 150)},    # Gold
    {'main': (100, 200, 100), 'accent': (50, 150, 50), 'light': (180, 255, 180)},    # Green
    {'main': (180, 100, 200), 'accent': (140, 50, 160), 'light': (220, 180, 255)},   # Purple
    {'main': (220, 140, 100), 'accent': (180, 100, 60), 'light': (255, 200, 170)},   # Orange
]

CAKE_BOX_COLORS = [
    {'main': (245, 220, 200), 'accent': (200, 150, 120), 'detail': (220, 100, 100)},  # Beige/Red
    {'main': (255, 240, 245), 'accent': (230, 200, 220), 'detail': (200, 100, 150)},  # Pink
    {'main': (240, 240, 245), 'accent': (200, 200, 220), 'detail': (100, 100, 200)},  # Blue tint
    {'main': (250, 245, 220), 'accent': (220, 210, 180), 'detail': (200, 150, 50)},   # Cream/Gold
    {'main': (245, 235, 245), 'accent': (210, 190, 210), 'detail': (150, 50, 150)},   # Lavender
]

GIFT_BOX_COLORS = [
    {'main': (200, 50, 50), 'accent': (150, 30, 30), 'ribbon': (255, 215, 0)},        # Red/Gold
    {'main': (50, 100, 200), 'accent': (30, 70, 150), 'ribbon': (255, 255, 255)},     # Blue/White
    {'main': (50, 150, 50), 'accent': (30, 110, 30), 'ribbon': (255, 50, 50)},        # Green/Red
    {'main': (180, 50, 180), 'accent': (140, 30, 140), 'ribbon': (255, 215, 0)},      # Purple/Gold
    {'main': (255, 140, 0), 'accent': (220, 110, 0), 'ribbon': (255, 255, 255)},      # Orange/White
    {'main': (100, 180, 220), 'accent': (70, 140, 180), 'ribbon': (255, 100, 100)},   # Cyan/Red
    {'main': (220, 100, 150), 'accent': (180, 70, 120), 'ribbon': (255, 215, 0)},     # Pink/Gold
    {'main': (150, 120, 100), 'accent': (110, 85, 65), 'ribbon': (255, 215, 0)},      # Brown/Gold
    {'main': (80, 200, 180), 'accent': (50, 160, 140), 'ribbon': (255, 255, 255)},    # Teal/White
]


def create_bag(filename, color_palette, index):
    """Create a product bag image."""
    img = Image.new('RGB', (STANDARD_WIDTH, STANDARD_HEIGHT), color=(240, 240, 240))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Draw bag body with gradient effect
    # Left side darker
    draw.rectangle(
        [(100, 50), (700, 550)],
        fill=color_palette['main']
    )
    
    # Highlight area (lighter side)
    highlight_points = [(120, 80), (300, 50), (350, 450), (150, 550)]
    draw.polygon(highlight_points, fill=color_palette['light'])
    
    # Bag handles
    draw.arc([(150, 30), (300, 180)], 0, 180, fill=color_palette['accent'], width=15)
    draw.arc([(500, 30), (650, 180)], 0, 180, fill=color_palette['accent'], width=15)
    
    # Shadow at bottom
    draw.rectangle([(120, 520), (680, 550)], fill=(50, 50, 50, 100))
    
    # Add decorative lines
    draw.line([(200, 150), (200, 500)], fill=color_palette['accent'], width=3)
    draw.line([(600, 150), (600, 500)], fill=color_palette['accent'], width=3)
    
    img.save(f'images/PP_Bags_{index}.jpeg', 'JPEG', quality=95)
    print(f"✓ Created PP_Bags_{index}.jpeg")


def create_cake_box(filename, color_palette, index):
    """Create a cake box image."""
    img = Image.new('RGB', (STANDARD_WIDTH, STANDARD_HEIGHT), color=(245, 245, 245))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Main box body (isometric view)
    # Front face
    draw.rectangle(
        [(150, 150), (650, 450)],
        fill=color_palette['main'],
        outline=color_palette['accent']
    )
    
    # Top face (lid)
    top_left = [(150, 150), (200, 120), (650, 120), (600, 150)]
    draw.polygon(top_left, fill=color_palette['accent'])
    
    # Right face
    right_face = [(650, 150), (600, 120), (600, 420), (650, 450)]
    draw.polygon(right_face, fill=tuple(max(0, c - 40) for c in color_palette['main']))
    
    # Decorative ribbon/stripe
    draw.rectangle([(170, 280), (630, 310)], fill=color_palette['detail'])
    draw.rectangle([(170, 285), (630, 305)], outline=(255, 255, 255), width=2)
    
    # Window area (showing product)
    window_color = (200 + random.randint(-30, 30), 
                   180 + random.randint(-30, 30), 
                   160 + random.randint(-30, 30))
    draw.rectangle([(200, 200), (600, 380)], fill=window_color, outline=color_palette['accent'], width=2)
    
    # Add shine effect
    draw.arc([(250, 200), (550, 300)], 0, 180, fill=(255, 255, 255, 100), width=4)
    
    img.save(f'images/PP_CakeBox_{index}.jpeg', 'JPEG', quality=95)
    print(f"✓ Created PP_CakeBox_{index}.jpeg")


def create_gift_box(filename, color_palette, index):
    """Create a gift box image."""
    img = Image.new('RGB', (STANDARD_WIDTH, STANDARD_HEIGHT), color=(250, 250, 250))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Gift box body - isometric view
    # Front face (main)
    draw.rectangle(
        [(150, 200), (650, 500)],
        fill=color_palette['main'],
        outline=(0, 0, 0)
    )
    
    # Top face
    top_face = [(150, 200), (180, 140), (680, 140), (650, 200)]
    draw.polygon(top_face, fill=color_palette['accent'])
    
    # Right side face
    right_face = [(650, 200), (680, 140), (680, 440), (650, 500)]
    draw.polygon(right_face, fill=tuple(max(0, c - 50) for c in color_palette['main']))
    
    # Ribbon around box (horizontal)
    draw.rectangle([(140, 320), (660, 360)], fill=color_palette['ribbon'])
    draw.rectangle([(145, 325), (655, 355)], outline=(255, 255, 255), width=3)
    
    # Ribbon bow on top
    bow_x, bow_y = 415, 140
    bow_size = 60
    # Left loop
    draw.ellipse(
        [(bow_x - bow_size, bow_y - 30), (bow_x - 20, bow_y + 30)],
        fill=color_palette['ribbon']
    )
    # Right loop
    draw.ellipse(
        [(bow_x + 20, bow_y - 30), (bow_x + bow_size, bow_y + 30)],
        fill=color_palette['ribbon']
    )
    # Center knot
    draw.ellipse(
        [(bow_x - 15, bow_y - 15), (bow_x + 15, bow_y + 15)],
        fill=(200, 170, 0)
    )
    
    # Shine/highlight
    draw.arc([(200, 220), (600, 380)], 0, 180, fill=(255, 255, 255, 80), width=5)
    
    # Shadow at bottom
    draw.rectangle([(150, 480), (650, 510)], fill=(0, 0, 0, 50))
    
    img.save(f'images/PP_GiftBox_{index}.jpeg', 'JPEG', quality=95)
    print(f"✓ Created PP_GiftBox_{index}.jpeg")


def main():
    """Generate all product images."""
    print("\n🎨 Generating brand-new product images without branding...\n")
    
    # Generate bags
    print("Creating Bags...")
    for i in range(1, 7):
        create_bag(f'PP_Bags_{i}.jpeg', BAG_COLORS[(i-1) % len(BAG_COLORS)], i)
    
    # Generate cake boxes
    print("\nCreating Cake Boxes...")
    for i in range(1, 6):
        create_cake_box(f'PP_CakeBox_{i}.jpeg', CAKE_BOX_COLORS[(i-1) % len(CAKE_BOX_COLORS)], i)
    
    # Generate gift boxes
    print("\nCreating Gift Boxes...")
    for i in range(1, 10):
        create_gift_box(f'PP_GiftBox_{i}.jpeg', GIFT_BOX_COLORS[(i-1) % len(GIFT_BOX_COLORS)], i)
    
    print("\n✅ All images generated successfully!")
    print("📁 Images saved to: images/")


if __name__ == '__main__':
    main()
