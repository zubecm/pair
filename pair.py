with open('C:\\Users\\ASUS\\Downloads\\PythonTest.txt', 'r', encoding='utf-8') as file,\
     open('C:\\Users\\ASUS\\Downloads\\English.txt', 'w', encoding='utf-8') as english,\
     open('C:\\Users\\ASUS\\Downloads\\Russian.txt', 'w', encoding='utf-8') as russian:
    for line in file:
        words = line.split('\t')                                    # Разбиваю строку на отдельные списки английские слова и русские
        eng, rus = words[0].split(';'), words[1].split(';')         # Разбиваю списки на слова
        for i in eng:
            for j in rus:                                           # Вложенным циклом присваиваю английскому слову каждое соответствуещее русское
                english.write(i.strip()+'\n')                       # Записываю новые файлы
                if j is rus[-1]:
                    russian.write(j.lstrip())
                else:
                    russian.write(j.strip()+'\n')
