## Wrangling text data from GeoDeepDive

The Python script `find_target.py` is a simplified component of the data-mining application utilized in [Peters, Husson and Wilcots (in press, Geology)](https://github.com/UW-Macrostrat/stromatolites_demo), which utilizes the [GeoDeepDive](https://geodeepdive.org) digital library to constrain the spatio-temporal distribution of stromatolite fossils across Earth history. This script searches for user-defined word(s) or phrases in 5 provided USGS Technical Reports that have been processed and annotated by GeoDeepDive. The output is a list of `document-sentence` tuples that uniquely describe the location of the specified word(s) within the GeoDeepDive library, along with any adjectives that are used to describe those word(s). It serves as a demonstration of what data derived from GeoDeepDive looks like, and how it can be manipulated in simple ways to gain knowledge about the published literature.

## Getting started

Download or clone this repo. The only dependency is Python and its standard modules.

## Input description

Input for `find_target.py` are two text files: `input/sentences_nlp352` and `var/target_variables.txt`. The `sentences_nlp352` file comes from the GeoDeepDive library, and is a TSV file containing 5 technical reports from the United States Geological Survey that have been parsed using [Stanford Natural Language Processing](http://nlp.stanford.edu/) (version 3.5.2). More detailed information about the sentences table data structure can be found [here](https://github.com/jonhusson/gdd_demo/tree/master/input). You can also view a reference list describing the five included reports [here](https://github.com/jonhusson/gdd_demo/blob/master/input/references.pdf); it is also in the downloaded input folder as `references.pdf`.

The `var/target_variables.txt` file can (and should!) be altered by the user, and principally consists of Python list of strings called `target_names`. Each object in the list is searched for within the set of five documents, using Python's regular expressions module. For example, when downloaded, this file is initialized as:

```
target_names = ['stromatol', r'\b' + 'Gamuza Formation' + r'\b']
```

meaning that words containing the string fragment `stromatol` will be returned (i.e., stromatolite, stromatolitic), as well as the phrase `Gamuza Formation`, provided the latter is bound by non-alphanumeric characters (e.g., `TheNotGamuza Formation` will not be returned). This list can be altered to anything you like:

```
target_names = ['Mexico', 'mountain']
```

## Running the script

In your Terminal, navigate to the root of the `gdd_demo` directory by typing:

```
cd /YOUR/PERSONAL/PATH/gdd_demo
```

then type:

```
python find_target.py
```

## Output description

The result of running `find_target.py` will be written to `output/output.tsv` as tab-delimited text file. Each row consists of a discovery of one of the strings specified in `var/target_variables.txt`.  The columns are described below:

Column | Description 
-------|--------
docid| identifier for the relevant document from the GeoDeepDive database, with metadata for it available through the GeoDeepDive API (i.e., [558dcf01e13823109f3edf8e](https://geodeepdive.org/api/articles?id=558dcf01e13823109f3edf8e))
sentid| identifier for sentence within the specified document where the `target` was extracted
target| discovered word or phrase (e.g., stromatolite, stromatolites, stromatolitic).
start\_idx| Pythonic index for start of discovered `target` (e.g., `0` would mean first word in that sentence).
end\_idx| Pythonic index for end of discovered `target`
adjective| words determined by [NLP](http://nlp.stanford.edu/) to be an adjective describing `target` (e.g., `Riphean, domal stromatolites`)
sentence| full sentence in which `target` was discovered

## Exercises
Using the provided Python script and some coding (in any language) of your own:

1. What adjectives are used to describe stromatolites?

2. Create a list of `document-sentence` tuples for sentences in this test set that contain BOTH `sandstone` and `limestone,` two commonly studied rock types.

## Additional Information

I recently added a simple script that seeks to determine the start of the "References" list in a given GDD document. This information may be helpful, because one may be interested in discarding phrase matches that happen within the reference list or bibliography, focusing only on the main body of the document. To run this extractor, simply type:

```
python find_target.py
```

The output is written to `output/ref_start.tsv`, and consists of `docid-sentid` tuples. For example, for docid `55adf5cde13823763a830891`, the associated sentid is `2783`. This means that for sentences with sentids less than 2783 are the main body of the text (for that particular document), and sentences with sentids greater than or equal to 2783 are determined to be part of the reference list.

