#!/bin/sh
mapreduce(){
        hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}
alias hs=mapreduce

echo "***********************************************************************************************************"
echo "* Remarque: Les mapper/reducer sont testés sur le fichier test.tsv					*"
echo "* Voir le rapport pour plus d'informations sur le code							*"
echo "*														*"
echo "*	Commande =  num de la partie + num de sous-partie du rapport:						*"
echo "* (1) Execute toutes les commandes									*"
echo "* (23) Mapper récupérant les posts d'une phrase ou moins							*"
echo "*	(24) Reducer comptant le nombre de posts d'une phrase ou moins 						*"
echo "*	(261) Mapper pour trouver les 10 phrases les plus longues						*"
echo "*	(262) Reducer pour trouver les 10 phrases les plus longues 						*"
echo "*	(311) Mapper  pour extraire les mots d'un post avec l'ID du node 					*"
echo "*	(312) Reducer pour donner chacun des mots: le nombre d'occurences et la liste des node_ID		*"
echo "*														*"
echo "* Utilisation du fichier purchasesTest.txt								*"
echo "*	(321) MapReduce pour calculer la moyenne des ventes chaque jour de la semaine : purchasesTest.txt*"
echo "* (431) MapReduce pour calculer la somme des ventes chaque jour de la semaine: purchasesTest.txt		*"

echo "* Tous les résultats sont dans le dossier res/res[le num de la commande].txt)				*"
echo "***********************************************************************************************************"
echo
echo "Votre choix : "
read choice

case $choice in

1) 
echo "**** All commands ****"
cat ./datas/test.tsv | ./part2/mapper.py > ./res/res23.txt
cat ./datas/test.tsv | ./part2/mapper.py | ./part2/reducer.py  > ./res/res24.txt
cat ./datas/test.tsv | ./part2/mapper2.py  > ./res/res261.txt
cat ./datas/test.tsv | ./part2/mapper2.py | ./part2/reducer2.py  > ./res/res262.txt
cat ./datas/test.tsv | ./part3/mapper.py > ./res/res311.txt
cat ./datas/test.tsv | ./part3/mapper.py | sort | ./part3/reducer.py > ./res/res312.txt
cat ./datas/purchasesTest.txt | ./part3/mapper2.py | sort | ./part3/reducer2.py > ./res/res321.txt
cat ./datas/purchasesTest.txt | ./part4/mapper.py | sort | ./part4/reducer.py > ./res/res431.txt

;;

23)
echo "**** part 2.3: Mapper posts with only one or less sentence ****"
cat ./datas/test.tsv | ./part2/mapper.py > ./res/res23.txt
;;

24)
echo "**** part 2.4: Reducer to get number of posts which contain less than one sentence  ****"
cat ./datas/test.tsv | ./part2/mapper.py | ./part2/reducer.py  > ./res/res24.txt
;;

261)
echo "**** part 2.6: Mapper to get 10 first longest posts on test.tsv ****"
cat ./datas/test.tsv | ./part2/mapper2.py  > ./res/res261.txt
;;

262)
echo "**** part 2.6: Reducer to get 10 first longest posts on test.tsv ****"
cat ./datas/test.tsv | ./part2/mapper2.py | ./part2/reducer2.py  > ./res/res262.txt
;;

311)
echo "*** part 3.1.1: Mapper to get words and the list of id_node where they are ****"
cat ./datas/test.tsv | ./part3/mapper.py > ./res/res311.txt
;;

312)
echo "*** part 3.1.2: Reducer to get for each word: number of occurences  and the list of id_node where they are ****"
cat ./datas/test.tsv | ./part3/mapper.py | sort | ./part3/reducer.py > ./res/res312.txt
;;

321)
echo "*** part 3.2.1: MapReduce to extract the average of sells each day of the week ***"
cat ./datas/purchasesTest.txt | ./part3/mapper2.py | sort | ./part3/reducer2.py > ./res/res321.txt
;;

431)
echo "*** part 4.3.1: MapReduce to extract the sum of sells each day of the week ***"
cat ./datas/purchasesTest.txt | ./part4/mapper.py | sort | ./part4/reducer.py > ./res/res431.txt

;;

esac


