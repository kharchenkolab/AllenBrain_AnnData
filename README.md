# Instructions on how to convert Allen Brain Atlas .csv data into AnnData files
python test.py -p/data/AllenBrain_mouseBrainTranscriptomicCellsSmartSeq_25Nov2021 -o/obs.csv.gz -c/exon.counts.csv.gz -a/cluster.annotation.csv -m/cluster.membership.csv

We have converted some *csv* files into *h5ad* format.

We worked with https://portal.brain-map.org/atlases-and-data/rnaseq

You can follow these instructions to convert csv to h5ad
https://knowledge.brain-map.org/data/CCDLINBDBP7KYYBOXOJ/summary

http://data.nemoarchive.org/biccn/grant/u19_zeng/zeng/transcriptome/scell/SSv4/mouse/processed/analysis/SMARTer_cells_MOp/

Structure is different from project to project.
