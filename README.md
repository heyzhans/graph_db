# graph_db

Была выбрана графовая бд neo4j. В note.ipynb описаны шаги подключения и добавления данных.
Создается узел «Event» со значением свойства «id», взятым из столбца «id события», узел «Person» со значением свойства «имя», взятым из «ФИО». столбец наличия событий 1" и еще один узел "Person" со значением свойства "имя", взятым из столбца "ФИО наличия событий 2".
Затем два отношения «PARTICIPATED_IN» между узлом «Event» и каждым узлом «Person».

![image](https://user-images.githubusercontent.com/81826648/225326245-1aa9c45b-34e1-4bfa-95e3-95dd64792c78.png)

Алгоритм Лувена — популярный метод обнаружения сообществ на графах. Это иерархический агломеративный алгоритм кластеризации, целью которого является максимизация модульности, мера качества разделения сети на сообщества. В Python вы можете использовать communityмодуль библиотеки networkxдля запуска алгоритма Лувена.

Чтобы использовать алгоритм Лувена для обнаружения сообщества в графовой базе данных, такой как Neo4j, нужно сначала извлечь граф в формат, который может обрабатываться библиотекой networkx.
Cначала создаем подключение к графовой базе данных Neo4j, используя класс Graph из py2neo библиотеки. Затем используем запрос Cypher для получения всех узлов типа «Person», которые участвуют в событиях типа «Event» через отношение «PARTICIPATED_IN». Результатом является объект Node и Event для каждой записи, которые мы добавляем как узлы и ребра к networkx графу, используя их свойства имени и идентификатора соответственно.

Получив networkx график, мы можем применить алгоритм Лувена, используя best_partition() функцию из community модуля. 
networkx с Matplotlib: можно использовать networkx для визуализации графика и раскрашивания узлов в соответствии с их назначениями сообщества. Результат:



![image](https://user-images.githubusercontent.com/81826648/225325766-4019a656-f14e-42be-9b19-4b0649e44bb7.png)

Сложность сообществ, идентифицированных алгоритмом Лувена, следует анализировать и визуализировать с помощью соответствующих инструментов, таких как тепловые карты или дендрограммы. Это может помочь раскрыть внутреннюю структуру и динамику сообществ, таких как их подсообщества, центральные узлы или временные закономерности.

Результаты алгоритма Лувена следует сочетать с другими анализами и знаниями предметной области, чтобы получить более глубокое понимание отношений между людьми и событиями. Например, можно проанализировать свойства узлов и ребер в каждом сообществе, такие как их центральность, степень или коэффициент кластеризации, чтобы определить ключевых участников или действия.


# Rest сервис на python (Flask) к графовой БД в котором на вход поступает ФИО, на выходе json

![image](https://user-images.githubusercontent.com/81826648/225325884-486a134e-6ce1-4ecf-b43f-37b06639d369.png)

![image](https://user-images.githubusercontent.com/81826648/225326168-6055d3ac-0c9d-4f28-982c-494631fd39cb.png)
