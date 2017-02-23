## Wrangling text data from GeoDeepDive

This Python script is a simplified component of the data-mining application utilized in [Peters, Husson and Wilcots (in press, Geology)](https://github.com/UW-Macrostrat/stromatolites_demo), which utilizes the [GeoDeepDive](https://geodeepdive.org) digital library to constrain the spatio-temporal distribution of stromatolite fossils across Earth history. The script searches for user-define word(s) or phrases in 5 provided USGS Technical Reports that have been processed and annotated by GeoDeepDive. The output is a list of `document-sentence` tuples that uniquely describe the location of the specific word(s) within the GeoDeepDive library, along with any adjectives that are used to describe those word(s). It serves as a demonstration of what data derived from GeoDeepDive looks like, and how it can be manipulated in simple ways to gain knowledge about the published literature.

### Exercise
Using the provided Python script and some coding of your own, create a list of `document-sentence` tuples for sentences in this test set that contain BOTH `sandstone` and `limestone,` two commonly studied rock types.
