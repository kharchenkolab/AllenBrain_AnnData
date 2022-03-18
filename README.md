## This is a basic script to convert .csv Allen Brain Atlas datasets into .h5ad AnnData format

The script was created following the [Cell Types Database: RNA-Seq Data](https://portal.brain-map.org/atlases-and-data/rnaseq) and using [this](https://knowledge.brain-map.org/data/CCDLINBDBP7KYYBOXOJ/summary) example from the Allen Brain Map data portal ([NeMO archive here](http://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/scell/SSv4/mouse/processed/analysis/SMARTer_cells_MOp/))

## Dependencies

## Usage

```
required arguments:
  -h, --help            show this help message and exit
  -p PROJECTFOLDER, --projectFolder PROJECTFOLDER
                        Path to the targeted project folder
  -m METADATAFILE, --metadataFile METADATAFILE
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
  -e MEMBERSHIPSFILE, --membershipsFile MEMBERSHIPSFILE
                        Path to the memberships file
  -t TSNEFILE, --tsneFile TSNEFILE
                        Path to the tSNE file'
  -f TRIMMEDMEANSFILE, --trimmedMeansFile TRIMMEDMEANSFILE
                        Path to the trimmed means file'                        
```

### Steps to generate .h5ad file
1. Clone the repository
2. Create a project folder in the data folder
3. Download necessary files in the project folder
4. Run the script "converter.py" with the files full names as arguments. Example below:

```
python3 converter.py -p /data/AllenBrain_mouseBrainTranscriptomicCellsSmartSeq_25Nov2021 -o /obs.csv.gz -c /exon.counts.csv.gz -a /cluster.annotation.csv -m /cluster.membership.csv
```

## Notes:
Availability of files (observations, counts and etc.) within a certain project can vary from project to project. AnnData .h5ad file is usually created from combination of observations metatable and counts matrix
