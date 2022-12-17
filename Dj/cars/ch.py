
from datetime import datetime
year_choice = []
for r in range(2010, (datetime.now().year+1)):
    year_choice.append((r,r))
print(year_choice)    