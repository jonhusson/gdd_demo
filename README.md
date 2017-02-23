## Wrangling text data from GeoDeepDive

The Python script `find_target.py` is a simplified component of the data-mining application utilized in [Peters, Husson and Wilcots (in press, Geology)](https://github.com/UW-Macrostrat/stromatolites_demo), which utilizes the [GeoDeepDive](https://geodeepdive.org) digital library to constrain the spatio-temporal distribution of stromatolite fossils across Earth history. The script searches for user-define word(s) or phrases in 5 provided USGS Technical Reports that have been processed and annotated by GeoDeepDive. The output is a list of `document-sentence` tuples that uniquely describe the location of the specific word(s) within the GeoDeepDive library, along with any adjectives that are used to describe those word(s). It serves as a demonstration of what data derived from GeoDeepDive looks like, and how it can be manipulated in simple ways to gain knowledge about the published literature.

## Input description

Input for this script are two text files: `input\sentences_nlp352` and `var\target_variables.txt`. The `sentences_nlp352` file comes from the GeoDeepDive library, and it is a TSV file that consists of 5 technical reports from the United States Geological Survey that have been parsed using [Stanford Natural Language Processing](http://nlp.stanford.edu/) (version 3.5.2). 

The `var\target_variables.txt` file can (and should!) be altered by the user, and principally consists of Python list of strings called `target_names`. Each object in the list is searched for within the set of five documents using Python's regex module. For example, when downloaded, this file is initialized as:

```
target_names = ['stromatol',r'\b' + 'Gamuza Formation' + r'\b']
```

meaning that words containing the string fragment `stromato` will be returned (i.e., stromatolite, stromatolitic), as well as the phrase `Gamuza Formation`, provided the latter is bound by non-alphanumeric characters (e.g., `TheNotGamuza Formation` will not be returned). This list can be altered to anything you like:

```
target_names = ['Mexico', 'mountain']
```

and typing `python find_target.py` in your Terminal, provided you are in the root of the `gdd_demo` directory, will run the script and find the specified word(s)/phrase(s).

## Output description

The result of running `find_target.py` will be written to `output\output.tsv` as tab-delimited text file. Each row consists of a discovery of the strings specified in `var\target_variables.txt`.  The columns are described below:

Column | Description 
-------|--------
docid| identifier for the relevant document from the GeoDeepDive database, with metadata for it available through the GeoDeepDive API (i.e., [558dcf01e13823109f3edf8e](https://geodeepdive.org/api/articles?id=558dcf01e13823109f3edf8e))
sentid| identifier for sentence within the specified document where the tuple was extracted
target| discovered word or phrase (e.g., stromatolite, stromatolites, stromatolitic).
start\_idx| Pythonic index for start of discovered `target` (e.g., `0` would mean first word in a sentence).
end\_idx| Pythonic index for end of discovered `target`
adjective| words determined by [NLP](http://nlp.stanford.edu/) to be an adjective describing `target` (e.g., `Riphean, domal stromatolites`)
sentence| full sentence in which `target` was discovered

## Exercises
Using the provided Python script and some coding (in any language) of your own:

1. What adjectives are used to describe stromatolites?

2. Create a list of `document-sentence` tuples for sentences in this test set that contain BOTH `sandstone` and `limestone,` two commonly studied rock types.
