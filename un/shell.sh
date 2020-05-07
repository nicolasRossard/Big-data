#!/bin/sh
mapreduce(){
        hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}
alias hs=mapreduce

echo "*******************************************************************************************"
echo "*	IMPORTANT avant de lancer: 								*"
echo "* - Ajouter les données dans ./data/purchases.txt						*"
echo "* - Mettre purchases.txt dans myinput sur Hadoop						*"
echo "*												*"
echo "*	Commande:										*"
echo "*	(1) Test en local du mapper en python							*"
echo "*	(2) Test en local du reducer en python							*"	
echo "* (3) Test sur Hadoop le mapper et le reducer en Python					*"
echo "*	(4) Test sur Hadoop le mapper et le reducer en Java					*"
echo "*	(51) Liste des ventes par catégories en Java						*"
echo "*	(52) Liste des ventes par catégories en Python						*"
echo "*	(61) Liste de la meilleure vente/magasin en Java					*"
echo "*	(62) Liste de la meilleure vente/magasin en Python					*"
echo "*	(71) Total des ventes de tous les produits pour tous les magasins en Java		*"
echo "*	(72) Total des ventes de tous les produits pour tous les magasins en Python		*"
echo "*												*"
echo "* Tous les résultats sont dans le dossier resultat (res + le num de la commande)		*"
echo "*******************************************************************************************"
echo
echo "Votre choix : "
read choice

case $choice in
1)
echo "**** PYTHON: Local mapper ****"
cat data/purchases.txt|pythonCode/etape2/mapper.py > resultat/res1
;; 

2)
echo "**** PYTHON: Local reducer ****"
cat data/purchases.txt |pythonCode/etape2/mapper.py |sort |pythonCode/etape2/reducer.py > resultat/res2
;;

3)
echo "**** PYTHON: Hadoop mapper + reducer ****"
hs pythonCode/etape2/mapper.py pythonCode/etape2/reducer.py myinput/purchases.txt out3
hadoop fs -get out3/p*
mv par* res3
mv res3 resultat/
hadoop fs -rmr out3
;;

4)
echo "**** JAVA: Hadoop mapper + reducer ****"
hadoop jar javaCode/etape2/wordcount_demo.jar wordcount.WordCountDriver myinput/purchases.txt out4
hadoop fs -get out4/p*
mv par* res4
mv res4 resultat/
hadoop fs -rmr out4
;;

51)
echo "**** JAVA: Liste des ventes par catégorie de produtis ****"
hadoop jar javaCode/etape3/tp1etape3.jar RunClass myinput/purchases.txt out51 1
hadoop fs -get out51/p*
mv par* res51
mv res51 resultat/
hadoop fs -rmr out51
;;

52)
echo "**** PYTHON: Liste des ventes par catégorie de produtis ****"
hs pythonCode/category/mapCat.py pythonCode/category/redCat.py myinput/purchases.txt out52
hadoop fs -get out52/p*
mv par* res52
mv res52 resultat/
hadoop fs -rmr out52
;;

61)
echo "**** JAVA: Liste de la meilleure vente par magasin ****"
hadoop jar javaCode/etape3/tp1etape3.jar RunClass myinput/purchases.txt out61 2
hadoop fs -get out61/p*
mv par* res61
mv res61 resultat/
hadoop fs -rmr out61
;;

62)
echo "**** PYTHON: Liste de la meilleure vente par magasin ****"
hs pythonCode/saleMax/mapSaleMax.py pythonCode/saleMax/redSaleMax.py myinput/purchases.txt out62
hadoop fs -get out62/p*
mv par* res62
mv res62 resultat/
hadoop fs -rmr out62
;;

71)
echo "**** Java: Total ****"
hadoop jar javaCode/etape3/tp1etape3.jar RunClass myinput/purchases.txt out71 3
hadoop fs -get out71/p*
mv par* res71
mv res71 resultat/
hadoop fs -rmr out71
;;

72)
echo "**** PYTHON: Total ****"
hs pythonCode/total/mapTotal.py pythonCode/total/redTotal.py myinput/purchases.txt out72
hadoop fs -get out72/p*
mv par* res72
mv res72 resultat/
hadoop fs -rmr out72
;;
esac









