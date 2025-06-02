# Don't Remove Credit Telegram - @spidy_universe
import time
import math
import os
from pyrogram.errors import FloodWait
from datetime import datetime, timedelta

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def hrb(value, digits=2, delim="", postfix=""):
    """Return a human-readable file size."""
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KB", "MB", "GB", "TB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f} {chosen_unit}"

def hrt(seconds, precision=0):
    """Return a human-readable time delta as a string."""
    pieces = []
    value = timedelta(seconds=seconds)
    
    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])

timer = Timer()

async def download_progress_bar(current, total, reply, start, filename="File"):
    """New Download Progress Bar"""
    if timer.can_send():
        now = time.time()
        elapsed = now - start
        if elapsed < 1:
            return
        
        # Calculate progress
        perc = (current * 100 / total)
        speed = current / elapsed
        remaining_bytes = total - current
        
        if speed > 0:
            eta_seconds = remaining_bytes / speed
            eta = f"{int(eta_seconds)}s"
        else:
            eta = "-"
        
        # Format sizes
        current_size = hrb(current)
        total_size = hrb(total)
        speed_str = hrb(speed) + "/s"
        elapsed_str = f"{int(elapsed)}s"
        
        # Create progress bar (20 circles)
        bar_length = 20
        filled_length = int(current * bar_length / total)
        bar = "●" * filled_length + "○" * (bar_length - filled_length)
        
        progress_text = (
            f"**Downloading**\n\n"
            f"**{filename}**\n\n"
            f"{current_size} Out Of {total_size}\n"
            f"[{bar}] {perc:.2f}%\n\n"
            f"**Speed:** {speed_str}\n"
            f"**ETA:** {eta}\n"
            f"**Elapsed:** {elapsed_str}"
        )
        
        try:
            await reply.edit(progress_text)
        except FloodWait as e:
            time.sleep(e.x)
        except Exception:
            pass

async def upload_progress_bar(current, total, reply, start, filename="File"):
    """New Upload Progress Bar"""
    if timer.can_send():
        now = time.time()
        elapsed = now - start
        if elapsed < 1:
            return
        
        # Calculate progress
        perc = (current * 100 / total)
        speed = current / elapsed
        remaining_bytes = total - current
        
        if speed > 0:
            eta_seconds = remaining_bytes / speed
            eta = f"{int(eta_seconds)}s"
        else:
            eta = "-"
        
        # Format sizes
        current_size = hrb(current)
        total_size = hrb(total)
        speed_str = hrb(speed) + "/s"
        elapsed_str = f"{int(elapsed)}s"
        
        # Create progress bar (20 circles)
        bar_length = 20
        filled_length = int(current * bar_length / total)
        bar = "●" * filled_length + "○" * (bar_length - filled_length)
        
        progress_text = (
            f"**Uploading**\n\n"
            f"**{filename}**\n\n"
            f"{current_size} Out Of {total_size}\n"
            f"[{bar}] {perc:.2f}%\n\n"
            f"**Speed:** {speed_str}\n"
            f"**ETA:** {eta}\n"
            f"**Elapsed:** {elapsed_str}"
        )
        
        try:
            await reply.edit(progress_text)
        except FloodWait as e:
            time.sleep(e.x)
        except Exception:
            pass

async def progress_bar(current, total, reply, start):
    """Main progress bar function for compatibility"""
    if timer.can_send():
        now = time.time()
        elapsed = now - start
        if elapsed < 1:
            return
        
        # Calculate progress
        perc = (current * 100 / total)
        speed = current / elapsed
        remaining_bytes = total - current
        
        if speed > 0:
            eta_seconds = remaining_bytes / speed
            eta = f"{int(eta_seconds)}s"
        else:
            eta = "-"
        
        # Format sizes
        current_size = hrb(current)
        total_size = hrb(total)
        speed_str = hrb(speed) + "/s"
        elapsed_str = f"{int(elapsed)}s"
        
        # Create progress bar (20 circles)
        bar_length = 20
        filled_length = int(current * bar_length / total)
        bar = "●" * filled_length + "○" * (bar_length - filled_length)
        
        progress_text = (
            f"**Processing**\n\n"
            f"**File**\n\n"
            f"{current_size} Out Of {total_size}\n"
            f"[{bar}] {perc:.2f}%\n\n"
            f"**Speed:** {speed_str}\n"
            f"**ETA:** {eta}\n"
            f"**Elapsed:** {elapsed_str}"
        )
        
        try:
            await reply.edit(progress_text)
        except FloodWait as e:
            time.sleep(e.x)
        except Exception:
            pass
