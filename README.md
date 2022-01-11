## This is a basic script to convert .csv Allen Brain Atlas datasets into .h5ad AnnData format

The script was created accordingly with https://portal.brain-map.org/atlases-and-data/rnaseq and some nemo archives like https://knowledge.brain-map.org/data/CCDLINBDBP7KYYBOXOJ/summary (http://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/scell/SSv4/mouse/processed/analysis/SMARTer_cells_MOp/)

## Sample command
```python converter.py -p/data/AllenBrain_mouseBrainTranscriptomicCellsSmartSeq_25Nov2021 -o/obs.csv.gz -c/exon.counts.csv.gz -a/cluster.annotation.csv -m/cluster.membership.csv```

## Notes:
Availability of files (observations, counts and etc.) within a certain project can vary from project to project. AnnData .h5ad file is usually created from combination of observations metatable and counts matrix
