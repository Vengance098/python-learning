year=['2024','2026','2001','2007']
for years in year:
    years=int(years)
    if(years%4==0 and years%100!=0)or(years%400==0):
        print(f"{year},is a leap year")
    else:
        print(f"{years},is not a leap year")
    