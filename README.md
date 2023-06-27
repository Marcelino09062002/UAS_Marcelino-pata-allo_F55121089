# UAS_marcelino_F55121089

analisis nomor 1

Worst case:
Bubble Sort: Pada worst case, bubble sort memiliki kompleksitas waktu O(n^2), di mana n adalah jumlah elemen dalam list. Worst case terjadi ketika list dalam keadaan terurut terbalik, sehingga setiap elemen harus dipindahkan ke posisi yang tepat melalui iterasi penuh.
Insertion Sort: Pada worst case, insertion sort juga memiliki kompleksitas waktu O(n^2). Hal ini terjadi ketika list dalam keadaan terurut terbalik, dan setiap elemen harus dipindahkan ke posisi yang tepat dengan pergeseran elemen-elemen lain.

Best case:
Bubble Sort: Pada best case, bubble sort memiliki kompleksitas waktu O(n). Hal ini terjadi ketika list sudah dalam keadaan terurut secara ascending, sehingga tidak ada pertukaran elemen yang diperlukan dalam iterasi.
Insertion Sort: Pada best case, insertion sort memiliki kompleksitas waktu O(n). Hal ini terjadi ketika list sudah dalam keadaan terurut secara ascending, dan tidak ada pergeseran elemen yang diperlukan selama iterasi.

Average case:
Bubble Sort: Pada average case, bubble sort memiliki kompleksitas waktu O(n^2). Rata-rata, setengah dari elemen dalam list harus dipindahkan ke posisi yang tepat melalui pertukaran.
Insertion Sort: Pada average case, insertion sort memiliki kompleksitas waktu O(n^2). Rata-rata, setengah dari elemen dalam list harus dipindahkan ke posisi yang tepat dengan pergeseran elemen-elemen lain.
Dalam kasus pengurutan list yang diberikan, baik bubble sort maupun insertion sort akan memiliki kompleksitas waktu O(n^2) dalam worst case dan average case, serta O(n) dalam best case (khususnya jika list sudah dalam keadaan terurut secara ascending sejak awal).

Selain itu, perlu dicatat bahwa insertion sort cenderung lebih efisien daripada bubble sort karena memiliki sedikit operasi pertukaran elemen. Namun, jika jumlah elemen dalam list sangat kecil, perbedaan dalam kinerja keduanya mungkin tidak signifikan.

analisis nomor 2

Worst case:
Algoritma TSP: Tidak ada definisi worst case yang jelas untuk TSP karena kompleksitas waktu algoritma TSP adalah O(n!), di mana n adalah jumlah node dalam graph. Ini berarti waktu komputasi meningkat secara eksponensial dengan penambahan node dalam graph.
Algoritma Dijkstra: Pada worst case, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah jumlah edge dalam graph. Jadi, dalam kasus terburuk, waktu komputasi algoritma Dijkstra meningkat dengan jumlah node dan edge dalam graph.

Best case:
Algoritma TSP: Tidak ada definisi best case yang jelas untuk TSP karena kompleksitas waktu algoritma TSP adalah O(n!).
Algoritma Dijkstra: Pada best case, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V). Dalam kasus terbaik, waktu komputasi algoritma Dijkstra dapat mencapai O(V log V) ketika graph adalah graf berbobot positif dan jarak terpendek dari source node ke semua node lainnya adalah konstan.

Average case:
Algoritma TSP: Tidak ada definisi average case yang jelas untuk TSP karena kompleksitas waktu algoritma TSP adalah O(n!).
Algoritma Dijkstra: Pada average case, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V). Dalam kasus rata-rata, algoritma Dijkstra bekerja lebih cepat ketika graph tidak terlalu kompleks dan jarak terpendek antara node-node tidak memiliki perbedaan yang signifikan.
