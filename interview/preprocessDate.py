def preprocessDate(dates: list[str]):
    
    # 20th Oct 2052 -> 2052-10-20
    months = {
        m: i + 1 for i, m in enumerate([
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ])
    }
    def parse(date: str) -> str:
        [day, month, year] = date.split()
        day = day[:-2]
        month = str(months[month])
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    
    return [parse(date) for date in dates]

print(preprocessDate(["20th Oct 2052", "6th Jun 1933", "26th May 1960"]))
