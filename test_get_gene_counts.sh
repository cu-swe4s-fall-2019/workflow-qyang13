#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run unit_tests python test_get_gene_counts.py
assert_exit_code 0

run test_gene_not_found python get_gene_counts.py\
 --out_file SDHB.txt\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --gene doesnt_Exist
assert_exit_code 1
assert_in_stdout "Unable to find read counts for specified gene"

run test_file_not_found python get_gene_counts.py\
 --out_file SDHB.txt\
 --gene_reads doesnt_Exist\
 --gene SDHB
assert_exit_code 1
assert_in_stdout "Cannot find read count file"

run test_normal python get_gene_counts.py\
 --out_file SDHB.txt\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --gene SDHB
assert_in_stdout "enerated sucessfully."
assert_exit_code 0

run test_normal_file_exist test -e SDHB.txt
assert_exit_code 0

rm SDHB.txt ssshtest
