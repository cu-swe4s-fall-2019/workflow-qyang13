python get_tissue_samples.py --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
 --out_file Blood_samples.txt\
 --group_type Blood

python get_tissue_samples.py --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
 --out_file Brain_samples.txt\
 --group_type Brain

python get_tissue_samples.py --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
 --out_file Heart_samples.txt\
 --group_type Heart

 python get_tissue_samples.py --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt\
  --out_file Skin_samples.txt\
  --group_type Skin

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file SDHB_counts.txt\
 --gene SDHB

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file MEN1_counts.txt\
 --gene MEN1

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file KCNH2_counts.txt\
 --gene KCNH2

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file MSH2_counts.txt\
 --gene MSH2

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file MYL2_counts.txt\
 --gene MYL2

python get_gene_counts.py\
 --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz\
 --out_file BRCA2_counts.txt\
 --gene BRCA2

python box.py\
 --out_file Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png\
 --genes SDHB MEN1 KCNH2 MSH2 MYL2 BRCA2\
 --tissues Brain Heart Blood Skin
