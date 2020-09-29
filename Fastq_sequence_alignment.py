import os

os.chdir('/home/rjing/Desktop/sambamdata')

#val = os.system('ls -al')
#print(val)

#put reference sequence and fastq dataset into the directory(sambamdata)

#1. create index for the reference sequence
os.chdir('/home/rjing/Desktop/bwa-master')
#val = os.system('ls -al')
#print(val)
os.system('bwa index "/home/rjing/Desktop/sambamdata/TCXpress_pLVX-EF1a-4110A_miHA1_Correct.fa"')

#2. Using mem algorithm to process the alignment
os.chdir('/home/rjing/Desktop/bwa-master')
os.system("bwa mem '/home/rjing/Desktop/sambamdata/TCXpress_pLVX-EF1a-4110A_miHA1_Correct.fa' '/home/rjing/Desktop/sambamdata/1_R1.fastq' '/home/rjing/Desktop/sambamdata/1_R2.fastq'>aln-seq1.sam")
#os.system("bwa mem '/home/rjing/Desktop/sambamdata/TCXpress_pLVX-EF1a-4110A_miHA1_Correct.fa' '/home/rjing/Desktop/sambamdata/' '/home/rjing/Desktop/sambamdata/'>")

#3. convert sam file to a bam file
os.system("mv aln-seq1.sam /home/rjing/Desktop/sambamdata/")
os.system("samtools view -bS '/home/rjing/Desktop/sambamdata/aln-seq1.sam' > aln-seq1.bam")

#4. sort the bam file
os.system("mv /home/rjing/Desktop/bwa-master/aln-seq1.bam /home/rjing/Desktop/sambamdata/")
os.system("samtools sort /home/rjing/Desktop/sambamdata/aln-seq1.bam > aln-seq1_sort.bam")

#5. create index for the sorted bam files
os.system("mv /home/rjing/Desktop/bwa-master/aln-seq1_sort.bam /home/rjing/Desktop/sambamdata/")
os.system("samtools index '/home/rjing/Desktop/sambamdata/aln-seq1_sort.bam' > aln-seq1_sort.bam.bai")
