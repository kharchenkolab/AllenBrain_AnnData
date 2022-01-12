import anndata
import argparse
import numpy as np
import os
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--projectPath", action='store', dest='projectPath',
                    help="type in the path of the targeted project folder", required=True)

parser.add_argument("-o", "--observationsFile", action='store', dest='observationsFile',
                    help="type in observations file name", required=True)

parser.add_argument("-c", "--countsFile", action='store', dest='countsFile',
                    help="type in counts file name'")

parser.add_argument("-a", "--annotationsFile", action='store', dest='annotationsFile',
                    help="type in annotations file name")

parser.add_argument("-m", "--membershipsFile", action='store', dest='membershipsFile',
                    help="type in memberships file name'")

parser.add_argument("-t", "--tsneFile", action='store', dest='tsneFile',
                    help="type in tsne file name'")

args = parser.parse_args()

path = args.projectPath.lstrip('/')

# cells observations metadata
try:
    obs = pd.read_csv(path + args.observationsFile, index_col='sample_name')
    print('read ', path + args.observationsFile)
except:
    print('Check observations file or type in right index name')

# clusters memberships table
try:
  print(args.membershipsFile)
  try:
      print('read ', path + args.membershipsFile)
      memb = pd.read_csv(path + args.membershipsFile)
      obs = obs.merge(memb, on='Unnamed: 0', how='left')
  except:
      print('type in right joining column between observations and memberships')
except:
  print('no memberships file')

# cluster annotations table
try:
  print(args.annotationsFile)
  try:
      print('read ', path + args.annotationsFile)
      annot = pd.read_csv(path + args.annotationsFile)
      annot.rename(columns={'cluster_id': 'x'}, inplace=True)
  except:
      print('type in right column name as index')
except:
  print('There is no annotations file')
  

# merge obs with annot
try:
  print(annot)
  try:
      obs = obs.merge(annot, on='x', how='left')
      obs.rename(columns={'Unnamed: 0' :'cluster_id'}, inplace=True)
      obs.set_index('cluster_id', inplace=True)
  except:
      print('Rename joining column between observations and annotations to a common notation')
except:
  print('there is no annot variable')

# counts matrix
try:
  print(args.countsFile)
  try:
      print('read ', path + args.countsFile)
      counts = pd.read_csv(path + args.countsFile, index_col=0).T
  except:
      print('Check if a right column name was set as index')
except:
  print('there is no annotation file')

# create anndata file
try:
    adata = anndata.AnnData(counts, obs)
except:
    adata = anndata.AnnData(obs)

print('Creating anndata file ...')
adata.write(path + '/Input.h5ad')
print('Created  anndata file')
