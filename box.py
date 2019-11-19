import os
import sys
import argparse as ap
import gzip
import matplotlib
import matplotlib.pyplot as plt
import importlib
matplotlib.use('Agg')

def linear_search(key, L):
    '''Linear search to find the key in a list'''
    hit = -1
    for i in range(len(L)):
        curr = L[i][0]
        if key == curr:
            return  int(L[i][1])
    return -1

def boxplot(meta, counts, tissue_labs, gene_labs, outfile):
    '''
    Given a numerical array, make a box plot and save as png file
    '''
    width = len(gene_labs) + 2
    height = len(tissue_labs) * 3 + 10
    plot_num = len(tissue_labs) * 100 + 11
    fig = plt.figure(figsize=(width, height), dpi=300)
    i = -1
    # For each tissue type, return the list of SAMPID
    for tissue_type in meta:
        i += 1
        L = []
        j = -1
        # For each gene in counts
        for gene in counts:
            j += 1
            L.append([])
            # Use the sample ID and return counts for that gene and tissue type
            for id in tissue_type:
                count = linear_search(id[0], gene)
                if count != -1:
                    L[j].append(count)
        ax = fig.add_subplot(plot_num+i)
        ax.boxplot(L)
        ax.set_xticklabels(gene_labs, rotation=90)
        ax.set_ylabel("Gene read counts")
        ax.set_title(tissue_labs[i])

    plt.savefig(outfile, bbox_inches='tight')
    plt.close()
    return 0


def parse_args():
    '''    Argument Parser    '''
    parser = ap.ArgumentParser(description="correct way to parse",
                               prog='box plot')

    parser.add_argument('-o',
                        '--out_file',
                        type=str,
                        help="Output filename",
                        required=True)

    parser.add_argument('-t',
                        '--tissues',
                        type=str,
                        nargs='+',
                        help="Enter one or more tissues",
                        required=True)

    parser.add_argument('-g',
                        '--genes',
                        type=str,
                        nargs='+',
                        help="Enter one or more gene name",
                        required=True)

    return parser.parse_args()


def main():
    args = parse_args()
    target_genes = args.genes
    target_tissues = args.tissues
    outfile_name = args.out_file

    categoraized_ids = []
    i = -1
    for t in target_tissues:
        if not os.path.exists(t + '_samples.txt'):
            print(t + '_samples.txt does not exist. Skipping.')
            continue
        else:
            i += 1
            categoraized_ids.append([])
            for l in open(t + '_samples.txt'):
                l = l.rstrip().split("\n")
                categoraized_ids[i].append(l)
    # categoraized_ids is a 2-D array
    # 1D: Tissue type
    # 2D: SAMPID
    # print(categoraized_ids[0][1])

    counts = []
    j = -1

    for t in target_genes:
        if not os.path.exists(t + '_counts.txt'):
            print(t + '_counts.txt does not exist. Skipping.')
            continue
        else:
            j += 1
            counts.append([])
            # For each sample id + gene counts
            for l in open(t + '_counts.txt'):
                l = l.rstrip().split("\t")
                counts[j].append(l)
    # Counts is a 3-D array
    # 1D: Gene names
    # 2D: Sample ID and counts
    # 3D: 0:Sample id 1:counts
    # print(counts[0][1][0])

    boxplot(categoraized_ids, counts,
            target_tissues, target_genes, outfile_name)


if __name__ == '__main__':
    main()
