import os
import sys
import argparse as ap


def linear_search(key, L):
    '''Linear search to find the key in a list'''
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
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

    parser.add_argument('-a',
                        '--sample_attributes',
                        type=str,
                        help="Input meta data filename",
                        required=False)

    parser.add_argument('-t',
                        '--group_type',
                        type=str,
                        help="Group type: SMTS or SMTSD",
                        required=False)

    return parser.parse_args()


def main():
    args = parse_args()
    meta_data_file_name = args.sample_attributes
    target_type = args.group_type
    out_file_name = args.out_file

    if (not os.path.exists(meta_data_file_name)):
        print('Cannot find metadata file')
        sys.exit(1)

    SAMPID = []
    SMTS = []
    metadata_header = None
    tissue_group = []

    categoraized_ids = []
    sample_info = None

    # Processing the meta data file
    output = open(out_file_name, 'w')
    for l in open(meta_data_file_name):
        # Store the first row i.e. header in a separate array
        if metadata_header is None:
            metadata_header = l.rstrip().split("\t")
            SAMPID_idx = linear_search("SAMPID", metadata_header)
            if SAMPID_idx == -1:
                print('The column with sample ids does not exist!')
                sys.exit(1)
            SMTS_idx = linear_search(target_type, metadata_header)
            if SMTS_idx == -1:
                print('The column with tissue group does not exist!')
                sys.exit(1)

        else:
            # Split lines by tab and stored them in array
            # rstrip() returns a copy of the string
            # with trailing characters removed
            sample_info = l.rstrip().split("\t")
            sample_id = sample_info[SAMPID_idx]
            tissue_type = sample_info[SMTS_idx]
            output.write(sample_id+'\t'+tissue_type+'\n')
    output.close()
    print(out_file_name + ' generated successfully!')


if __name__ == '__main__':
    main()
