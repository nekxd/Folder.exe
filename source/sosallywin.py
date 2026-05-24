import sys
import time
import array
import pygame
import win32gui
import win32con
import win32api
import random
import math


user_choice = win32gui.MessageBox(
    0, 
    "ДАННЫЙ ПРОЕКТ МОЖЕТ НАВРЕДИТЬ!\nПри случаи приступа эпилепсии,немедленно позвонить в 112 или в 911 и выключить ПК!\nСделано n3kxdd канал @APXUBbl_BUPYC0B", 
    "sosallywin", 
    win32con.MB_YESNO | win32con.MB_ICONEXCLAMATION
)

if user_choice == win32con.IDNO:
    sys.exit()


pygame.mixer.pre_init(frequency=8000, size=-8, channels=1, buffer=1024)
pygame.init()

SAMPLE_RATE = 8000
DURATION = 250
TOTAL_SAMPLES = SAMPLE_RATE * DURATION

sound_buffer = bytearray(TOTAL_SAMPLES)

for t in range(TOTAL_SAMPLES):
    val = (
        ((t > 0 and t < 237568) * (t & t >> 8)) |
        ((t > 245760 and t < 475136) * (t >> 5 | (t >> 2) * (t >> 5))) |
        ((t > 483328 and t < 724992) * (((t >> 5 & t) - (t >> 5) + (t >> 5 & t)) + (t * (((t + 40960) >> 14) & 14)))) |
        ((t > 729088 and t < 966656) * (t + (t & t ^ t >> 6) - t * ((t >> 9) & (t % 16 if 0 else 2 if t % 16 else 6) & t >> 9))) |
        ((t > 970752 and t < 1208320) * (t * (t ^ t + ((t - 970752) >> 15 | 1) ^ (t - 1280 ^ t) >> 10))) |
        ((t > 1212416 and t < 1437696) * (t * ((int(t / 2) >> 10 | t % 16 * t >> 8) & 8 * t >> 12 & 18) | -int(t / 16) + 64)) |
        ((t > 1441792 and t < 1679360) * (t * (6 if t & 16384 else 5) * (4 - (1 & t >> 8)) >> (3 & t >> 9) | (t | t * 3) >> 5)) |
        ((t > 1683456 and t < 1900544) * (t * ((6 if t & 4096 else 16) + (1 & (t + 16384) >> 14)) >> (3 & t >> 8) | t >> (3 if t & 4096 else 4))) |
        ((t > 1900544) * (t * ((7 if t % 65536 < 59392 else t & 7 if t & 4096 else 16) + (1 & t >> 14)) >> (3 & -t >> (2 if t & 2048 else 10)) | (t > (10 if t & 4096 else 3 if t & 16384 else 2))))
    )
    sound_buffer[t] = val & 255

sound_object = pygame.mixer.Sound(buffer=sound_buffer)
sound_object.play()

hdc = win32gui.GetDC(0)
sw = win32api.GetSystemMetrics(0)
sh = win32api.GetSystemMetrics(1)

start_time = time.time()
try:
    while pygame.mixer.get_busy():
        elapsed = time.time() - start_time
        current_t = int(elapsed * SAMPLE_RATE)
        
        if current_t < TOTAL_SAMPLES:
            b = sound_buffer[current_t]
        else:
            break
            
        rx = random.randint(0, sw)
        ry = random.randint(0, sh)
        
        
        if current_t % 16 == 0:
            
            win32gui.BitBlt(hdc, 0, random.randint(0, sh), sw, random.randint(50, 300), hdc, 0, random.randint(0, sh), win32con.NOTSRCCOPY)

        
        
        
        if 0 < current_t < 237568:
            win32gui.BitBlt(hdc, random.randint(-15, 15), random.randint(-15, 15), sw, sh, hdc, 0, 0, win32con.SRCINVERT)
            
        
        elif 245760 < current_t < 475136:
            h_line = random.randint(10, 50)
            win32gui.BitBlt(hdc, (b % 40) - 20, ry, sw, h_line, hdc, 0, ry, win32con.SRCPAINT)
            if b > 180:
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, 0, 0, win32con.DSTINVERT)
            
        
        elif 483328 < current_t < 724992:
            
            color = win32api.RGB(random.randint(0, 255), b, 255 - b)
            brush = win32gui.CreateSolidBrush(color)
            win32gui.FillRect(hdc, (rx - b, ry - b, rx + b, ry + b), brush)
            win32gui.DeleteObject(brush)
            if current_t % 4 == 0:
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, 0, 0, win32con.NOTSRCCOPY)
                
        
        elif 729088 < current_t < 966656:
            color = win32api.RGB(b ^ 255, (current_t >> 2) & 255, b)
            brush = win32gui.CreateSolidBrush(color)
            win32gui.FillRect(hdc, (0, ry, sw, ry + (b % 30)), brush)
            win32gui.DeleteObject(brush)
            win32gui.BitBlt(hdc, random.randint(-5, 5), 0, sw, sh, hdc, 0, 0, win32con.SRCERASE)
            
        
        elif 970752 < current_t < 1208320:
            
            win32gui.StretchBlt(hdc, 15, 15, sw - 30, sh - 30, hdc, 0, 0, sw, sh, win32con.MERGEPAINT)
            if b % 5 == 0:
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, 0, 0, win32con.DSTINVERT)
            
        
        elif 1212416 < current_t < 1437696:
            
            wave = int(math.sin(current_t) * 20)
            win32gui.StretchBlt(hdc, 0, wave, sw, sh - abs(wave), hdc, 0, 0, sw, sh, win32con.SRCCOPY)
            win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCINVERT)
            
        
        elif 1441792 < current_t < 1679360:
            win32gui.PatBlt(hdc, rx, ry, b * 3, b * 2, win32con.PATINVERT)
            if current_t % 3 == 0:
                win32gui.BitBlt(hdc, random.randint(-50, 50), 0, sw, sh, hdc, 0, 0, win32con.SRCPAINT)
                
        
        elif 1683456 < current_t < 1900544:
            
            win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, 0, 0, win32con.DSTINVERT)
            win32gui.StretchBlt(hdc, rx, ry, b, b, hdc, random.randint(0, sw), random.randint(0, sh), b, b, win32con.SRCCOPY)
            
       
        elif current_t > 1900544:
            win32gui.StretchBlt(hdc, -10, -10, sw + 20, sh + 20, hdc, 0, 0, sw, sh, win32con.SRCPAINT)
            win32gui.BitBlt(hdc, random.randint(-30, 30), random.randint(-30, 30), sw, sh, hdc, 0, 0, win32con.SRCINVERT)
            if b % 2 == 0:
                win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, 0, 0, win32con.NOTSRCCOPY)

        
        time.sleep(0.001)

except KeyboardInterrupt:
    pass

finally:
    pygame.mixer.stop()
    win32gui.ReleaseDC(0, hdc)
    # Форсированное стирание глитчей с рабочего стола при выходе
    win32gui.RedrawWindow(0, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE | win32con.RDW_ALLCHILDREN)
