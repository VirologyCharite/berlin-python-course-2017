
# for i in [0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9].fasta
# for i in *.fasta
# for i in *-*.fasta

for i in ????-????.fasta
do
    base=$(echo $i | cut -f1 -d.)
    newfile=$base.sequence-count
    grep -c '^>' $i > $newfile
done
