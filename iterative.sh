#!/bin/sh
CONVERGE=1
ITER=1
rm v v1 log*

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /Assignment-2/output/task-* 

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
-mapper "'/home/pes1ug19cs563/Documents/Big-Data/Assignment-2/T1/mapper.py'" \
-reducer "'/home/pes1ug19cs563/Documents/Big-Data/Assignment-2/T1/reducer.py' 'home/pes1ug19cs563/Documents/Big-Data/Assignment-2/T1/v.txt" \
-input /Assignment-2/Input/dataset-sample.txt \
-output /Assignment-2/output/task-1-output

while [ "$CONVERGE" -ne 0 ]
do
	echo "############################# ITERATION $ITER #############################"
	hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar \
	-mapper "'/home/pes_bigdata/Desktop/Assignment-2/mapper_t2.py' '/home/pes_bigdata/Desktop/Assignment-2/v' '/home/pes_bigdata/Desktop/Assignment-2/Input/node-map-sample.json'" \
	-reducer "'/home/pes_bigdata/Desktop/Assignment-2/reducer_t2.py'" \
	-input /Assignment-2/output/task-1-output/part-00000 \
	-output /Assignment-2/output/task-2-output
	touch v1
	hadoop fs -cat /Assignment-2/output/task-2-output/part-00000 > "/home/pes_bigdata/Desktop/Assignment-2/v1"
	CONVERGE=$(python3 check_conv.py $ITER>&1)
	ITER=$((ITER+1))
	hdfs dfs -rm -r /Assignment-2/output/task-2-output/
	echo $CONVERGE
done

# to run the scripts without hadoop
# run the following commands inside `/Assignment-2`


#  ------------------------------
# cat T1/dataset_1percent.txt | python3 T1/mapper.py | sort -k 1,1 | python3 T1/reducer.py v > temp.txt
# echo "T1 done"
# CONVERGE=1
# ITER=1

# while [ "$CONVERGE" -ne 0 ]
# do
# 	cat temp.txt | python3 T2/mapper.py v T2/embedding_1percent.json| sort -k 1,1 | python3 T2/reducer.py > v1
# 	echo "############################# ITERATION $ITER #############################"
# 	CONVERGE=$(python3 check_conv.py $ITER>&1)
# 	ITER=$((ITER+1))
# 	echo "$CONVERGE
# done
# echo "T2 done"
# rm v v1 log*
#  -------------------------------