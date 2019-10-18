avg_by_hour = []
for hour in comments_by_hour:
    avg = comments_by_hour[hour]/counts_by_hour[hour]
    avg_by_hour.append([hour,avg])
print(avg_by_hour)
