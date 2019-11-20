GENES = ["SDHB", "MEN1", "KCNH2", "MSH2", "MYL2", "BRCA2"]
TISSUES = ["Brain", "Heart", "Blood", "Skin"]

rule all:
    input:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'

rule get_tissue_samples:
    input:
        'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    output:
        expand('{ts}_samples.txt', ts=TISSUES)
    shell:
        'for TS in {TISSUES}; do ' \
        + 'python get_tissue_samples.py --out_file $TS\_samples.txt --group_type $TS --sample_attributes {input};' \
        + 'done'

rule get_gene_counts:
    input:
        'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
    output:
        expand('{gs}_counts.txt', gs=GENES)
    shell:
        'for GS in {GENES}; do ' \
        + 'python get_gene_counts.py --out_file $GS\_counts.txt --gene $GS --gene_reads {input}; ' \
        + 'done'

rule box:
    input:
        rules.get_tissue_samples.output,
        rules.get_gene_counts.output
    output:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'
    shell:
        'python box.py --out_file {output} --genes \"{GENES}\" --tissues \"{TISSUES}\" --tissues {TISSUE_GROUP}_samples.txt'
