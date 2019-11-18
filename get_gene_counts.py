import os
import sys
import argparse as ap
import gzip


def binary_search(key, D):
    '''Binary search to find the key in a SORTED list'''
    lo = -1
    hi = len(D)
    while(hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if(key < D[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


def parse_args():
    '''    Argument Parser    '''
    parser = ap.ArgumentParser(description="correct way to parse",
                               prog='Plot GTEX')

    parser.add_argument('-o',
                        '--out_file',
                        type=str,
                        help="Output filename",
                        required=False)

    parser.add_argument('-c',
                        '--gene_reads',
                        type=str,
                        help="Input read counts filename",
                        required=False)

    parser.add_argument('-g',
                        '--gene',
                        type=str,
                        help="Enter a gene name",
                        required=False)

    return parser.parse_args()


def main():
    args = parse_args()
    rna_data_file_name = args.gene_reads
    target_gene_name = args.gene
    out_file_name = args.out_file

    version = None
    dim = None
    rna_header = None
    rna_counts = None
    found = False
    output = open(out_file_name, 'w')

    if (not os.path.exists(rna_data_file_name)):
        print('Cannot find read count file')
        sys.exit(1)
    # Processing the count file
    # use gzip.open to read gzip file
    for l in gzip.open(rna_data_file_name, "rt"):
        # Assume first line stores the version
        if version is None:
            version = l
            continue
        # Assume second line stores the dimension
        if dim is None:
            dim = l
            continue
        # Assume thrid line stores the header for counts
        if rna_header is None:
            rna_header = l.rstrip().split("\t")
            # Use tuple to store the original index
            # and then sort based on the first element in tuple
            rna_header_index = []
            for i in range(len(rna_header)):
                rna_header_index.append([rna_header[i], i])
            rna_header_index.sort(key=lambda pair: pair[0])
            Description_idx = binary_search("Description",
                                            rna_header_index)
            if Description_idx == -1:
                sys.exit('Description not found in header.')
                sys.exit(1)

        else:
            rna_counts = l.rstrip().split("\t")
            if rna_counts[Description_idx] == target_gene_name:
                found = True
                for i in range(Description_idx+1, len(rna_counts)-1):
                    output.write(rna_header[i]+'\t'+rna_counts[i]+'\n')
                output.close()
                print(out_file_name + ' generated sucessfully.')
                break

    if found is not True:
        print('Unable to find read counts for specified gene: '
              + target_gene_name)
        sys.exit(1)


if __name__ == '__main__':
    main()
