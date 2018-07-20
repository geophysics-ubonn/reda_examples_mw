#!/usr/bin/env python3
import reda.importers.sip04 as sip04
df = sip04.import_sip04_data('sip_dataA.mat')
print(df[['a', 'b', 'm', 'n', 'frequency', 'z']])
