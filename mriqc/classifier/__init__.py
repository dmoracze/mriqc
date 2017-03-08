#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""

MRIQC is shipped with a random-forests classifier, using the combination of the
`ABIDE <http://fcon_1000.projects.nitrc.org/indi/abide/>`_ and
`DS030 <https://openfmri.org/dataset/ds000030/>`_ datasets as training sample.


To predict the quality labels (0="accept", 1="reject") on a features table
computed by ``mriqc`` with the default classifier, the command line
is as follows:

  ::

      mriqc_clf --load-classifier -X aMRIQC.csv -o mypredictions.csv


where ``aMRIQC.csv`` is the file generated by the ``group`` level run of
``mriqc``.

Custom classifiers can be fitted using the same ``mriqc_clf`` tool in fitting
mode:

  ::

      mriqc_clf --train aMRIQC_train.csv labels.csv --log-file fit_clf.log --save-classifier myclassifier.pklz

where ``aMRIQC_train.csv`` contains the IQMs calculated by ``mriqc`` and ``labels.csv`` contains
the matching ratings assigned by an expert.
The labels can be numerical (``-1``= exclude, ``0``= doubtful, ``1`` = accept) or textual ("bad", "fail" can be
used for exclude; "may be" or "maybe" for doubtful and "ok", "good" for accept).

The trained classifier can be then used for prediction on unseen data with
the command at the top, indicating now which classifier should be used:

  ::

      mriqc_clf --load-classifier myclassifier.pklz -X aMRIQC.csv -o mypredictions.csv


Predictions are stored as a CSV file, containing the BIDS identifiers as
indexing columns and the predicted quality label under the ``prediction`` column.


.. toctree::
    :maxdepth: 3

    cv/helpers
    cv/data
    cv/sklearn_ext

"""

