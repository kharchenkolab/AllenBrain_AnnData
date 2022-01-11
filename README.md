## This is instructions on how to convert .csv Allen Brain Atlas data into .h5ad AnnData format

We have converted some *csv* files into *h5ad* format.

We worked with https://portal.brain-map.org/atlases-and-data/rnaseq and nemoarchives like https://knowledge.brain-map.org/data/CCDLINBDBP7KYYBOXOJ/summary (http://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/scell/SSv4/mouse/processed/analysis/SMARTer_cells_MOp/)

## Example command
```python converter.py -p/data/AllenBrain_mouseBrainTranscriptomicCellsSmartSeq_25Nov2021 -o/obs.csv.gz -c/exon.counts.csv.gz -a/cluster.annotation.csv -m/cluster.membership.csv```

## Notes:
existence of folders files can change from project to project 
