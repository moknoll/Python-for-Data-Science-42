from datetime import datetime

curr = datetime.now()
epoch_sec = curr.timestamp()
scientific_format = "{:.2e}".format(int(epoch_sec))
today = curr.strftime("%b %d %Y")

print(f'Seconds since January 1, 1970: {epoch_sec:,.4f} or {scientific_format} in scientific notation')
print(today)



