import board
import digitalio
import adafruit_ili9341
from PIL import Image, ImageDraw

# تنظیمات پین‌ها
spi = board.SPI()
dc = digitalio.DigitalInOut(board.D25)  # پین DC
cs = digitalio.DigitalInOut(board.CE0)  # پین Chip Select

# راه‌اندازی LCD
display = adafruit_ili9341.ILI9341(spi, cs=cs, dc=dc)

# ایجاد تصویر
img = Image.new("RGB", (display.width, display.height), "blue")
draw = ImageDraw.Draw(img)
draw.rectangle((10, 10, 100, 100), fill="red")

# نمایش تصویر روی LCD
display.image(img)
