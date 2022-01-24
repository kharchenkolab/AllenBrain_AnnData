#!/usr/bin/env python3

import anndata
import argparse
import numpy as np
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--projectPath", action='store', dest='projectPath',
                    help="Path to the targeted project folder", required=True)

parser.add_argument("-o", "--observationsFile", action='store', dest='observationsFile',
                    help="Path to the observations file", required=True)

parser.add_argument("-c", "--countsFile", action='store', dest='countsFile',
                    help="Path to the counts file'")

parser.add_argument("-a", "--annotationsFile", action='store', dest='annotationsFile',
                    help="Path to the annotations file")

parser.add_argument("-m", "--membershipsFile", action='store', dest='membershipsFile',
                    help="Path to the memberships file")

parser.add_argument("-t", "--tsneFile", action='store', dest='tsneFile',
                    help="Path to the tSNE file'")

args = parser.parse_args()

path = args.projectPath.lstrip('/')


# cells observations metadata
try:
    obs = pd.read_csv(path + args.observationsFile, index_col='sample_name')
    print('read ', path + args.observationsFile)
except:
    print('Check "observationsFile" or type in right index name')

# clusters memberships table
if args.membershipsFile is not None:
  try:
      print('read ', path + args.membershipsFile)
      memb = pd.read_csv(path + args.membershipsFile)
      obs = obs.merge(memb, on='Unnamed: 0', how='left')
  except:
      print('type in right joining column between observations and memberships')
else:
  print('Note: There is no memberships file specified with "membershipsFile"')

# cluster annotations table
if args.annotationsFile is not None:
  try:
      print('read ', path + args.annotationsFile)
      annot = pd.read_csv(path + args.annotationsFile)
      annot.rename(columns={'cluster_id': 'x'}, inplace=True)
  except:
      print('type in right column name as index in annotations')
else:
  print('Note: There is no annotationss file specified with "annotationsFile"')
  

# merge obs with annot
## note: annot variable must exist
try:
    obs = obs.merge(annot, on='x', how='left')
    obs.rename(columns={'Unnamed: 0' :'cluster_id'}, inplace=True)
    obs.set_index('cluster_id', inplace=True)
except:
    print('Rename joining column between observations and annotations to a common notation')


# counts matrix
if args.countsFile is not None:
  try:
      print('read ', path + args.countsFile)
      counts = pd.read_csv(path + args.countsFile, index_col=0).T
  except:
      print('Check if a right column name was set as index in counts file')
else:
  counts = None
  print('Note: There is no counts file specified with "countsFile"')

# create anndata file
if counts is not None:
    adata = anndata.AnnData(counts, obs)
else:
    adata = anndata.AnnData(obs)

print('Creating anndata file ...')
adata.write(path + '/Input.h5ad')
print('Successfully created anndata file. Done.')
