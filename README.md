## This is a basic script to convert .csv Allen Brain Atlas datasets into .h5ad AnnData format

The script was created following the [Cell Types Database: RNA-Seq Data](https://portal.brain-map.org/atlases-and-data/rnaseq) and using [this](https://knowledge.brain-map.org/data/CCDLINBDBP7KYYBOXOJ/summary) example from the Allen Brain Map data portal ([NeMO archive here](http://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/scell/SSv4/mouse/processed/analysis/SMARTer_cells_MOp/))

## Dependencies

## Usage

```
usage: converter.py [-h] -p PROJECTPATH -o OBSERVATIONSFILE [-c COUNTSFILE] [-a ANNOTATIONSFILE] [-m MEMBERSHIPSFILE] [-t TSNEFILE]

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECTPATH, --projectPath PROJECTPATH
                        Path to the targeted project folder
  -o OBSERVATIONSFILE, --observationsFile OBSERVATIONSFILE
                        Path to the observations file
  -c COUNTSFILE, --countsFile COUNTSFILE
                        Path to the counts file'
  -a ANNOTATIONSFILE, --annotationsFile ANNOTATIONSFILE
                        Path to the annotations file
  -m MEMBERSHIPSFILE, --membershipsFile MEMBERSHIPSFILE
                        Path to the memberships file
  -t TSNEFILE, --tsneFile TSNEFILE
                        Path to the tSNE file'
```

### Sample command

```
python3 converter.py -p /data/AllenBrain_mouseBrainTranscriptomicCellsSmartSeq_25Nov2021 -o /obs.csv.gz -c /exon.counts.csv.gz -a /cluster.annotation.csv -m /cluster.membership.csv
```

## Notes:
Availability of files (observations, counts and etc.) within a certain project can vary from project to project. AnnData .h5ad file is usually created from combination of observations metatable and counts matrix
