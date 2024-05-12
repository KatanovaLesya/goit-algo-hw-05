encodings = ['windows-1252', 'iso-8859-1', 'iso-8859-2', 'iso-8859-5']
for enc in encodings:
    try:
        with open('/Users/lesyakatanova/Documents/Навчання/GOIT/ДЗ_5_Катанова/file01.txt', 'r', encoding=enc) as file:
            text = file.read()
        print(f"Success with encoding: {enc}")
        break
    except UnicodeDecodeError:
        print(f"Failed with encoding: {enc}")
