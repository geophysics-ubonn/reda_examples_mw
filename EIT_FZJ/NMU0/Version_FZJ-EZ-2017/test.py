#!/usr/bin/env python3
import sys
from reda.importers import eit160
import IPython.core.ultratb as ultratb
sys.excepthook = ultratb.VerboseTB(
    call_pdb=True,
)
emd, md = eit160.import_medusa_data(
    'eit_data_mnu0.mat', 'configs_large_dipoles_norrec.dat'
)

import IPython
IPython.embed()
