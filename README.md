## This is a basic script to convert certain .csv Allen Brain Atlas projects into .h5ad AnnData format

## Dependencies installation
Run the following from the root folder
```
pip install -r requirements.txt
```
## Usage

```
usage: python3 converter.py [-h] -p/PROJECTFOLDER -o/METADATAFILE -c/COUNTSFILE -a/CLUSTERFILE -m/MEMBERSHIPSFILE -t/TSNEFILE

  -h, --help            show this help message and exit
required arguments:
  -p PROJECTFOLDER, --projectFolder PROJECTFOLDER
                        Path to the targeted project folder
  -o METADATAFILE, --metadataFile METADATAFILE
                        Path to the observations file
optional arguments:                   
  -c COUNTSFILE, --countsFile COUNTSFILE
                        Path to the counts file'
  -e EXONCOUNTSFILE, --exonCountsFile exonCountsFile
                        Path to the exon counts file'
  -i INTRONCOUNTSFILE, --intronCountsFile intronCountsFile
                        Path to the intron counts file'                        
  -a CLUSTERFILE, --clusterFile CLUSTERFILE
                        Path to the cluster annotations file
  -m MEMBERSHIPSFILE, --membershipsFile MEMBERSHIPSFILE
                        Path to the memberships file
  -t TSNEFILE, --tsneFile TSNEFILE
                        Path to the tSNE file'
  -f TRIMMEDMEANSFILE, --trimmedMeansFile TRIMMEDMEANSFILE
                        Path to the trimmed means file'                        
```

### Steps to generate .h5ad file
1. Clone the repository
2. Create a project folder of interest in a folder called "data" 
3. Download necessary files in the project folder
4. From the root repository folder run the script "converter.py" with the files full names as arguments

For a project example [Human Multiple Cortical Areas SMART-seq](https://portal.brain-map.org/atlases-and-data/rnaseq/human-multiple-cortical-areas-smart-seq) we used the following command:
```
python3 converter.py -p/AllenBrain_humanMultipleCorticalAreas_09Nov2021 -o/metadata.csv -c/matrix.csv -t/tsne.csv -f/trimmed_means.csv
```

For a project example [Transcriptomic cell types in the mouse brain: SMART-seq cells](http://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/sncell/SSv4/mouse/processed/analysis/SMARTer_nuclei_MOp/) we used the following command:
```
python3 converter.py -p/AllenBrain_mouseBrainTranscriptomicCellsSmartSeqNuclei_25Nov2021 -o/sample_metadata.csv.gz -e/exon.counts.csv.gz -i/intron.counts.csv.gz -a/cluster.annotation.csv -m/cluster.membership.csv -t/tsne.df.csv 
```

# IMPORTANT NOTES:
Availability and format of files (metadata, counts matrices and etc.) within a certain project can vary from project to project dramatically. The particular script given here is applicable to files of .csv formats, with examples presented above. Having metadata and counts matrix (whether common or exon or intron count matrices) included is mandatory to generate .h5ad file
