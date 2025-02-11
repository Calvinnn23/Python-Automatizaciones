import calendar
from pathlib import Path

yearMonths = list(calendar.month_name[1:])
weekDays = ["Dia 1", "Dia 10", "Dia 20", "Dia 30"]

for i, month in enumerate(yearMonths):
    for day in weekDays:
        Path(f"2024/{i + 1}.{month}/{day}").mkdir(parents=True, exist_ok=True)

print("Carpetas creadas!")
