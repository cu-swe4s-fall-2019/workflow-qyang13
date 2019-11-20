 #!/bin/bash

 test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
 . ssshtest

 run unit_tests python test_get_gene_counts.py
 assert_exit_code 0

 run test_grouptype_not_found python get_tissue_samples.py\
  --out_file test.txt\
  --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
  --group_type NOTEXIST
 assert_exit_code 1
 assert_in_stdout "Specified tissue type does not exist"

 run test_file_not_found python get_tissue_samples.py\
  --out_file test.txt\
  --sample_attributes NOTEXIST.txt\
  --group_type Blood
 assert_exit_code 1
 assert_in_stdout "Cannot find metadata file"

 run test_normal python get_tissue_samples.py\
  --out_file test.txt\
  --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
  --group_type Blood
 assert_in_stdout "generated successfully"
 assert_exit_code 0

 run test_normal_file_exist test -e test.txt
 assert_exit_code 0

 rm test.txt ssshtest
