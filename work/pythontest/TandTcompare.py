#Bryce EVans
#LAB 5
#Honor Code: ALL work submitted is my own unless otherwise stated
from Bio import SeqIO
#from Bio import Seq

myFilestr = raw_input("Enter File : \n")
data_str = open(myFile_str)
data_str.close()
myFile_str2 = raw_input("Enter next File: \n")
data_str2 = open(myFile_str2)
data_str2.close()
#compare dna sequences
def compare_DNA(string1, string2):
    count = 0
    print "Comparing DNA"
#if characters are different print out each characters from each sequence and add to counter
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
            count = count +1
            print "Different at place", i
            print "Sequence 1", string1[i]
            print "Sequence 2", string2[i]
#number of differences
    print "Number of differences", count
    print "\n"
#compare the rna sequences
def compare_RNA(string1, string2):
    count = 0
    print "Comparing RNA"
#if characters are different print out each characters from each sequence and add to counter
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
            count = count +1
            print "Different at place", i
            print "Sequence 1", string1[i]
            print "Sequence 2", string2[i]
#number of differences
    print "Number of differences", count
    print"\n"
#compare protein sequences
def compare_Pro(string1, string2):
    count = 0
    print "Comparing Proteins"
    #if characters are different print out each characters from each sequence and add to counter
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
            count = count +1
            print "Different at place", i
            print "Sequence 1", string1[i]
            print "Sequence 2", string2[i]
#number of differences
    print "Number of differences", count
    print "\n"

#save the string sequence as seq
print 'file name:', myFile_str
for record in SeqIO.parse(myFile_str, 'fasta'):
	ide = record.id
	seq = record.seq
	print 'Name: ', ide
	print 'Size: ', len(seq)
	print 'Base Counter:'
	print "\n"
#used from lab 4
#save the second string sequence as seq2
print 'file name:', myFile_str2
for record in SeqIO.parse(myFile_str2, 'fasta'):
	ide = record.id
	seq2 = record.seq
	print 'Name: ', ide
	print 'Size: ', len(seq)
	print 'Base Counter:'
	print "\n"
#used from lab4

#convert dna to rna
rna1 = seq.transcribe()
rna2 = seq2.transcribe()
#convert dna to protein
pro1 = seq.translate()
pro2 = seq2.translate()
#compare each type of string to the other
compare_DNA(seq, seq2)
compare_RNA(rna1, rna2)
compare_Pro(pro1, pro2)

#print "DNA1", seq
#print "DNA2", seq2
#print "RNA1", rna1
#print "RNA2", rna2
#print "Pro1", pro1
#print "Pro2", pro2
