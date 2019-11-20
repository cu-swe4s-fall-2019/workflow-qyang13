#!/bin/bash
echo generating necessary data files for testing ...
python get_tissue_samples.py --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
 --out_file Blood_samples.txt\
 --group_type Blood

python get_tissue_samples.py --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
 --out_file Brain_samples.txt\
 --group_type Brain

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file SDHB_counts.txt\
 --gene SDHB

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file MEN1_counts.txt\
 --gene MEN1

rm *.png
test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_box python box.py\
 --out_file test.png\
 --genes SDHB MEN1\
 --tissues Brain Blood
assert_exit_code 0
assert_no_stdout

test -e test.png
assert_exit_code 0

rm ssshtest *_samples.txt *_counts.txt
