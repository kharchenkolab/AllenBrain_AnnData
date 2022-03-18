# #!/usr/bin/env python3
# ## Date: March 18, 2022
# ## Version: 0.1.3

import anndata as ad
import argparse
import numpy as np
import os
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--projectFolder", action='store', dest='projectFolder',
                    help="enter AllenBrain project name", required=True)

parser.add_argument("-o", "--metadataFile", action='store', dest='metadataFile',
                    help="Enter metadata file name", required=True)

parser.add_argument("-c", "--countsFile", action='store', dest='countsFile',
                    help="Counts file")

parser.add_argument("-e", "--exonCountsFile", action='store', dest='exonCountsFile',
                    help="Exon counts file")

parser.add_argument("-i", "--intronCountsFile", action='store', dest='intronCountsFile',
                    help="Intron counts file")

parser.add_argument("-a", "--clusterFile", action='store', dest='clusterFile',
                    help="Cluster annotations file")

parser.add_argument("-m", "--membershipsFile", action='store', dest='membershipsFile',
                    help="Memberships file")

parser.add_argument("-t", "--tsneFile", action='store', dest='tsneFile',
                    help="tSNE file")

parser.add_argument("-f", "--trimmedMeansFile", action='store', dest='trimmedMeansFile',
                    help="Trimmed means file")

args = parser.parse_args()
path = 'data' + args.projectFolder

metadata = pd.read_csv(path + args.metadataFile)

if 'external_donor_name_label' in metadata.columns:
    metadata['external_donor_name_label'] = metadata['external_donor_name_label'].astype(str)

# cells observations metadata
if args.exonCountsFile is not None or args.intronCountsFile is not None:
    if 'sample_name' in metadata.columns:
        metadata.rename(columns={'sample_name': 'id'}, inplace=True)
        if 'Unnamed: 0' in metadata.columns:
            metadata.rename(columns={'Unnamed: 0': 'sample_name'}, inplace=True)

print(metadata.columns)

# cluster memberships table
if args.membershipsFile is not None:
    memb = pd.read_csv(path + args.membershipsFile)
    memb.rename(columns={'Unnamed: 0': 'sample_name'}, inplace=True)
    # merge metadata with cluster memberships
    metadata = metadata.merge(memb, on='sample_name', how='left')

# cluster annotations table
if args.clusterFile is not None:
    cluster = pd.read_csv(path + args.clusterFile)
    cluster.rename(columns={'cluster_id': 'x'}, inplace=True)
    # merge metadata with cluster annotations
    metadata = metadata.merge(cluster, on='x', how='left')

# tSNE
if args.tsneFile is not None:
    tsne = pd.read_csv(path + args.tsneFile)
    if 'Unnamed: 0' in tsne.columns:
        tsne.rename(columns={'Unnamed: 0': 'sample_name'}, inplace=True)
    print(tsne.columns)
    metadata = tsne.merge(metadata, on='sample_name', how='left')
    # merge metadata with tsne
    tsne.set_index('sample_name', inplace=True)

# features
if args.trimmedMeansFile is not None:
    features = pd.read_csv(path + args.trimmedMeansFile)

if 'sample_name' in metadata.columns:
    metadata.set_index('sample_name', inplace=True)
metadata.dropna(axis=1, inplace=True)

# exon counts matrix
if args.exonCountsFile is not None:
    exonCounts = pd.read_csv(path + args.exonCountsFile, index_col=0).T
    exonCounts = exonCounts[exonCounts.index.isin(metadata.index)]
    if 'features' in globals():
        adata = ad.AnnData(X=exonCounts, obs=metadata, var=features)
    else:
        adata = ad.AnnData(X=exonCounts, obs=metadata)
    if 'tsne' in globals():
        adata.obsm['X_tsne'] = np.array(tsne)
    output_name = path + '/exonInput.h5ad'
    print(f"Generating {output_name} ...")
    if os.path.exists(output_name):
        os.remove(output_name)
    adata.write(filename=output_name, compression="gzip")
    print(f"Completed generating {output_name}!")

# intron counts matrix
if args.intronCountsFile is not None:
    intronCounts = pd.read_csv(path + args.intronCountsFile, index_col=0).T
    intronCounts = intronCounts[intronCounts.index.isin(metadata.index)]
    if 'features' in globals():
        adata = ad.AnnData(X=intronCounts, obs=metadata, var=features)
    else:
        adata = ad.AnnData(X=intronCounts, obs=metadata)
    if 'tsne' in globals():
        adata.obsm['X_tsne'] = np.array(tsne)
    output_name = path + '/intronInput.h5ad'
    print(f"Generating {output_name} ...")
    if os.path.exists(output_name):
        os.remove(output_name)
    adata.write(filename=output_name, compression="gzip")
    print(f"Completed generating {output_name}!")

# common counts matrix
if args.countsFile is not None:
    counts = pd.read_csv(path + args.countsFile, index_col=0).T
    counts = counts[counts.index.isin(metadata.index)]
    if 'features' in globals():
        adata = ad.AnnData(X=counts, obs=metadata, var=features)
    else:
        adata = ad.AnnData(X=counts, obs=metadata)
    if 'tsne' in globals():
        adata.obsm['X_tsne'] = np.array(tsne)
    output_name = path + '/Input.h5ad'
    print(f"Generating {output_name} ...")
    if os.path.exists(output_name):
        os.remove(output_name)
    adata.write(filename=output_name, compression="gzip")
    print(f"Completed generating {output_name}!")



