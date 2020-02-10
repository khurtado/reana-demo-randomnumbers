# Random number example

Simple yadage example to generate random numbers. Each job will generate a random number according to a seed input in reana.yam -> parameters -> rseed.
rseed is a list. Its size represents the number of jobs to be submitted and the numbers represent the seed number for the random number generator.


To use:

```
    $ reana-client create -n my-analysis
    $ export REANA_WORKON=my-analysis
    $ # upload input code and data to the workspace
    $ reana-client upload ./code
    $ reana-client list
    $ # start computational workflow
    $ reana-client start
    $ # should take about a minute
    $ reana-client status
    $ # list workspace files
    $ reana-client list
    $ # download output results (X = job number output result)
    $ reana-client download generate_X/randomnumber.txt
```
